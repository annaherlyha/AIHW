import logging.config
from os import path

file_dir = path.dirname(path.abspath(__file__))
log_file_path = path.join(file_dir, 'logging.ini')

logging.config.fileConfig(log_file_path)
logger = logging.getLogger(__name__)
