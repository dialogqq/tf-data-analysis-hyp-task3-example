import pandas as pd
import numpy as np
import scipy.stats as sps

chat_id = 991556115 # Ваш chat ID, не меняйте название переменной

def solution(control_sample: pd.Series, test_sample: pd.Series) -> bool:
    t_stat, p_value = stats.ttest_ind(control_sample, test_sample, equal_var=False)
    ans = False
    alpha = 0.06
    if p_value < alpha:
        ans = True
    
    return ans
