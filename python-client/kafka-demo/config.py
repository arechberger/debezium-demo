from pydantic import BaseSettings


class Settings(BaseSettings):
    kafka_bootstrap_server: str = "kafka:9092"
    send_interval_sec: int = 1
    kafka_topic: str
    kafka_consumer_group: str = "my-group"
    send_initial_burst: int = 0
