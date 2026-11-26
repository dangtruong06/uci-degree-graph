from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "UCI Degree Graph"
    database_url: str
    environment: str = "dev"
    anteater_api_base_url: str = "https://anteaterapi.com/v2/rest"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()