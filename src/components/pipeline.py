import pandas as pd
import numpy as np
import os
import sys
from src.exception import CustomException
from src.logging import logger
from dataclasses import dataclass

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer



class ColumnImputation:

    def missing_value_imputer(self):
        """Return a ColumnTransformer that imputes missing values per-column.

        Uses ColumnTransformer because imputers target specific columns.
        """
        try:
            transformers = [
                ("age_imputer", SimpleImputer(strategy="mean"), ["Age"]),
                ("embarked_imputer", SimpleImputer(strategy="most_frequent"), ["Embarked"]),
                (
                    "cabin_imputer",
                    SimpleImputer(strategy="constant", fill_value="unknown"),
                    ["Cabin"],
                ),
            ]

            col_transformer = ColumnTransformer(transformers=transformers, remainder="passthrough")
            return col_transformer
        except Exception as e:
            raise CustomException(e, sys)

    def preprocessing(self):
        """Return a full preprocessor ColumnTransformer.

        This composes numeric and categorical pipelines. Adjust column lists as needed.
        """
        try:
            # columns to treat as categorical / numeric - adjust if your dataset differs
            categorical_cols = ["Compartment", "Family", "Embarked", "Sex"]
            numeric_cols = ["Age"]

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="mean")),
                ("scaler", StandardScaler())
            ])

            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ])

            preprocessor = ColumnTransformer(transformers=[
                ("num", num_pipeline, numeric_cols),
                ("cat", cat_pipeline, categorical_cols),
            ], remainder="passthrough")

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)