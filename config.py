"""Set up environment specific configurations"""
import os


class Config():
    """Parent configuration class"""
    DEBUG = False
    SECRET = os.getenv('SECRET_KEY')


class Development(Config):
    """Configuration for development environment"""
    DEBUG = True


class Testing(Config):
    """Configuration for testing environment"""
    TESTING = True
    DEBUG = True
    SECRET = os.getenv('SECRET_KEY')


class Production(Config):
    """Configuration for production environment"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}