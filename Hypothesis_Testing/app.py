# app.py
from dataset import get_fixed_dataset
import tests

# Generate and fix the dataset
df = get_fixed_dataset(seed=123, n_samples=30)

print("=" * 60)
print("PARAMETRIC HYPOTHESIS TESTING PIPELINE")
print("=" * 60)

print("\nDataset Summary Preview:")
print(df.head(3))
print("-" * 60)

# 1. One-Sample Z-Test
res_z = tests.run_one_sample_ztest(df["Sample_Group"], pop_mean=100)
print(f"\n[1] {res_z['test_name']}")
print(f"Sample Mean: {res_z['sample_mean']:.2f} | Benchmark: {res_z['hypothesized_mean']}")
print(f"Z-Stat: {res_z['statistic']:.4f} | P-Val: {res_z['p_value']:.4f}")
print(f"Decision: {res_z['decision']}")

# 2. One-Sample T-Test
res_t1 = tests.run_one_sample_ttest(df["Sample_Group"], pop_mean=100)
print(f"\n[2] {res_t1['test_name']}")
print(f"Sample Mean: {res_t1['sample_mean']:.2f} | Benchmark: {res_t1['hypothesized_mean']}")
print(f"T-Stat: {res_t1['statistic']:.4f} | P-Val: {res_t1['p_value']:.4f}")
print(f"Decision: {res_t1['decision']}")

# 3. Two-Sample Independent T-Test
res_t2 = tests.run_two_sample_ttest(df["Control_Group"], df["Treatment_Group"])
print(f"\n[3] {res_t2['test_name']}")
print(f"Control Mean: {res_t2['group_a_mean']:.2f} | Treatment Mean: {res_t2['group_b_mean']:.2f}")
print(f"T-Stat: {res_t2['statistic']:.4f} | P-Val: {res_t2['p_value']:.4f}")
print(f"Decision: {res_t2['decision']}")

# 4. Paired Sample T-Test
res_paired = tests.run_paired_ttest(df["Pre_Intervention"], df["Post_Intervention"])
print(f"\n[4] {res_paired['test_name']}")
print(f"Pre-Mean: {res_paired['pre_mean']:.2f} | Post-Mean: {res_paired['post_mean']:.2f}")
print(f"Mean Diff: {res_paired['mean_diff']:.2f}")
print(f"T-Stat: {res_paired['statistic']:.4f} | P-Val: {res_paired['p_value']:.4f}")
print(f"Decision: {res_paired['decision']}")