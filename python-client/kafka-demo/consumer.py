import json
import logging
import time

from kafka import KafkaConsumer

from config import Settings


def main():
    settings = Settings()

    consumer = KafkaConsumer(
        bootstrap_servers=[settings.kafka_bootstrap_server],
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        group_id=settings.kafka_consumer_group,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )
    consumer.subscribe(settings.kafka_topic)

    for msg in consumer:
        logging.info(msg)
        time.sleep(0.1)

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s:%(name)s:%(levelname)s:%(message)s", level=logging.INFO
    )
    main()
