import json
import random
import time

from faker import Faker
from redis import Redis

MAX_ITERATIONS = 1000


def get_redis_connection() -> Redis:
    return Redis(
        host='localhost',
        db=0,
        decode_responses=True,
        encoding='utf-8'
    )


def generate_data() -> dict:
    faker = Faker()
    salary = random.randint(100, 1000000)
    return {
        'name': faker.name(),
        'b_day': faker.date(),
        'ean': faker.ean8(),
        'address': faker.address(),
        'city': faker.city(),
        'browser': faker.user_agent(),
        'ip': faker.ipv4(),
        'salary': salary
    }


def main():
    api = get_redis_connection()
    stream_key = "user_data"
    api.flushdb()
    for i in range(MAX_ITERATIONS):
        data = generate_data()
        api.rpush(stream_key, json.dumps(data))
        print('[!] Data added: ', data)
        time.sleep(3)


if __name__ == '__main__':
    main()
