

import pandas as pd


class DataHandler:

    def __init__(self, data_path):
        """ 
        Constructor of the DataHandler Class. Save Data Set path Data. 
        """
        self.data_path = data_path

    

    def load_data(self):
        """
        Loads Data. Checks for the Data Set Path Validity and also for the Data Set not Empty. Reads the Data and
        Converts to DataFrame using Pandas.
        """
        if not self.data_path:
            return None
        
        df = pd.read_csv(self.data_path)

        if df.empty:
            return None

        print("Successfull")

        return df
    


    def inspect_data(self, df):
        """
        It Inspects Whole Data. Checks for Null Values. Duplicate Values and Also Displays No of Columns 
        and Total Rows and Columns.
        """
        # df = self.load_data()

        rows, columns = df.shape
        print(f"\n Total Rows: {rows}", end='\n')
        print(f"Total Columns: {columns}", end='\n')
        print(f"Columns Names: \n")
        for cols in df.columns:
            print(cols)
        
        print(f"\n\nNo of Missing Values: \n{df.isnull().sum()}", end='\n')
        print(f"No of Duplicate Values: {df.duplicated().sum()}", end='\n')



    def clean_data(self, df):
        """
        Cleans the Data by removing duplicate and NUll Values. Also Checks for the File Not Empty.
        Returns the Data Frame.
        """

        # df = self.load_data()


        if df is None and df.empty:
            return None


        # Inplace means do changes in same df rather than doing
        # new_df = df.dropna()
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        df.reset_index(inplace=True, drop=True)

        return df
        