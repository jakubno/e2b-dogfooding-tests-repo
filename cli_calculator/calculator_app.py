import click
from calc import add_numbers, multiply_numbers

@click.command()
@click.option('--add', nargs=2, type=float, help='Add two numbers.')
@click.option('--mult', nargs=2, type=float, help='Multiply two numbers.')
def cli(add, mult):
    if add:
        result = add_numbers(*add)
        click.echo(f"Result of addition: {result}")
    elif mult:
        result = multiply_numbers(*mult)
        click.echo(f"Result of multiplication: {result}")

if __name__ == '__main__':
    cli()
