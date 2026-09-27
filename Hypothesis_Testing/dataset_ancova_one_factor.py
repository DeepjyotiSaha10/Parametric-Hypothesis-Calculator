# dataset_ancova_one_factor.py
import numpy as np
import pandas as pd

def get_ancova_dataset(seed=42, n_per_group=30):
    """
    Generates synthetic continuous data for ANCOVA:
    - Factor (Categorical): Method (Method_A, Method_B, Method_C)
    - Covariate (Continuous): Pre_Score (baseline measurement)
    - Outcome (Continuous): Post_Score (dependent variable)
    """
    np.random.seed(seed)
    
    methods = ["Method_A", "Method_B", "Method_C"]
    data = []
    
    # Treatment effects for each method
    method_effects = {"Method_A": 5.0, "Method_B": 10.0, "Method_C": 18.0}
    
    for method in methods:
        # Pre-test score (covariate)
        pre_scores = np.random.normal(loc=60.0, scale=10.0, size=n_per_group)
        
        # Post-test score depends on pre-test score + treatment effect + random noise
        post_scores = 0.7 * pre_scores + method_effects[method] + np.random.normal(loc=10.0, scale=4.0, size=n_per_group)
        
        for pre, post in zip(pre_scores, post_scores):
            data.append({
                "Method": method,
                "Pre_Score": pre,
                "Post_Score": post
            })
            
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = get_ancova_dataset()
    df.to_csv("dataset_ancova_one_factor.csv", index=False)
    print("`dataset_ancova_one_factor.py` executed successfully!")
    print("Saved 'dataset_ancova_one_factor.csv' with shape:", df.shape)