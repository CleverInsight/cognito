# -*- coding: utf-8 -*-
import os
import six
import shutil
import yaml
import click
import json
import pickle
import logging
import pandas as pd
import numpy as np

from pyfiglet import figlet_format, Figlet
from prettytable import PrettyTable
from cognito import *
from cognito.table import Table
from cognito.story import get_interesting_stories
from datetime import datetime
from tornado import template
from tqdm import tqdm, trange



VERSION = 'version 0.0.1-beta-3'


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def read_yaml(filename):
    ''' take filename as parameter and convert yaml to ordereddict '''
    return yaml.load(open(filename))


custom_fig = Figlet(font='slant')
click.echo(custom_fig.renderText('cognito'))
click.echo(VERSION)



@click.group()
@click.option('--version', is_flag=True, default=False)
def cli(version):
    '''  
        Generate ML consumable datasets using advanced data preprocessing
        and data wrangling.        

        USAGE: \n
        $ cognito prepare -m ml --input filepath --out filepath 

    '''
    pass


@cli.command('report')
def report():

    preformat = """
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.8.2/css/bulma.min.css">
        <img src="https://cognito.readthedocs.io/en/latest/_images/logo.png" width="200px"/>
        <h3>Summary Report</h3>
        <button class="button is-success is-rounded" onclick="window.print()">Generate PDF</button>
    """

    file_loader = FileSystemLoader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
    env = Environment(loader=file_loader)
    template = env.get_template('index.html')
    print(template.render(data=preformat))
    

@cli.command('audit', short_help=": Audit the given dataset and generate report")
@click.option('--inp', '-i', help="Input dataset file in following format .csv", required=True, metavar='<path>')
@click.option('--save', '-o', help="Enter the filename to save html", metavar='<path>')
def audit(inp, save):
    
    if inp:
        start_time = datetime.now()
        description = PrettyTable(['Name', 'Values'])
        description.align['Name'] = "l"
        

        table = PrettyTable([
            'Features', 
            'Type', 
            'Value Type', 
            'Outliers', 
            'Missing', 
            '(%) Missing',
            'Distinct Count',
            'Min',
            'Mean',
            'Max',
            'Zeros',
            '(%) Zeros',
            'Memory Size'            
        ])
        try:
            df_raw = Table(inp)
            df = df_raw.data
            features = df.columns
            table.align["Features"] = "l"
            table.align["Value Type"] = "l"
            table.sortby = "Distinct Count"
            table.reversesort = True

            # Generate dynamic analytical stories
            stories = get_interesting_stories(df_raw)


            # Group duplicates
            dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})

            description.add_row(['Total variables', df.shape[1]])
            description.add_row(['Total Observations', df.shape[0]])
            description.add_row(['Missing Cells', df.isnull().sum().sum()])
            description.add_row(['(%) Missing Cells', df.isnull().sum().sum() / len(df)])
            description.add_row(['Duplicate Rows', dups['count'].sum() - dups.shape[0]])
            description.add_row(['(%) Duplicate Rows', (dups['count'].sum() - dups.shape[0]) / len(dups)])
            description.add_row(['Total Size of Memory', str(df.memory_usage().sum() / 1000) + 'KiB'])
            description.add_row(['🍋 Total Categorical', count_categorical(df)])
            description.add_row(['🔟 Total Continuous', len(df_raw.get_numerical().columns)])
            description.add_row(['Started at', start_time.strftime("%d-%b-%y %H:%M:%S")])

            for col in tqdm(features, ascii=True, desc="Auditing.. : "):
                table.add_row([
                    col.strip(),
                    df[col].dtypes,
                    type_of_variable(df[col]), 
                    check_outlier(df[col]),
                    check_missing(df[col]), 
                    column_missing_percentage(df[col]), 
                    distinct_count(df[col]),
                    count_min(df[col]),
                    count_mean(df[col]),
                    count_max(df[col]),
                    df[col].isin([0]).sum(),
                    round(df[col].isin([0]).sum() / len(df.columns), 2),
                    str(df[col].memory_usage() / 1000) + 'KiB'
                ])

            end_time = datetime.now()
            description.add_row(['Ended at', end_time.strftime("%d-%b-%y %H:%M:%S")])
            description.add_row(['Time Elapsed', (end_time - start_time).total_seconds()])



            # Save the report into HTML
            if save:
                
                desc_html = description.get_html_string()
                description_summary = desc_html.replace('<table>', '<table class="table is-bordered">')


                report_html = table.get_html_string()
                report_html = report_html.replace('<table>', '<table class="table is-bordered">')

                
                stories_json = [{'question': row['question'], 'answer': row['answer']} for row in stories]
                loader = template.Loader(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

                total_categorical = list(df_raw.get_categorical())
                total_continuous = list(df_raw.get_numerical())

                open(save + '.html', 'wb').write(loader.load("index.html").generate(**locals()))
                click.echo('Report generated with name ' + save + '.html')


            click.echo(description)
            click.echo(table)

        except FileNotFoundError as e:
            logging.warning("Given input file doesn't exists")
            print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
       



@cli.command('inverse', short_help=": Inverse re-transform generated dataset")
@click.option('--report', '-r', prompt='Select any one operation', type=click.Choice(['transform', 'report']))
def inverse(report):
    """ Inverse transform generated Machine Learning friendly dataset """

    if report == 'report':
        inverse_transform_report()
    elif report == 'transform':
        inverse_transform()


@cli.command('prepare', short_help=': Transform given dataset')
@click.option('--mode', '-m', type=click.Choice(['ml', 'decode', 'autoML', 'help', 'report'], \
    case_sensitive=False), help="Set any mode such as `prepare`, `autoML`, `clean`", metavar='<path>')
@click.option('--inp', '-i', help="Input dataset file in following format .csv", required=True, metavar='<path>')
@click.option('--out', '-o', help="Select output desitnation", required=True, metavar='<path>')
def prepare(mode, inp, out):
    """ Transform the given dataset file """

    if mode == 'help':
        # log("Cognito CLI", color="blue", figlet=True)
        click.echo(custom_fig.renderText('cognito'))


    if mode == 'ml':

        df = Table(inp)
        response, encoder = df.generate()
        click.echo(save_to(out, response, encoder))


    if mode == 'report':
        
        df = Table(inp)
        table = PrettyTable(['Features', 'Feature Type', 'Outliers', '% of outliers', 'Missing', '%of missing'])
        for col in df.columns():
            table.add_row([col, '', '', '', '', ''])
        click.echo(table)   



if __name__ == '__main__':
    cli()
