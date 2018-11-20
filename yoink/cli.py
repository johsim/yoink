"""Cli for yoink"""
import click

@click.command()
def cli():
    """Yoink CLI"""
    print('Save all your snippets')


@click.command()
def add():
    """Add new snippet"""
    pass

@click.command()
def add():
    """Delete snippet"""
    pass



if __name__ == '__main__':
    cli()
