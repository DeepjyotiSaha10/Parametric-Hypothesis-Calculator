# app1.py
from dataset1 import get_proportion_dataset
import tests1

def main():
    print("=" * 65)
    print("PROPORTION HYPOTHESIS TESTING SUITE")
    print("=" * 65)
    
    # 1. Load Fixed Dataset
    df = get_proportion_dataset(seed=42, n_samples=60)
    
    # 2. Run Tests
    # Test A: 1-Sample Proportion Z-Test (Target benchmark = 15%)
    res_1prop = tests1.run_one_sample_prop_ztest(df["Single_Group_Clicks"], target_prop=0.15)
    
    # Test B: 2-Sample Proportion Z-Test (Variant A vs Variant B)
    res_2prop = tests1.run_two_sample_prop_ztest(df["Variant_A_Conversions"], df["Variant_B_Conversions"])
    
    # Test C: Fisher's Exact Test (Small sample sizes)
    res_fisher = tests1.run_fishers_exact_test(df["Small_Group_1"], df["Small_Group_2"])
    
    # Test D: McNemar's Test (Pre-Campaign vs Post-Campaign Interest)
    res_mcnemar = tests1.run_mcnemar_test(df["Pre_Campaign_Interest"], df["Post_Campaign_Interest"])
    
    # 3. Print Results
    # --- 1-Sample Z-Test ---
    print(f"\n[1] {res_1prop['test_name']}")
    print(f"    Observed Proportion : {res_1prop['observed_prop']:.2%} (Target: {res_1prop['target_prop']:.2%})")
    print(f"    Z-Statistic         : {res_1prop['statistic']:.4f}")
    print(f"    P-Value             : {res_1prop['p_value']:.4f}")
    print(f"    Decision            : {res_1prop['decision']}")
    print("-" * 65)
    
    # --- 2-Sample Z-Test ---
    print(f"\n[2] {res_2prop['test_name']}")
    print(f"    Variant A Conversion: {res_2prop['prop_a']:.2%}")
    print(f"    Variant B Conversion: {res_2prop['prop_b']:.2%}")
    print(f"    Z-Statistic         : {res_2prop['statistic']:.4f}")
    print(f"    P-Value             : {res_2prop['p_value']:.4f}")
    print(f"    Decision            : {res_2prop['decision']}")
    print("-" * 65)
    
    # --- Fisher's Exact Test ---
    print(f"\n[3] {res_fisher['test_name']}")
    print(f"    Odds Ratio          : {res_fisher['odds_ratio']:.4f}")
    print(f"    P-Value             : {res_fisher['p_value']:.4f}")
    print(f"    Decision            : {res_fisher['decision']}")
    print("-" * 65)
    
    # --- McNemar's Test ---
    print(f"\n[4] {res_mcnemar['test_name']}")
    print(f"    Chi2-Statistic      : {res_mcnemar['statistic']:.4f}")
    print(f"    P-Value             : {res_mcnemar['p_value']:.4f}")
    print(f"    Decision            : {res_mcnemar['decision']}")
    print("=" * 65)

if __name__ == "__main__":
    main()