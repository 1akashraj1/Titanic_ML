import pandas as pd
import numpy as np
import os
import sys
from src.exception import CustomException
from src.logging import logger
from src.utils import save_object
from dataclasses import dataclass

from pipeline import ColumnImputation


@dataclass
class DataPreprocessingConfig():
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataPreprocessor():
    def __init__(self):
        self.data_preprocessor_config = DataPreprocessingConfig()


    def data_preprocessing(self):
        try:
            logger('Loading the training and testing dataset')
            train_data, X_test_data = pd.read_csv('dataset\\train.csv'), pd.read_csv('dataset\\test.csv')
            
            
            logger('Splitting the train and test dataset')
            X_train_data = pd.concat([train_data.iloc[:,0], train_data.iloc[:,2:]])
            Y_train_data = train_data.iloc[:,1]
            
            logger('Merging Parch and SibSp cols')
            # Training data
            X_train_data['Family'] = (X_train_data['SibSp'] + X_train_data['Parch'])
            X_train_data['Family'] = X_train_data['Family'].apply(lambda x: 'Alone' if x == 0 else 'Not Alone')

            # Testing data
            X_test_data['Family'] = (X_test_data['SibSp'] + X_test_data['Parch'])
            X_test_data['Family'] = X_test_data['Family'].apply(lambda x: 'Alone' if x == 0 else 'Not Alone')


            logger('Splitting Cabin columns and extracting copartment and the room num')
            # Training dataset
            X_train_data['Room_num'] = X_train_data['Cabin'].str.strip().str.extract('(\d+)')
            X_train_data['Compartment'] = X_train_data['Cabin'].str.strip().str.extract("([a-zA-Z]+)", expand=False)

            # Testing dataset
            X_test_data['Room_num'] = X_test_data['Cabin'].str.strip().str.extract('(\d+)')
            X_test_data['Compartment'] = X_test_data['Cabin'].str.strip().str.extract("([a-zA-Z]+)", expand=False)

            logger('Dropping unnecessary columns')
            X_train_data.drop(['SibSp','Parch','Cabin','Name','Ticket'],axis = 1, inplace = True)
            X_test_data.drop(['SibSp','Parch','Cabin','Name','Ticket'],axis = 1, inplace = True)



            logger('Imputing the missing values')
            column_imputer_obj = ColumnImputation()
            preprocessor = column_imputer_obj.preprocessing()


            logger('Transformation of test and training data')
            X_train_transformed = preprocessor.fit_transform(X_train_data)
            X_test_trasformed = preprocessor.transform(X_test_data)


            save_object(
                self.data_preprocessor_config.preprocessor_obj_file_path,
                preprocessor

            )

            
            return (
                X_train_transformed, Y_train_data, X_test_trasformed
            )
        
            
            


        except Exception as e:
            raise CustomException(e,sys)



if __name__ == '__main__':
    my_data_preprocessor_obj = DataPreprocessor()

    X_train, Y_train, Xtest = my_data_preprocessor_obj.data_preprocessing()