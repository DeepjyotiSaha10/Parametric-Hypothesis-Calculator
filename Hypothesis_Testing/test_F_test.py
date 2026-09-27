# test_F_test.py
import numpy as np
from scipy import stats

ALPHA = 0.05

def run_f_test_variances(group_a, group_b):
    """
    Performs a Two-Tailed F-Test for Equality of Variances.
    
    H0: Variance(Group A) == Variance(Group B)
    H1: Variance(Group A) != Variance(Group B)
    """
    # Drop NaNs to handle different sample sizes safely
    clean_a = group_a.dropna()
    clean_b = group_b.dropna()
    
    # Sample Variances (ddof=1 for sample variance s^2)
    var_a = np.var(clean_a, ddof=1)
    var_b = np.var(clean_b, ddof=1)
    
    # Place larger variance in numerator to keep F >= 1
    if var_a >= var_b:
        f_stat = var_a / var_b
        df1 = len(clean_a) - 1
        df2 = len(clean_b) - 1
    else:
        f_stat = var_b / var_a
        df1 = len(clean_b) - 1
        df2 = len(clean_a) - 1
        
    # Two-tailed p-value
    p_val = 2 * (1 - stats.f.cdf(f_stat, df1, df2))
    
    decision = "Reject H0 (Unequal Variances)" if p_val < ALPHA else "Fail to Reject H0 (Equal Variances)"
    
    return {
        "test_name": "F-Test for Equality of Variances",
        "var_a": var_a,
        "var_b": var_b,
        "f_statistic": f_stat,
        "df1": df1,
        "df2": df2,
        "p_value": p_val,
        "decision": decision
    }