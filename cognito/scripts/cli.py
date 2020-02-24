import os
import six
import shutil
import yaml
import click
from pyfiglet import figlet_format
from prettytable import PrettyTable
from cognito.table import Table



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
    '''  Welcome to Cognito CLI '''
    config.verbose = verbose



@cli.command()
@click.argument('mode')
@click.option('--inp', '-i')
@click.option('--out', '-o')
def mode(mode, inp, out):
    ''' Set any mode such as `prepare`, `autoML`, `clean` ''' 
    table = PrettyTable(['Cognito v-0.0.1'])

    if not mode:
        click.echo("Missing")
    else:
        _mode = mode

    if not inp:
        click.echo('-i Missing')
    else:
        _input = inp
    
    if not out:
        click.echo('-o Missing')
    else:
        _output = out

    if _mode == 'prepare':
        df = Table(_input)
        print(df.summary())

    if _mode == 'autoML':
        df = Table(_input)
        print(df.total_columns())        


def main():
    log("Cognito CLI", color="blue", figlet=True)


if __name__ == "cognito":
    main()
