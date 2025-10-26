import os
import sys
from src.logging import logger
from src.exception import CustomException
from src.utils import load_dataset
from dataclasses import dataclass
import pandas as pd
from src.components.data_preprocessing import DataPreprocessor

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')


class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()


    def my_data_ingestion(self):
        logger('Started the data ingestion')

        try:
            train_dataset, test_dataset = load_dataset()


            logger('Creating artifacts folder')
            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)


            logger('Sending the training and test dataset to the artifacts folder')
            train_dataset.to_csv(self.data_ingestion.train_data_path,index=False, header=True)
            test_dataset.to_csv(self.data_ingestion.test_data_path,index=False,header=True)


            logger('Data ingestion completed')
        
            return (
            self.data_ingestion.train_data_path,
            self.data_ingestion.test_data_path
        )
    

        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == '__main__':
    my_obj = DataIngestion()
    my_data_preprocessor_obj = DataPreprocessor()

    train_data_path, test_data_path = my_obj.my_data_ingestion()

    X_train, Y_train, Xtest = my_data_preprocessor_obj.data_preprocessing
    