from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_name: str = "api_music"
    mongo_url: str = "mongodb://localhost:27017"
    db_name: str = "db_music"
    minute_rate_limit: int = 60


def get_settings():
    return Settings()
