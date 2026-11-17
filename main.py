
from src.datahandler import DataHandler
from src.datavisualizer import DataVisualizer

print("\n\nHelllo World\n\n")

Data_Set = "data/Synthetic_Financial_datasets_log.csv"

handler = DataHandler(Data_Set)


# handler.inspect_data()

data = handler.load_data()


obj = DataVisualizer()

obj.visualize_all(data)