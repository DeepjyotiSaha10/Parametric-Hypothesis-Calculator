# dataset1.py
import numpy as np
import pandas as pd

def get_proportion_dataset(seed=42, n_samples=60):
    """
    Generates binary proportion data for 1-sample, 2-sample A/B,
    small-sample, and paired (McNemar) testing.
    """
    np.random.seed(seed)
    
    # 1. Single group binary outcome (Target benchmark = 0.15)
    single_group = np.random.binomial(n=1, p=0.25, size=n_samples)
    
    # 2. Two independent groups (A/B testing)
    variant_a = np.random.binomial(n=1, p=0.20, size=n_samples)
    variant_b = np.random.binomial(n=1, p=0.45, size=n_samples)
    
    # 3. Small samples for Fisher's Exact Test (N = 12)
    # Convert to float (.astype(float)) so np.nan can be used as padding
    small_group_1 = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)
    small_group_2 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], dtype=float)
    
    # Pad small groups with NaN to match main DataFrame length
    pad_len = n_samples - len(small_group_1)
    small_g1_padded = np.pad(small_group_1, (0, pad_len), constant_values=np.nan)
    small_g2_padded = np.pad(small_group_2, (0, pad_len), constant_values=np.nan)
    
    # 4. Paired binary outcome (Before vs After)
    pre_campaign = np.random.binomial(n=1, p=0.30, size=n_samples)
    post_campaign = np.where(
        pre_campaign == 1,
        1,
        np.random.binomial(n=1, p=0.35, size=n_samples)
    )
    
    df = pd.DataFrame({
        "Single_Group_Clicks": single_group,
        "Variant_A_Conversions": variant_a,
        "Variant_B_Conversions": variant_b,
        "Small_Group_1": small_g1_padded,
        "Small_Group_2": small_g2_padded,
        "Pre_Campaign_Interest": pre_campaign,
        "Post_Campaign_Interest": post_campaign
    })
    
    return df

if __name__ == "__main__":
    df = get_proportion_dataset()
    df.to_csv("dataset1.csv", index=False)
    print("`dataset1.py` ran successfully!")
    print("Dataset saved to `dataset1.csv` with shape:", df.shape)