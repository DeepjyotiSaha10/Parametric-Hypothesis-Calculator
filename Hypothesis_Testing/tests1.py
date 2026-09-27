# tests1.py
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.contingency_tables import mcnemar

ALPHA = 0.05

def run_one_sample_prop_ztest(success_series, target_prop):
    """1-Sample Z-Test for Proportions against a known benchmark."""
    clean_series = success_series.dropna()
    count = int(clean_series.sum())
    nobs = len(clean_series)
    
    z_stat, p_val = proportions_ztest(count, nobs, value=target_prop)
    observed_prop = count / nobs
    
    return {
        "test_name": "1-Sample Proportion Z-Test",
        "observed_prop": observed_prop,
        "target_prop": target_prop,
        "statistic": z_stat,
        "p_value": p_val,
        "decision": "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    }

def run_two_sample_prop_ztest(group_a, group_b):
    """2-Sample Z-Test for Independent Proportions (A/B Testing)."""
    clean_a = group_a.dropna()
    clean_b = group_b.dropna()
    
    count = [int(clean_a.sum()), int(clean_b.sum())]
    nobs = [len(clean_a), len(clean_b)]
    
    z_stat, p_val = proportions_ztest(count, nobs)
    
    return {
        "test_name": "2-Sample Independent Proportion Z-Test",
        "prop_a": count[0] / nobs[0],
        "prop_b": count[1] / nobs[1],
        "statistic": z_stat,
        "p_value": p_val,
        "decision": "Reject H0 (Significantly Different)" if p_val < ALPHA else "Fail to Reject H0"
    }

def run_fishers_exact_test(group_a, group_b):
    """Fisher's Exact Test for small sample sizes."""
    clean_a = group_a.dropna()
    clean_b = group_b.dropna()
    
    a_success, a_fail = int(clean_a.sum()), int(len(clean_a) - clean_a.sum())
    b_success, b_fail = int(clean_b.sum()), int(len(clean_b) - clean_b.sum())
    
    contingency_table = [[a_success, a_fail], [b_success, b_fail]]
    odds_ratio, p_val = stats.fisher_exact(contingency_table)
    
    return {
        "test_name": "Fisher's Exact Test (Small Samples)",
        "odds_ratio": odds_ratio,
        "p_value": p_val,
        "decision": "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    }

def run_mcnemar_test(pre_series, post_series):
    """McNemar's Test for Paired Binary Outcomes (Before vs After)."""
    clean_df = pd.DataFrame({"pre": pre_series, "post": post_series}).dropna()
    contingency_table = pd.crosstab(clean_df["pre"], clean_df["post"])
    
    result = mcnemar(contingency_table, exact=False, correction=True)
    
    return {
        "test_name": "McNemar's Paired Proportion Test",
        "statistic": result.statistic,
        "p_value": result.pvalue,
        "decision": "Reject H0 (Significant Change)" if result.pvalue < ALPHA else "Fail to Reject H0"
    }