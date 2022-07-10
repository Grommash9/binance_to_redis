# импортируем модуль requests что бы слать запросы, если пишет что его
# нет можно установить его командой pip install requests введенной в Terminal PyCharm
import requests

# получаем данные о торовли с бинанс и делаем из них список
data = requests.get('https://api1.binance.com/api/v3/exchangeInfo').json()

# идем по списку монет и достаем только нужные нам
for coin in data['symbols']:
    # проверяем открыта ли торговля и можно ли торговать на споте
    if coin['status'] == 'TRADING' and coin['isSpotTradingAllowed']:
        print(coin)
        print(coin['baseAsset'], coin['quoteAsset'])
