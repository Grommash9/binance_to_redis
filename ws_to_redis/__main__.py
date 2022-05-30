from ws_to_redis.websocket.ticker import ws

if __name__ == '__main__':
    while True:
        ws.run_forever()

