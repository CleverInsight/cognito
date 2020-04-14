import os
import six
import shutil
import yaml
import click
import pickle
import pandas as pd
from pyfiglet import figlet_format, Figlet
from prettytable import PrettyTable
from cognito import save_to, get_all_files, inverse_transform
from cognito.table import Table
from datetime import datetime
from tqdm import tqdm, trange


    

def read_yaml(filename):
    ''' take filename as parameter and convert yaml to ordereddict '''
    return yaml.load(open(filename))


custom_fig = Figlet(font='slant')
click.echo(custom_fig.renderText('cognito'))

@click.group()
@click.option('--version', default=True, help="Get cognito version")
def cli(version):
    '''  
        Generate ML consumable datasets using advanced data preprocessing
        and data wrangling.        

        USAGE: \n
        $ cognito prepare -m ml --input filepath --out filepath 


    '''
    pass



@cli.command('inverse', short_help=": Inverse re-transform generated dataset")
def inverse():
    """ Inverse transform generated Machine Learning friendly dataset """
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




