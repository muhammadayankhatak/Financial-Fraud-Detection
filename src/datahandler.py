

import pandas as pd


class DataHandler:

    def __init__(self):
        self.Data = "Data/Synthetic_Financial_datasets_log.csv"

    

    def clean_data(self):

        df = pd.read_csv(self.Data)
    

        print(f"First 30 Rows of Data: \n{df.head(30)}", end='\n\n')

        print(f"Null Values: {df.isnull().sum()}", end='\n\n')

        print(f"Duplicate Rows: {df.duplicated()}", end='\n\n')