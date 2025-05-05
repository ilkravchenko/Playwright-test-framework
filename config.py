from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

    login_url: str
    base_url: str
    email: str
    password: str
    admin_username: str
    admin_password: str


get_ui_config = Settings()
