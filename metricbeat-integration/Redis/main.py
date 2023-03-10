import json
import time

from redis.client import Redis


def get_redis_connection():
    return Redis(host='localhost', port=6379, db=0, encoding='utf-8', decode_responses=True)


def main():
    client = get_redis_connection()
    keyspace = 'redis:list'
    idx = 0
    for _ in range(100):
        values = {'data': 1, 'value': 0, 'idx': idx}
        client.rpush(keyspace, json.dumps(values))
        idx += 1
        time.sleep(0.1)
    print('list done')

    keyspace = 'redis:dict'
    for _ in range(100):
        values = {'data': 1, 'value': 0, 'idx': idx}
        client.hset(name=keyspace, mapping=values)
        idx += 1
        time.sleep(0.1)
    print('dict done')


if __name__ == '__main__':
    main()
