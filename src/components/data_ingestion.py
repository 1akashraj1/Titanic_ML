import os
import sys
from src.logging import logger
from src.exception import CustomException
from dataclasses import dataclass
import pandas as pd

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
            train_dataset = pd.read_csv('dataset\\train.csv')
            test_dataset = pd.read_csv('dataset\\test.csv')

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

    train_data_path, test_data_path = my_obj.my_data_ingestion()
    print(test_data_path, train_data_path)