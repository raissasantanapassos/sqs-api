from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Configuração da aplicação
    app_name: str = "SQS API"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    # Configurações AWS
    aws_region: str = "us-east-1"
    aws_access_key_id: str = "test"
    aws_secret_access_key: str = "test"
    aws_endpoint_url: str | None = None  # None = AWS real, ou URL do LocalStack

    # Configurações SQS
    sqs_queue_name: str = "main-queue"
    sqs_dlq_name: str = "main-queue-dlq"

    # Configuração do Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",  # Lê do arquivo .env
        env_file_encoding="utf-8",
        case_sensitive=False,  # AWS_REGION ou aws_region funcionam
    )

settings = Settings()