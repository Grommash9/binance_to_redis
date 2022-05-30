import redis

redis = redis.Redis(decode_responses=True)

MYSQL = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'db': 'parser_data',
    # 'unix_socket': '/var/run/mysqld/mysqld.sock'
}