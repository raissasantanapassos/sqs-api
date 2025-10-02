from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SQS API"
    debug: bool = False
    aws_region: str = "us-east-1"

    class Config:
        env_file = ".env"

settings = Settings()