from config.env import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.local:
    DB_CONNECTION_STRING = 'sqlite:///monitoring.db'
    API_LOGFILE_LOG = "api_logfile.log"
else:
    DB_CONNECTION_STRING = 'postgresql://postgres:postgres@postgres:5432/postgres'
    API_LOGFILE_LOG = "/home/jovyan/api_logfile.log"
