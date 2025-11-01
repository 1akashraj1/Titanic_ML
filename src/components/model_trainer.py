import numpy as np
import pandas as pd
import os
import sys

from src.utils import save_object
from src.exception import CustomException
from src.logging import logger

from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model_trainer.pkl')

class ModelTrainer:
    logger('Model Trainer initiation')
    def __init__(self):
        self.trained_model_config = ModelTrainerConfig()
    
    def model_training(self,X_train, Y_train, X_test):
        try:
            logger('Object of LR')
            lr = LogisticRegression(max_iter=1000)

            logger('LR prediction')
            lr.fit(X_train,Y_train)

            Y_train_pred_lr = lr.predict(X_train)

            Y_test_pred_lr = lr.predict(X_test)

            X_train_score_lr = r2_score(Y_train,Y_train_pred_lr)


            logger('Object of DT')
            dt = DecisionTreeRegressor(max_depth=15,random_state=2)
            dt.fit(X_train,Y_train)

            logger('DT prediction')
            Y_train_pred_dt = dt.predict(X_train)

            Y_test_pred_dt = dt.predict(X_test)

            X_train_score_dt = r2_score(Y_train,Y_train_pred_dt)

            best_score = max(X_train_score_dt,X_train_score_lr)
            print(best_score,X_train_score_lr,X_train_score_dt)

            
            if X_train_score_dt >= X_train_score_lr:
                best_model = dt
                pd.DataFrame({
                    'PassengerId': X_test[:,6].astype('int32'),
                    'Survived': Y_test_pred_dt.astype('int32')
                    }).rename_axis('Index').to_csv(os.path.join('artifacts','test_pred.csv'),index=False)
            else:
                best_model = lr
                pd.DataFrame({
                    'PassengerId': X_test[:,6],
                    'Survived': Y_test_pred_lr
                    }).rename_axis('Index').to_csv(os.path.join('artifacts','test_pred.csv'),index=False)


            save_object(
                file_path=self.trained_model_config.trained_model_file_path,
                obj=best_model
            )

            return best_score,best_model
        except Exception as e:
            raise CustomException(e,sys)
    # alias for backwards compatibility / alternative caller name
    train_model = model_training