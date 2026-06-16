# analysis.py
# Author: Hellen Beatrice Apolot
# Date: 16/06/2026
# Description: Data Analysis project using pandas and matplotlib

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load CSV data into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None

def summarize_data(df):
    """
    Print summary statistics of the dataset.
    """
    print("\n--- Summary Statistics ---")
    print(df.describe())

def filter_high_scores(df, threshold=80):
    """
    Filter rows where 'Score' is greater than threshold.
    """
    filtered = df[df["Score"] > threshold]
    print(f"\n--- Students scoring above {threshold} ---")
    print(filtered)
    return filtered

def visualize_scores(df):
    """
    Create a histogram of the 'Score' column.
    """
    plt.hist(df["Score"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    file_path = "sampledata.csv"
    df = load_data(file_path)

    if df is not None:
        summarize_data(df)
        filter_high_scores(df, 80)
        visualize_scores(df)
