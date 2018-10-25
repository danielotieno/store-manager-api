"""Set up environment specific configurations"""
import os


class Config():
    """Parent configuration class"""
    DEBUG = False
    SECRET = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')


class Development(Config):
    """Configuration for development environment"""
    DEBUG = True


class Testing(Config):
    """Configuration for testing environment"""
    TESTING = True
    DEBUG = True
    SECRET = os.getenv('SECRET_KEY')
    DATABASE_TEST_URL = os.getenv('DATABASE_TEST_URL')


class Production(Config):
    """Configuration for production environment"""
    DEBUG = False
    TESTING = False


# The dictionary app_config is used to export the environments we've specified. It's convenient to have it so that we can import the config under its name tag in future.
app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}
