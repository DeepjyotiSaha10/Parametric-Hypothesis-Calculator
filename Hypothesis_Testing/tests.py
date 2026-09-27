# tests.py
from scipy import stats
from statsmodels.stats.weightstats import ztest

ALPHA = 0.05

def run_one_sample_ztest(data, pop_mean):
    z_stat, p_val = ztest(data, value=pop_mean)
    decision = "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    return {
        "test_name": "One-Sample Z-Test",
        "sample_mean": data.mean(),
        "hypothesized_mean": pop_mean,
        "statistic": z_stat,
        "p_value": p_val,
        "decision": decision
    }

def run_one_sample_ttest(data, pop_mean):
    t_stat, p_val = stats.ttest_1samp(data, popmean=pop_mean)
    decision = "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    return {
        "test_name": "One-Sample T-Test",
        "sample_mean": data.mean(),
        "hypothesized_mean": pop_mean,
        "statistic": t_stat,
        "p_value": p_val,
        "decision": decision
    }

def run_two_sample_ttest(group_a, group_b):
    t_stat, p_val = stats.ttest_ind(group_a, group_b)
    decision = "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    return {
        "test_name": "Two-Sample Independent T-Test",
        "group_a_mean": group_a.mean(),
        "group_b_mean": group_b.mean(),
        "statistic": t_stat,
        "p_value": p_val,
        "decision": decision
    }

def run_paired_ttest(pre_data, post_data):
    t_stat, p_val = stats.ttest_rel(pre_data, post_data)
    decision = "Reject H0" if p_val < ALPHA else "Fail to Reject H0"
    return {
        "test_name": "Paired Sample T-Test",
        "pre_mean": pre_data.mean(),
        "post_mean": post_data.mean(),
        "mean_diff": (pre_data - post_data).mean(),
        "statistic": t_stat,
        "p_value": p_val,
        "decision": decision
    }