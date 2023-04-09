import pandas as pd
import numpy as np
import statsmodels
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 965404933  # Ваш chat ID, не меняйте название переменной


def solution(x) -> bool:
    alpha = 0.06
    a,b = ztest(x, value=500, alternative='smaller')
    if b <= alpha:
        return True
    else:
        return False
