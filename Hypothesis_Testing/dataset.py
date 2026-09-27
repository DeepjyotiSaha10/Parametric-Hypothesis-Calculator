import numpy as np
import pandas as pd

def get_fixed_dataset(seed=123, n_samples=30):
    """
    Generates and returns a reproducible, fixed pandas DataFrame.
    """
    np.random.seed(seed)
    
    data = {
        # One-sample target scenario
        "Sample_Group": np.random.normal(loc=104.5, scale=12.0, size=n_samples),
        
        # Two independent groups scenario
        "Control_Group": np.random.normal(loc=50.0, scale=8.0, size=n_samples),
        "Treatment_Group": np.random.normal(loc=56.2, scale=8.5, size=n_samples),
        
        # Paired scenario (Before vs After)
        "Pre_Intervention": np.random.normal(loc=135.0, scale=10.0, size=n_samples)
    }
    
    df = pd.DataFrame(data)
    # Dependent change for paired test
    df["Post_Intervention"] = df["Pre_Intervention"] - np.random.normal(loc=6.0, scale=4.0, size=n_samples)
    
    return df

if __name__ == "__main__":
    df = get_fixed_dataset()
    print("Dataset generated successfully!")
    print(df.head())