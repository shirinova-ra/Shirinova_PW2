import pytest
import numpy as np
import pandas as pd
from file import generate_data

def test_generate_data():
    df = generate_data(num_points=100)
    
    assert isinstance(df, pd.DataFrame), "Должен вернуть DataFrame"
    assert len(df) == 100, "Количество строк должно быть 100"
    assert 'x' in df.columns, "Колонка 'x' должна быть в DataFrame"
    assert 'y' in df.columns, "Колонка 'y' должна быть в DataFrame"
    assert (df['x'].min() >= 0) and (df['x'].max() <= 10), "Значения 'x' должны быть в диапазоне от 0 до 10"

if __name__ == "__main__":
    pytest.main()
