# test_ancova_one_factor.py
import statsmodels.api as sm
from statsmodels.formula.api import ols

ALPHA = 0.05

def run_one_factor_ancova(df, outcome_col, factor_col, covariate_col):
    """
    Performs One-Factor ANCOVA.
    
    Formula: Outcome ~ Covariate + Categorical_Factor
    Evaluates main treatment effect adjusted for baseline covariate.
    """
    formula = f"{outcome_col} ~ {covariate_col} + C({factor_col})"
    
    # Fit OLS model
    model = ols(formula, data=df).fit()
    
    # Compute Type II Sum of Squares ANOVA table
    ancova_table = sm.stats.anova_lm(model, typ=2)
    
    # Extract p-values
    p_covariate = ancova_table.loc[covariate_col, "PR(>F)"]
    p_factor = ancova_table.loc[f"C({factor_col})", "PR(>F)"]
    
    decisions = {
        f"Covariate Effect ({covariate_col})": "Statistically Significant" if p_covariate < ALPHA else "Not Significant",
        f"Main Factor Effect ({factor_col})": "Statistically Significant" if p_factor < ALPHA else "Not Significant"
    }
    
    return {
        "test_name": "One-Factor ANCOVA",
        "ancova_table": ancova_table,
        "p_covariate": p_covariate,
        "p_factor": p_factor,
        "decisions": decisions,
        "model_summary": model
    }