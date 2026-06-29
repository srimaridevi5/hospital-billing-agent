from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME:str

    DEBUG:bool

    HOST:str

    PORT:int

    DATABASE_URL:str

    JWT_SECRET:str

    JWT_ALGORITHM:str

    GROQ_API_KEY:str

    class Config:
        env_file=".env"

settings=Settings()