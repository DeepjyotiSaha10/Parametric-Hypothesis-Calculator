# app_F_test.py
from dataset_F_test import get_f_test_dataset
from test_F_test import run_f_test_variances

def main():
    print("=" * 65)
    print("F-TEST FOR EQUALITY OF VARIANCES PIPELINE")
    print("=" * 65)
    
    # Load generated dataset
    df = get_f_test_dataset(seed=42, n1=30, n2=35)
    
    print("\nDataset Summary Preview:")
    print(df.dropna().head(3))
    print("-" * 65)
    
    # Run F-Test
    res = run_f_test_variances(df["Group_A_Machine1"], df["Group_B_Machine2"])
    
    # Print Results
    print(f"\nTest Execution: {res['test_name']}")
    print(f"  Group A Variance (s1^2) : {res['var_a']:.4f}")
    print(f"  Group B Variance (s2^2) : {res['var_b']:.4f}")
    print(f"  F-Statistic Ratio       : {res['f_statistic']:.4f}")
    print(f"  Degrees of Freedom      : df1 = {res['df1']}, df2 = {res['df2']}")
    print(f"  P-Value                 : {res['p_value']:.4f}")
    print(f"  Decision (Alpha = 0.05) : {res['decision']}")
    print("=" * 65)

if __name__ == "__main__":
    main()