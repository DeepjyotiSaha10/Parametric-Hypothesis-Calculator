# test_corr.py
from scipy import stats

ALPHA = 0.05

def run_pearson_correlation(x, y):
    """
    Performs Pearson Product-Moment Correlation Test (Parametric).
    
    H0: No linear relationship exists between variables (r = 0).
    H1: A significant linear relationship exists (r != 0).
    """
    clean_x = x.dropna()
    clean_y = y.dropna()
    
    # Calculate Pearson r and p-value
    r_stat, p_val = stats.pearsonr(clean_x, clean_y)
    
    # Determine strength category
    abs_r = abs(r_stat)
    if abs_r >= 0.7:
        strength = "Strong"
    elif abs_r >= 0.4:
        strength = "Moderate"
    else:
        strength = "Weak"
        
    direction = "Positive" if r_stat > 0 else "Negative"
    
    decision = "Reject H0 (Statistically Significant Correlation)" if p_val < ALPHA else "Fail to Reject H0"
    
    return {
        "test_name": "Pearson Correlation Test",
        "correlation_r": r_stat,
        "strength": f"{strength} {direction}",
        "p_value": p_val,
        "decision": decision
    }