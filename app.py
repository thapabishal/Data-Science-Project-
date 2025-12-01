from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Train data saved at: {train_path}")
        logging.info(f"Test data saved at: {test_path}")
        #data_ingestion.initiate_data_ingestion
    except Exception as e:
        logging.info("Custom Exception ")
        raise CustomException(e, sys)