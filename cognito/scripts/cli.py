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

@pass_config
def cli(config, verbose):
    '''  Welcome to Sparx CLI '''
    config.verbose = verbose



# @cli.command()
# @click.option('--count', default=1, help='number of greetings')
# @click.argument('name')
# def hello(count, name):
#     for x in range(count):
#         click.echo('Hello %s!' % name)


@cli.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.argument('country')
def cli(verbose, name, country):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello {0}".format(country))
    for n in name:
        click.echo('Bye {0}'.format(n))



log("Cognito CLI", color="green", figlet=True)
