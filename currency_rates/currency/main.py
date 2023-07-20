import click
from datetime import datetime
import requests


def current_rates(date):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

    query_params = {
        'date': date,
    }

    response = requests.get(url, params=query_params)

    return response


@click.command()
@click.option('--date', default=datetime.today().strftime('%Y-%m-%d'), help='Day')
@click.option('--code', default='USD', help='Currency')
def cli(code, date):
    a = current_rates(date)
    click.echo(a)


if __name__ == '__main__':
    cli()
