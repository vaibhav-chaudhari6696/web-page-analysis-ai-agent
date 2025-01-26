from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'default_secret_key')
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')

settings = Settings()