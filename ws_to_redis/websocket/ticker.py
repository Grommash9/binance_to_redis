import json, websocket
socket = 'wss://stream.binance.com:9443/ws/!miniTicker'
from ws_to_redis.config import redis


def on_message(ws, message):
    json_message = json.loads(message)
    redis.set(f"binance_{json_message['s']}", json_message['c'])


def on_close(ws):
    print('closed')


def on_error(ws, message):
    raise ConnectionError(str(message))


ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close, on_error=on_error)
