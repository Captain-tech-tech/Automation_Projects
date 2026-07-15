# logger.py don't know anything about file_handler.py nut file_handler.py uses it --> this is called one-way dependency


import logging
from logging.handlers import RotatingFileHandler 
from pathlib import Path 

log_dir = Path("Logs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir/"project.log"

logger = logging.getLogger("project_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s::%(levelname)s::%(message)s")

# 5*1024*1024  means  5 MB
filehandler = RotatingFileHandler(log_file,maxBytes= 5 * 1024 * 1024,backupCount=5)

filehandler.setFormatter(formatter)

logger.addHandler(filehandler)




















