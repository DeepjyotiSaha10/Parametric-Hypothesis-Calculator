# dataset_anova_one_way.py
import numpy as np
import pandas as pd

def get_anova_one_way_dataset(seed=42, n_per_group=30):
    """
    Generates synthetic continuous data across three independent groups
    (e.g., Teaching Methods: Standard, Interactive, Online).
    """
    np.random.seed(seed)
    
    # Normally distributed scores with different group means
    method_a = np.random.normal(loc=70.0, scale=8.5, size=n_per_group)
    method_b = np.random.normal(loc=76.0, scale=8.5, size=n_per_group)
    method_c = np.random.normal(loc=82.0, scale=8.5, size=n_per_group)
    
    df = pd.DataFrame({
        "Method_Standard": method_a,
        "Method_Interactive": method_b,
        "Method_Online": method_c
    })
    
    return df

if __name__ == "__main__":
    df = get_anova_one_way_dataset()
    df.to_csv("dataset_anova_one_way.csv", index=False)
    print("`dataset_anova_one_way.py` executed successfully!")
    print("Saved 'dataset_anova_one_way.csv' with shape:", df.shape)