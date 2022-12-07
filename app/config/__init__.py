import os

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7' if 'API_PREFIX' not in os.environ else os.getenv('SECRET_KEY')
DATABASE_URL = 'sqlite:///database.db' if 'DATABASE_URL' not in os.environ else os.getenv('DATABASE_URL')