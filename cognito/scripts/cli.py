import os
import six
import shutil
import yaml
import click
import pickle
import pandas as pd
from pyfiglet import figlet_format, Figlet
from prettytable import PrettyTable
from cognito.table import Table
from datetime import datetime
from tqdm import tqdm, trange



def get_all_files():
    import os
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    return files


def save_to(path, df, encoder):
    """
    Save the encoded dataframe to csv file and 
    picle file.
    
    :param      path:     The path
    :type       path:     { type_description }
    :param      df:       { parameter_description }
    :type       df:       { type_description }
    :param      encoder:  The encoder
    :type       encoder:  { type_description }
    """
    filename = os.path.basename(path)

    if '.' in filename:
        fname, ext = filename.split('.')
    else:
        fname = filename

    path = os.path.dirname(path)
    save_path = os.path.join(path, fname)

    # make directory
    try:
        os.mkdir(save_path)

        #filenames
        pkl_file = os.path.join(save_path, 'encoder.pkl')
        df_file = os.path.join(save_path, filename)

        df.to_csv(df_file, index=False)
        f = open(pkl_file,"wb")
        pickle.dump(encoder, f)
        f.close()

        return df

    except Exception as e:

        click.echo(
            click.style(
                "Abort: The {} file already exists.", fg="red"
            ).format(os.path.join(save_path, filename)), err=True)
    

    



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


custom_fig = Figlet(font='slant')
click.echo(custom_fig.renderText('cognito'))

@click.group()
def cli():
    '''  
        Generate ML consumable datasets using advanced data preprocessing
        and data wrangling.        

        USAGE: \n
        $ cognito transform --input filepath --out filepath 


    '''


@cli.command('reverse', short_help=": re-transform generated dataset")
def reverse():
    """ Reverse transform generated Machine Learning friendly dataset """
    pass

@cli.command('prepare', short_help=': transform given dataset')
@click.option('--mode', '-m', type=click.Choice(['prepare', 'decode', 'autoML', 'help', 'report'], \
    case_sensitive=False), help="Set any mode such as `prepare`, `autoML`, `clean`", metavar='<path>')
@click.option('--inp', '-i', help="Input dataset file in following format .csv", required=True, metavar='<path>')
@click.option('--out', '-o', help="Select output desitnation", required=True, metavar='<path>')
def prepare(mode, inp, out):
    """ Transform the given dataset file """

    if mode == 'help':
        # log("Cognito CLI", color="blue", figlet=True)
        click.echo(custom_fig.renderText('cognito'))


    if mode == 'prepare':

        df = Table(inp)
        response, encoder = df.generate()
        click.echo(save_to(out, response, encoder))


    if mode == 'autoML':
        df = Table(inp)
        click.echo(df.total_columns())  


    if mode == 'report':
        
        df = Table(inp)
        
        table = PrettyTable(['Features', 'Feature Type', 'Outliers', '% of outliers', 'Missing', '%of missing'])

        for col in df.columns():
            table.add_row([col, '', '', '', '', ''])
        click.echo(table)   

    if mode == 'decode':

        with trange(11) as t:
            for i in t:
                t.set_description('C(x) decoding %i' % i)
                sleep(0.1)
        click.echo('Completed decoding')
        click.echo(get_all_files())


if __name__ == '__main__':
    cli()




