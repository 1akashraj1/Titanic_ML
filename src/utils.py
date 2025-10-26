import sys
import os
from src.exception import CustomException
# from src.logging import logger
import pandas as pd
import dill



def load_dataset():

    train_dataset = pd.read_csv('dataset\\train.csv')
    test_dataset = pd.read_csv('dataset\\test.csv')
    return (train_dataset, test_dataset)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)