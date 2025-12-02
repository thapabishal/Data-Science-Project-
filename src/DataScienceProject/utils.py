import os
import sys
from src.DataScienceProject.exception import CustomException
from src.DataScienceProject.logger import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv


import pickle
import numpy as np


# Load environment variables
load_dotenv()

dbname= os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")

def read_PostgreSQL_data():
    logging.info("Reading posgres database started")
    try:
        with psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        ) as mydb:
            logging.info(f"Connection established with Postgres: {mydb}")
            df = pd.read_sql_query("SELECT * FROM student_data", mydb)
            print(df.head())
            return df


    except Exception as ex:
        raise CustomException(ex)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)