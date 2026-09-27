# app_anova_two_way.py
from dataset_anova_two_way import get_anova_two_way_dataset
from test_anova_two_way import run_two_way_anova

def main():
    print("=" * 65)
    print("TWO-WAY ANOVA HYPOTHESIS TESTING PIPELINE")
    print("=" * 65)
    
    # 1. Load Dataset
    df = get_anova_two_way_dataset(seed=42, n_per_cell=20)
    
    print("\nDataset Sample Preview:")
    print(df.head(5))
    print("-" * 65)
    
    # 2. Group Means Summary
    means = df.groupby(["Supplement_Type", "Exercise_Level"])["Performance_Score"].mean()
    print("\nGroup Means Summary:")
    print(means)
    print("-" * 65)
    
    # 3. Run Two-Way ANOVA Test
    res = run_two_way_anova(df, "Performance_Score", "Supplement_Type", "Exercise_Level")
    
    # 4. Display Results
    print(f"\nTest Execution: {res['test_name']}\n")
    print("ANOVA Table:")
    print(res["anova_table"].round(4))
    print("-" * 65)
    
    print("HYPOTHESIS DECISIONS (Alpha = 0.05):")
    for key, decision in res["decisions"].items():
        print(f"  {key:<30}: {decision}")
    print("=" * 65)

if __name__ == "__main__":
    main()