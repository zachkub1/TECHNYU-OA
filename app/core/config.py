from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ANTHROPIC_API_KEY: str = ""
    START_TIME: int = 540   # 9:00 AM in minutes from midnight
    MAX_HOURS: int = 10

    model_config = {"env_file": ".env"}


settings = Settings()
