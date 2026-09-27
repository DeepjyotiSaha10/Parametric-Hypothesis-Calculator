# dataset_corr.py
import numpy as np
import pandas as pd

def get_correlation_dataset(seed=42, n_samples=50):
    """
    Generates continuous, normally distributed paired variables
    specifically suited for Pearson Correlation Analysis.
    """
    np.random.seed(seed)
    
    # Feature X: Normally distributed continuous variable (e.g., Study Hours)
    x_var = np.random.normal(loc=25.0, scale=5.0, size=n_samples)
    
    # Feature Y: Normally distributed with a strong linear relationship to X (e.g., Exam Score)
    y_var = (x_var * 2.8) + np.random.normal(loc=10.0, scale=6.0, size=n_samples)
    
    df = pd.DataFrame({
        "Study_Hours": x_var,
        "Exam_Score": y_var
    })
    
    return df

if __name__ == "__main__":
    df = get_correlation_dataset()
    df.to_csv("dataset_corr.csv", index=False)
    print("`dataset_corr.py` executed successfully!")
    print("Saved 'dataset_corr.csv' with shape:", df.shape)