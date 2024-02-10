#!/usr/bin/env python
import datetime
import json

import click

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as handle:
        return json.load(handle)

def process(data, key):
    # dict_keys([
    #    'fear_and_greed',
    #    'fear_and_greed_historical',
    #    'market_momentum_sp500',
    #    'market_momentum_sp125',
    #    'stock_price_strength',
    #    'stock_price_breadth',
    print(data.keys())
    h = data[key]
    for x in h['data']:
       t = datetime.datetime.fromtimestamp(x["x"] / 1000)
       print(f"{t} {x['y']}")


@click.command()
@click.argument("filename")
def main(filename):
    data = load_data(filename)
    process(data, 'fear_and_greed_historical')


if __name__ == '__main__':
    main()
