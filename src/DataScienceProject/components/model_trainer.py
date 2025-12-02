import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
    )

from sklearn. linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn. neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.logger import logging


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')
class ModelTrainer:
    def __init__ (self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train = train_array[:,:-1], train_array[:,-1]
            X_test, y_test = test_array[:,:-1], test_array[:,-1]

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbours Regressor": KNeighborsRegressor(),
                "XGB Regressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report: dict = {}

            for i in range(len(models)):
                model = list(models.values())[i]
                model.fit(X_train, y_train)

                y_train_pred = model.predict(X_train)

                y_test_pred = model.predict(X_test)

                train_model_score = r2_score(y_train, y_train_pred)

                test_model_score = r2_score(y_test, y_test_pred)

                model_report[list(models.keys())[i]] = test_model_score

            # To get the best model score from dict
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model found: {best_model_name} with r2 score: {best_model_score}")

            # Saving the best model
            from src.DataScienceProject.utils import save_object

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Use best_model for predictions
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square

        except Exception as e:
            raise CustomException(e, sys)