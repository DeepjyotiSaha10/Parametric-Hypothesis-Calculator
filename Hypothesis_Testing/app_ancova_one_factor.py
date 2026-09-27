# app_ancova_one_factor.py
from dataset_ancova_one_factor import get_ancova_dataset
from test_ancova_one_factor import run_one_factor_ancova

def main():
    print("=" * 65)
    print("ONE-FACTOR ANCOVA HYPOTHESIS TESTING PIPELINE")
    print("=" * 65)
    
    # 1. Load Dataset
    df = get_ancova_dataset(seed=42, n_per_group=30)
    
    print("\nDataset Preview:")
    print(df.head(5))
    print("-" * 65)
    
    # 2. Compute Raw Means
    raw_means = df.groupby("Method")[["Pre_Score", "Post_Score"]].mean()
    print("\nUnadjusted Raw Group Means:")
    print(raw_means.round(2))
    print("-" * 65)
    
    # 3. Run ANCOVA Test
    res = run_one_factor_ancova(
        df, 
        outcome_col="Post_Score", 
        factor_col="Method", 
        covariate_col="Pre_Score"
    )
    
    # 4. Display Results
    print(f"\nTest Execution: {res['test_name']}\n")
    print("ANCOVA Summary Table (Type II SS):")
    print(res["ancova_table"].round(4))
    print("-" * 65)
    
    print("HYPOTHESIS DECISIONS (Alpha = 0.05):")
    for effect, decision in res["decisions"].items():
        print(f"  {effect:<32}: {decision}")
    print("=" * 65)

if __name__ == "__main__":
    main()