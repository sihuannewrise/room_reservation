from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок в core.congig.py'
    app_description: str = 'Описание в core.congig.py'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
