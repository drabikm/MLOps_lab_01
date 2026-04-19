# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator
from yaml import safe_load


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET_VALUE: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed_values = ["prod", "dev", "test"]
        if value not in allowed_values:
            raise ValueError("Invalid value for ENVIRONMENT")
        else:
            return value

    @classmethod
    def gpg_secrets(cls):
        try:
            with open("secrets.yaml", "r") as secrets:
                return safe_load(secrets)
        except FileNotFoundError:
            print("The secrets.yaml file does not exist")
            return {}

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            cls.gpg_secrets,
            file_secret_settings,
        )
