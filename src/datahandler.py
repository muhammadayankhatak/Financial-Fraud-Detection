

import pandas as pd


class DataHandler:

    # def __init__(self):
    #     self.Data = "data/Synthetic_Financial_datasets_log.csv"

    

    def clean_data(self, Data):

        df = pd.read_csv(self.Data)
    
        # print(f"First 30 Rows of Data: \n{df.head(30)}", end='\n\n')
        # print(f"Null Values: {df.isnull().sum()}", end='\n\n')
        # print(f"Duplicate Rows: {df.duplicated()}", end='\n\n')

        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        df.reset_index(inplace=True, drop=True)


        return df


        