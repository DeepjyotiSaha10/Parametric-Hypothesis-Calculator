# app_corr.py
from dataset_corr import get_correlation_dataset
from test_corr import run_pearson_correlation

def main():
    print("=" * 65)
    print("PEARSON CORRELATION (PARAMETRIC) TEST PIPELINE")
    print("=" * 65)
    
    # 1. Load Generated Dataset
    df = get_correlation_dataset(seed=42, n_samples=50)
    
    print("\nDataset Summary Preview:")
    print(df.head(4))
    print("-" * 65)
    
    # 2. Run Pearson Correlation Test
    res = run_pearson_correlation(df["Study_Hours"], df["Exam_Score"])
    
    # 3. Display Results
    print(f"\nTest Execution: {res['test_name']}")
    print(f"  Pearson Correlation (r) : {res['correlation_r']:.4f}")
    print(f"  Relationship Strength   : {res['strength']}")
    print(f"  P-Value                 : {res['p_value']:.4e}")
    print(f"  Decision (Alpha = 0.05) : {res['decision']}")
    print("=" * 65)

if __name__ == "__main__":
    main()