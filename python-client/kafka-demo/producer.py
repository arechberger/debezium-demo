import json
import logging
import time

from kafka import KafkaProducer

from config import Settings

settings = Settings()


def on_send_success(record_metadata):
    logging.info(
        "topic: %s - partition %d - offset: %d",
        record_metadata.topic,
        record_metadata.partition,
        record_metadata.offset,
    )


def on_send_error(excp):
    logging.error("I am an errback", exc_info=excp)
    # handle exception

def send_kafka_msg(producer, data):
    producer.send(settings.kafka_topic, value=data).add_callback(
        on_send_success
    ).add_errback(on_send_error)

def main():
    logging.info(settings.dict())

    producer = KafkaProducer(
        bootstrap_servers=[settings.kafka_bootstrap_server],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    )

    i = 0
    if settings.send_initial_burst:
        for _ in range(settings.send_initial_burst):
            i += 1
            send_kafka_msg(producer, data={"number": i})

    while True:
        i += 1
        send_kafka_msg(producer, data={"number": i})
        time.sleep(settings.send_interval_sec)


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s:%(name)s:%(levelname)s:%(message)s", level=logging.INFO
    )
    main()
