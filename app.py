from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.components.data_ingestion import DataIngestion
import sys
from src.DataScienceProject.components.data_transformation import DataTransformation, DataTransformationConfig
from src.DataScienceProject.components.model_trainer import ModelTrainer, ModelTrainerConfig

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        ##data ingestion code
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        # logging.info(f"Train data saved at: {train_path}")
        # logging.info(f"Test data saved at: {test_path}")
        data_ingestion.initiate_data_ingestion()

        ##data transforamtion code
        data_transformation =DataTransformation()
        train_arr, test_arr, preprocessor_obj  =data_transformation.initiate_data_transformation(train_path,test_path)

        ## model trainer code
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    except Exception as e:
        logging.info("Custom Exception ")
        raise CustomException(e, sys)