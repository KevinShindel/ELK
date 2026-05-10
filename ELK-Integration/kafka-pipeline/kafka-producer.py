from faker import Faker
from kafka3 import KafkaProducer
import json
from time import sleep

fake = Faker()
MAX_PRODUCED_CNT = 10000


def get_reg_user() -> dict:
    return {
        "name": fake.name(),
        # "address": fake.address(),
        "created_at": fake.year()
    }


def json_serializer(data: dict) -> bytes:
    return json.dumps(data).encode('utf-8')


def main():
    producer = KafkaProducer(bootstrap_servers=["host.docker.internal:9092"],
                             value_serializer=json_serializer)
    value = get_reg_user()
    for i in range(MAX_PRODUCED_CNT):
        print(i, "[!] Produced: ", value)
        producer.send(topic='registered_user', value=value)
        sleep(3)


if __name__ == '__main__':
    main()
