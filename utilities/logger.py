import logging
import os

def get_logger():

   log_dir = "logs"
   os.makedirs(log_dir, exist_ok=True)

   log_file = os.path.join(log_dir,  "test_log.log")


   logger = logging.getLogger("automation")
   logger.setLevel(logging.INFO)

   file_handler = logging.FileHandler(log_file)
   formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
   file_handler.setFormatter(formatter)

   if not logger.handlers:
      logger.addHandler(file_handler)

   return logger


