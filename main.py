
from src.datahandler import DataHandler

print("\n\nHelllo World\n\n")

Data_Set = "data/Synthetic_Financial_datasets_log.csv"

handler = DataHandler(Data_Set)


data = handler.inspect_data()

print(f"\n\n First 50 Data: \n {Data_Set.head(50)}", end='\n\n')