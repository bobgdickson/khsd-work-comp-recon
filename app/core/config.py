from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "khsd-work-comp-recon"
    DATABASE_URL: str = "none"
    PS_DB_URL: str = "none"
    PASSPHRASE: str = "default_passphrase"

    class Config:
        env_file = ".env"

settings = Settings()