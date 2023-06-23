from config.env import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.local:
    DB_CONNECTION_STRING = 'sqlite:///monitoring.db'
else:
    DB_CONNECTION_STRING = 'postgresql://postgres:postgres@postgres:5432/postgres'
