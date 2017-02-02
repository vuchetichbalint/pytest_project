import pytest
import numpy as np
import pandas as pd

from datascience_sum import np_summa, pd_summa

@pytest.mark.parametrize("array,expected", [
    (np.array([1,2,3]), 6),
    (np.array([10,-1,2]), 11),
    (np.array([4,0,-1.2]), 2.8),
])
def test_np_summa(array, expected):
    assert np_summa(array) == expected

@pytest.mark.parametrize("serie,expected", [
    (pd.Series([1,2,3]), 6),
    (pd.Series([10,-1,2]), 11),
    (pd.Series([4,0,-1.2]), 2.8),
])
def test_pd_summa(serie, expected):
    assert np_summa(serie) == expected