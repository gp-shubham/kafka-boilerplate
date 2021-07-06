from kafka import KafkaConsumer
import json

from kafka.consumer import group


if __name__ == '__main__':
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='35.244.20.220:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
    )
    print("Starting the Consumer".center(50, '-'))
    for msg in consumer:
        print(f"Registered User = {json.loads(msg.value)}")