import logging

from config.monitoring_config import API_LOGFILE_LOG

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(API_LOGFILE_LOG)
logger.addHandler(handler)
