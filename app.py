from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException

if __name__=="__main__":
    logging.info("The execution has stared")

    try:
        a=1/0
    except Exception as e:
        logging.info("this one type of error")
        raise CustomException(e,sys)
