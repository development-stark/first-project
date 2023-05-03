import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Test-one API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///data.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    THREADS_PER_PAGE = 2
    DEBUG = True

class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = os.getenv('FLASK_DEBUG')


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = os.getenv('FLASK_DEBUG')
