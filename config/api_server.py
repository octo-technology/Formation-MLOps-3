import configparser

from config.env import ENVIRONMENT, EnvironmentType

if ENVIRONMENT == EnvironmentType.local:
    SERVER_ADRESS = '/'
else:
    # Specific code to run on dslab
    config = configparser.ConfigParser()
    config.read('api_conf.ini')
    SERVER_ADRESS = config['server']['address']
    # End of specific code
