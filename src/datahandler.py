

import pandas as pd


class DataHandler:

    def __init__(self, data_path):
        self.data_path = data_path

    

    def load_data(self):

        if not self.data_path:
            return None
        
        df = pd.read_csv(self.data_path)

        if df.empty:
            return None

        print("Successfull")

        return df
    


    def inspect_data(self):

        df = self.load_data()

        rows, columns = df.shape
        print(f"\n Total Rows: {rows}", end='\n')
        print(f"Total Columns: {columns}", end='\n')
        print(f"Columns Names: \n")
        for cols in df.columns:
            print(cols)
        
        print(f"\n\nNo of Missing Values: \n{df.isnull().sum()}", end='\n')
        print(f"No of Duplicate Values: {df.duplicated().sum()}", end='\n')



        