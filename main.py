
from src.datahandler import DataHandler
from src.datavisualizer import DataVisualizer

print("\n\nHelllo World\n\n")

Data_Set = "data/Synthetic_Financial_datasets_log.csv"

handler = DataHandler(Data_Set)


data = handler.load_data()
data = handler.clean_data(data)   # Store the returned cleaned data back into data (Variable).

obj = DataVisualizer(output_dir="reports")

obj.visualize_all(data)