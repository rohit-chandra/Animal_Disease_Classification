# for logging functionality

import os
import sys
import logging

# format of logging message
loggin_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create a logging directory
log_dir = "logs"
# create a log file
log_file_path = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok = True)

# initialize logging
logging.basicConfig(
    level = logging.INFO, 
    format = loggin_str,
    
    handlers = [
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
    
)

logger = logging.getLogger("chicken_disease_classification_logger")