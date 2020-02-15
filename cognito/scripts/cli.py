# Cognito Command Line Utility 

import os
import six
import yaml
import click
import shutil
import cognito
from pyfiglet import figlet_format
from prettytable import PrettyTable

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def read_yaml(filename):
    ''' take filename as parameter and convert yaml to ordereddict '''
    return yaml.load(open(filename))

def log(string, color, font="slant", figlet=False):
    '''
    Colors logging for better interfacing CLI
    '''
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)



class Config(object):
    '''
    Config verbose for click group commands
    '''
    def __init__(self):
        self.verbose = False
        

pass_config = click.make_pass_decorator(Config, ensure=True)



@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--input', default=1, help='Input source file only .csv accepted')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

@pass_config
def cli(config, verbose):
    '''  Welcome to Cognito CLI '''
    config.verbose = verbose


@cli.command()
@click.option('--input', '-i', is_flag=True, default=1, help='Input file only .csv accepted')
def intake(input):
	click.echo(input)

@cli.command()
def list():
    ''' List of all files '''
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        click.echo(f)



@cli.command()
def authors():
    ''' List of all authors ''' 
    people = ['A', 'B', 'C']
    for person in people:
        click.echo(person)


log("Cognito CLI", color="green", figlet=True)

