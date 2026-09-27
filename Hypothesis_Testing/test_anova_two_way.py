# test_anova_two_way.py
import statsmodels.api as sm
from statsmodels.formula.api import ols

ALPHA = 0.05

def run_two_way_anova(df, response_col, factor1_col, factor2_col):
    """
    Performs Two-Way ANOVA including Main Effects and Interaction Effect.
    
    Formula: Response ~ C(Factor1) + C(Factor2) + C(Factor1):C(Factor2)
    """
    formula = f"{response_col} ~ C({factor1_col}) + C({factor2_col}) + C({factor1_col}):C({factor2_col})"
    
    model = ols(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    
    # Extract p-values
    p_f1 = anova_table.loc[f"C({factor1_col})", "PR(>F)"]
    p_f2 = anova_table.loc[f"C({factor2_col})", "PR(>F)"]
    p_inter = anova_table.loc[f"C({factor1_col}):C({factor2_col})", "PR(>F)"]
    
    decisions = {
        f"Main Effect ({factor1_col})": "Significant" if p_f1 < ALPHA else "Not Significant",
        f"Main Effect ({factor2_col})": "Significant" if p_f2 < ALPHA else "Not Significant",
        "Interaction Effect": "Significant" if p_inter < ALPHA else "Not Significant"
    }
    
    return {
        "test_name": "Two-Way ANOVA",
        "anova_table": anova_table,
        "p_val_factor1": p_f1,
        "p_val_factor2": p_f2,
        "p_val_interaction": p_inter,
        "decisions": decisions
    }