# Skeleton of a CLI

import click
import cognito


@click.command('cognito')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(cognito.has_legs)
