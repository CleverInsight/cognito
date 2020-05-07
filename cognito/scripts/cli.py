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
from cognito.story import Story
from cognito.connect import SQL
from datetime import datetime
from tornado import template
from tqdm import tqdm, trange
from .click_default_group import DefaultGroup




VERSION = 'VERSION: 0.0.1-beta-3'


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



@click.group(cls=DefaultGroup, default='--help', default_if_no_args=True, invoke_without_command=True)
@click.option('--version', '-v',  is_flag=True, default=False)
def cli(version):
    '''  
        Generate ML consumable datasets using advanced data preprocessing
        and data wrangling.        

        USAGE: \n
        $ cognito prepare -m ml --input filepath --out filepath 

    '''

    if version:
        click.echo(VERSION)


@cli.command('audit', short_help=": Audit the given dataset and generate report")
@click.option('--inp', '-i', help="Input dataset file in following format .csv", required=True, metavar='<path>')
@click.option('--save', '-o', default='cognito', help="Enter the filename to save html", metavar='<path>')
def audit(inp, save):
 
    if inp:
        generate_audit_report(Table(inp), save)
        

@cli.command('connect', short_help=": Connect to different datasources")
@click.option('--conf', '-c', help="Input configuration YAML file path", required=True, metavar='<path>')
@click.option('--mode', '-m', type=click.Choice(['audit', 'download', 'prepare', 'inverse'], case_sensitive=False), \
    help="Set any mode such as `prepare`, `audit`, `inverse`", required=False)
@click.pass_context
def connect(ctx, conf, mode):
    
    # Returns the SQL Class 
    df = SQL(conf)

    if mode == 'audit':        
        df.data.drop_cardinality()
        generate_audit_report(df.data, 'makefiles')


    elif mode == 'download':
        df.save('makefiles.csv')
        
        


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
