from config.env import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.local:
    DB_CONNECTION_STRING = 'postgresql://postgres:postgres@0.0.0.0:5432/postgres'
else:
    DB_CONNECTION_STRING = 'postgresql://postgres:postgres@postgres:5432/postgres'
