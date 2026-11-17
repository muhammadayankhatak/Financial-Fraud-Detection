
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

        if df is None or df.empty:
            print(" No Data Available for Visualization.")
            return
        
        counts = df['isFraud'].value_counts().sort_index()

        plt.figure(figsize=(8, 5))

        plt.bar(['Non-Fraud','Fraud'], [counts.get(0, 0), counts.get(1, 0)], color=["green", "red"])

        plt.yscale("log")

        plt.title("Fraud vs Non Fraud Transactions")
        plt.xlabel("Transaction Class")
        plt.ylabel("Number of transactions")

        plt.savefig(os.path.join(self.output_dir, "class_distribution.png"))

        plt.show()


    
    def plot_transaction_types(self, df):
        """ Function for Ploting the Transactions Type in Bar Chart. """


        if df is None or df.empty:
            print(" No Data Available for Visualization.")
            return
        
        counts = df['type'].value_counts()

        plt.figure(figsize=(8, 5))

        plt.bar(counts.index, counts.values, color='skyblue')

        plt.title("Transaction Types Distribution")
        plt.xlabel("Transaction Types")
        plt.ylabel("Number of Transactions")


        plt.savefig(os.path.join(self.output_dir, "transactions.png"))

        plt.show()

    
    def plot_fraud_by_type(self, df):
        """
        Compares Fraud vs Non-Fraud transactions for each transaction type.
        """

        if df is None or df.empty:
            print("No Data Available for Visualization.")
            return

        counts = df.groupby(['type', 'isFraud']).size().unstack(fill_value=0)

        counts = counts.rename(columns={0: 'Non-Fraud', 1: 'Fraud'})

        counts.plot(kind='bar',figsize=(10, 6),color=['green', 'red'])

        plt.yscale("log")

        plt.title("Fraud vs Non-Fraud by Transaction Type")
        plt.xlabel("Transaction Type")
        plt.ylabel("Number of Transactions")
        plt.xticks(rotation=45)
        plt.legend(title="Transaction Class")
        plt.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "fraud_by_type.png"),dpi=300)

        plt.show()

    
    def plot_amount_distribution(self, df):
        """
        Compares transaction amount distributions for Fraud and Non-Fraud transactions.
        """

        if df is None or df.empty:
            print("No Data Available for Visualization.")
            return

        fraud = df[df['isFraud'] == 1]['amount']
        non_fraud = df[df['isFraud'] == 0]['amount']

        plt.figure(figsize=(10, 6))

        plt.hist(non_fraud, bins=50, alpha=0.6, color='green', label='Non-Fraud', density=True)

        plt.hist(fraud, bins=50, alpha=0.6, color='red', label='Fraud', density=True)

        plt.title("Transaction Amount Distribution")
        plt.xlabel("Transaction Amount")
        plt.ylabel("Density")
        plt.legend()

        plt.tight_layout()

        plt.savefig(os.path.join(self.output_dir, "amount_distribution.png"),dpi=300)

        plt.show()


    def visualize_all(self, df):
        """ Visualize all Functions 1 by 1. Calls all Function of Plotting of Data Visualizer Class. """
        # self.plot_class_distribution(df)
        # self.plot_transaction_types(df)

        # self.plot_fraud_by_type(df)

        self.plot_amount_distribution(df)