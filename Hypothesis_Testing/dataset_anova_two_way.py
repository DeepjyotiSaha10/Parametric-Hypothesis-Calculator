# dataset_anova_two_way.py
import numpy as np
import pandas as pd

def get_anova_two_way_dataset(seed=42, n_per_cell=20):
    """
    Generates synthetic continuous data affected by two factors:
    - Factor 1: Supplement_Type (Type_A vs Type_B)
    - Factor 2: Exercise_Level (Low vs High)
    """
    np.random.seed(seed)
    
    data = []
    
    # 2x2 Factorial Design setup with different baseline means
    combinations = [
        ("Type_A", "Low", 50.0, 5.0),
        ("Type_A", "High", 65.0, 5.0),
        ("Type_B", "Low", 55.0, 5.0),
        ("Type_B", "High", 80.0, 5.0)  # Strong interaction effect
    ]
    
    for supp, ex, mean, std in combinations:
        scores = np.random.normal(loc=mean, scale=std, size=n_per_cell)
        for val in scores:
            data.append({
                "Supplement_Type": supp,
                "Exercise_Level": ex,
                "Performance_Score": val
            })
            
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = get_anova_two_way_dataset()
    df.to_csv("dataset_anova_two_way.csv", index=False)
    print("`dataset_anova_two_way.py` executed successfully!")
    print("Saved 'dataset_anova_two_way.csv' with shape:", df.shape)