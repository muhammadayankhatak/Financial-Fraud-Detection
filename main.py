
from src.datahandler import DataHandler

print("\n\nHelllo World\n\n")

Data_Set = "data/Synthetic_Financial_datasets_log.csv"

handler = DataHandler(Data_Set)


handler.inspect_data()

data = handler.load_data()

print(f"\n\n First 50 Data: \n {data.head(50)}", end='\n\n')