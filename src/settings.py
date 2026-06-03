from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    postgres_connection_string: str = "postgresql+asyncpg://postgres:postgres@localhost:5434/ads_db"
    kafka_brokers: str = "localhost:9092"
    kafka_topic_marketplace_ads: str = "ads"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    auth_service_url: str = "http://localhost:8000"

    @property
    def database_url(self) -> str:
        url = self.postgres_connection_string
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url

    @property
    def kafka_bootstrap_servers(self) -> str:
        return self.kafka_brokers

    @property
    def kafka_topic_ads(self) -> str:
        return self.kafka_topic_marketplace_ads
