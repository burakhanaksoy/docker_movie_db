"""Flask config class."""
import os


class Config:
    """Set Flask configuration vars."""
    # General Config
    TESTING = True
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://postgres:test123@0.0.0.0:5401/movie_db')
    SQLALCHEMY_USERNAME = 'postgres'
    SQLALCHEMY_PASSWORD = 'test123'
    SQLALCHEMY_DATABASE_NAME = 'movie_db'
    SQLALCHEMY_TABLE = 'migrations'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False