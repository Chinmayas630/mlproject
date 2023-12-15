from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion,DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has stared")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()

        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("this one type of error")
        raise CustomException(e,sys)
