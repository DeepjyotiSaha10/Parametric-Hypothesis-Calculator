# test_anova_one_way.py
from scipy import stats

ALPHA = 0.05

def run_one_way_anova(*groups):
    """
    Performs One-Way Analysis of Variance (ANOVA) on 3 or more independent groups.
    
    H0: mu1 = mu2 = mu3 (All population means are equal)
    H1: At least one population mean is significantly different
    """
    clean_groups = [g.dropna() for g in groups]
    
    # Calculate F-statistic and p-value
    f_stat, p_val = stats.f_oneway(*clean_groups)
    
    decision = (
        "Reject H0 (At least one group mean is significantly different)"
        if p_val < ALPHA
        else "Fail to Reject H0 (No significant difference among group means)"
    )
    
    return {
        "test_name": "One-Way ANOVA",
        "num_groups": len(clean_groups),
        "f_statistic": f_stat,
        "p_value": p_val,
        "decision": decision
    }