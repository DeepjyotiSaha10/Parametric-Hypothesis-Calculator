# dataset_F_test.py
import numpy as np
import pandas as pd

def get_f_test_dataset(seed=42, n1=30, n2=35):
    """
    Generates synthetic data from two normal populations with known variances
    to evaluate the F-Test for Equality of Variances.
    """
    np.random.seed(seed)
    
    # Population 1: Mean = 100, Std Dev = 12 (Variance = 144)
    group_1 = np.random.normal(loc=100.0, scale=12.0, size=n1)
    
    # Population 2: Mean = 102, Std Dev = 18 (Variance = 324) - Notice higher variance
    group_2 = np.random.normal(loc=102.0, scale=18.0, size=n2)
    
    # Equalize lengths with NaN for clean DataFrame storage
    max_len = max(n1, n2)
    g1_padded = np.pad(group_1.astype(float), (0, max_len - n1), constant_values=np.nan)
    g2_padded = np.pad(group_2.astype(float), (0, max_len - n2), constant_values=np.nan)
    
    df = pd.DataFrame({
        "Group_A_Machine1": g1_padded,
        "Group_B_Machine2": g2_padded
    })
    
    return df

if __name__ == "__main__":
    df = get_f_test_dataset()
    df.to_csv("dataset_F_test.csv", index=False)
    print("dataset_F_test.py executed successfully!")
    print("Saved 'dataset_F_test.csv' with shape:", df.shape)