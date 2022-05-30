import redis

redis = redis.Redis(decode_responses=True)

# так мы можем получить все ключи которые начинаються с бинанс и есть у нас
print(redis.keys('binance_*'))

# в цикле можем пройтись по всем названиям ключей и получить их значения
for keys in redis.keys('binance_*'):
    print(keys, redis.get(keys))

# что бы получить данные по определенной валюте пишем
print(redis.get('binance_VIDTBUSD'))

# в цикле можем пройтись по всем названиям ключей и получить их значения удалив подпись бинанс
for keys in redis.keys('binance_*'):
    print(keys[8:], redis.get(keys))


# функция для получения словаря с названиями криптовалютных пар и значениями их последней цены
def get_binance_dict() -> dict:
    binance_dict = dict()
    for keys in redis.keys('binance_*'):
        binance_dict[keys[8:]] = redis.get(keys)
    return binance_dict

print(get_binance_dict())