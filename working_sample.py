import time
import requests

pairs_dict = dict()

data = requests.get('https://api1.binance.com/api/v3/exchangeInfo').json()

start_time = time.time()

for coin in data['symbols']:
    if coin['status'] == 'TRADING' and coin['isSpotTradingAllowed']:
        if coin['baseAsset'] not in pairs_dict.keys():
            pairs_dict[coin['baseAsset']] = [coin['quoteAsset']]
        else:
            pairs_dict[coin['baseAsset']].append(coin['quoteAsset'])
        if coin['quoteAsset'] not in pairs_dict.keys():
            pairs_dict[coin['quoteAsset']] = [coin['baseAsset']]
        else:
            pairs_dict[coin['quoteAsset']].append(coin['baseAsset'])


bundles_list = ({0: {'base': currency, 'target': variants}, 1: {'base': variants, 'target': second_variants}, 2: {'base': second_variants, 'target': currency}} for currency in pairs_dict.keys() for variants in pairs_dict[currency] for second_variants in pairs_dict[variants] if variants in pairs_dict[currency])

print(time.time() - start_time)

for pairs in bundles_list:
    with open('bundles_list.txt', 'a') as data_file:
        data_file.write(f"{pairs[0]['base']} > {pairs[0]['target']} |  {pairs[1]['base']} > {pairs[1]['target']}  |  {pairs[2]['base']} > {pairs[2]['target']}\n")
