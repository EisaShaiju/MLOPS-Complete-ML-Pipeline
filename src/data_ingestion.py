import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

log_dirs='logs'
os.makedirs(log_dirs,exist_ok=True)

#setting the logger object of logging class
logger=logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

#setting the console handler to debug level
console_handler=logging.StreamHandler()
console_handler.setLevel('DEBUG')

#setting the file handler which will save log output to a file
log_file_path=os.path.join(log_dirs,'data_ingestion.log')
file_handler=logging.FileHandler(log_file_path)

#setting up the formatter to define which format the file handler and console handler should show the results
formatter=logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

