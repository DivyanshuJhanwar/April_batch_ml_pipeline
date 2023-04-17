from datetime import datetime
import logging
import os, sys


# Creating a folder to capture the logs we will be defining in the basicConfig

LOG_DIR = "logs"

# I want Year, Month, Day, Hours, Minutes, Seconds

CURRENT_TIME_STAMP = f"log{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"


# Whenever we are going to create the folder we have to create a Extension as well, So for log we have 
# to define .log as we are going to create logs.log file and under this file we are going to capture 
# CURRENT_TIME_STAMP 
 
log_file_name = f"logs{CURRENT_TIME_STAMP}.log"

# Now we don't have logs file, So we have to create directory.

os.makedirs(LOG_DIR, exist_ok= True)

# Now lets join LOG_DIR with log_file_name
log_file_path = os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(filename= log_file_path,
                    filemode= "w",
                    format= '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO
                    )