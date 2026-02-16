import click
from mylib.bot import scrape


@click.command()
@click.option("--name", prompt="Wikipedia page to scrape", help="Web page we want to scrape")
def cli(name):
    result = scrape(name)
    click.echo(click.style(f"{result}:", bg="white", fg="blue"))


if __name__ == "__main__":
    cli()