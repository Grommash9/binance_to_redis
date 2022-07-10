# импортируем модуль requests что бы слать запросы, если пишет что его
# нет можно установить его командой pip install requests введенной в Terminal PyCharm
import requests
import time

# получаем данные о торовли с бинанс и делаем из них список
data = requests.get('https://api1.binance.com/api/v3/exchangeInfo').json()

# идем по списку монет и достаем только нужные нам
for coin in data['symbols']:
    # проверяем открыта ли торговля и можно ли торговать на споте
    if coin['status'] == 'TRADING' and coin['isSpotTradingAllowed']:
        print(coin)
        print(coin['baseAsset'], coin['quoteAsset'])


# задача состоит в том что бы из пар baseAsset и quoteAsset составить торговые цепочки, которые должны
# начинаться и заканчиваться одной и той же валютой, не ванжо какой. По вомзожности сделать редактируемое значение длины
# цепочек которые мы хотим получать, то есть цепочки из 5 пар и более вот пример того что должно получиться на выходе
# 'USDT/BTC' -> 'BTC/LTC' -> 'LTC/USDT'
# Критически важна скорость выполнения кода. Её можно замерять вот так:


# сохраняем текущее время в переменную
start_time = round(time.time())

# выполняем какой-то код
for x in range(0,50000000):
    y = x * x

# проверяем время выполнения вычитая из текущего время стартовое
print(f'Время выполнения: {round(time.time()) - start_time} секунд')
