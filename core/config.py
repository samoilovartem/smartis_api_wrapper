from pydantic import BaseSettings, Field


class Config(BaseSettings):
    base_url: str = Field('https://my.smartis.bi/api/', env='BASE_URL')

    class Config:
        env_file = '../.env'


config = Config()
