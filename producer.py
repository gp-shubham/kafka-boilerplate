from data import get_registered_user
from kafka import KafkaProducer
import json
import time
import random

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partitioner(key, all, available):
    """Define to select specific partition in topic"""
    return 0


producer = KafkaProducer(
    bootstrap_servers=['35.244.20.220:9092'],
    value_serializer=json_serializer,
    # partitioner=get_partitioner
)


if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        # print(registered_user)
        print(json.dumps(registered_user, indent=2))
        producer.send("registered_user", registered_user)
        time.sleep(random.randint(1,5))