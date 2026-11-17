
import os
import matplotlib.pylab as plt
import pandas as pd



class DataVisualizer:
    
    def __init__(self, output_dir="reports"):
        """
        Constructor for Data Visualizer Class. 
        Intiallizes the Directry.
        """

        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    


    def plot_class_distribution(self, df):
        """
        Function for Ploting the Fraud and not Fraud in Bar Chart.
        """

        if df is None and df.empty:
            print(" No Data Available for Visualization.")
            return
        
        counts = df['isFraud'].value_counts().sort_index()

        plt.figure(figsize=(8, 5))

        plt.bar(['Non-Fraud','Fraud'], [counts.get(0, 0), counts.get(1, 0)], color=["green", "red"])

        plt.title("Fraud vs Non Fraud Transactions")
        plt.xlabel("Transaction Class")
        plt.ylabel("Number of transactions")

        plt.show()

    


def visualize_all(self, df):
    self.plot_class_distribution(df)