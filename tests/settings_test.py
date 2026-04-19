from dotenv import load_dotenv
from settings import Settings

load_dotenv("config/.env.test")


def test_loads_env_secrets():
    settings = Settings()
    assert settings.ENVIRONMENT, "test"


def test_loads_yaml_secrets():
    settings = Settings()
    assert settings.SECRET_VALUE == "abc12345", "Yes, it is there and it is correct"
