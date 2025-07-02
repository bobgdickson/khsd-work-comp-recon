from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "khsd-work-comp-recon"
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    class Config:
        env_file = ".env"

settings = Settings()