"""
__main__.py
Aaron Cumming
1/22/2025

The output of the project can be edited in this file.
"""



def main():
    print("Hello from task-timer!")

if __name__=='__main__':
    main()

import click

@click.command()
def main():
    """This is my main cli"""

    click.echo("Hello World")