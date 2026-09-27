# app_anova_one_way.py
from dataset_anova_one_way import get_anova_one_way_dataset
from test_anova_one_way import run_one_way_anova

def main():
    print("=" * 65)
    print("ONE-WAY ANOVA HYPOTHESIS TESTING PIPELINE")
    print("=" * 65)
    
    # 1. Load Dataset
    df = get_anova_one_way_dataset(seed=42, n_per_group=30)
    
    print("\nDataset Preview:")
    print(df.head(3))
    print("-" * 65)
    
    # 2. Compute Group Means
    m_a = df["Method_Standard"].mean()
    m_b = df["Method_Interactive"].mean()
    m_c = df["Method_Online"].mean()
    
    print(f"Group Means -> Standard: {m_a:.2f} | Interactive: {m_b:.2f} | Online: {m_c:.2f}")
    print("-" * 65)
    
    # 3. Run One-Way ANOVA Test
    res = run_one_way_anova(
        df["Method_Standard"], 
        df["Method_Interactive"], 
        df["Method_Online"]
    )
    
    # 4. Display Results
    print(f"\nTest Execution   : {res['test_name']}")
    print(f"  Number of Groups : {res['num_groups']}")
    print(f"  F-Statistic      : {res['f_statistic']:.4f}")
    print(f"  P-Value          : {res['p_value']:.4e}")
    print(f"  Decision         : {res['decision']}")
    print("=" * 65)

if __name__ == "__main__":
    main()