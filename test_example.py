import pytest
import numpy as np
import pandas as pd
from file import generate_data

def test_generate_data():
    """Тестирует функцию генерации данных."""
    df = generate_data(num_points=100)

    # Проверяем, что возвращается DataFrame
    assert isinstance(df, pd.DataFrame), "Должен вернуть DataFrame"
    
    # Проверяем, что у DataFrame 100 строк
    assert len(df) == 100, "Количество строк должно быть 100"
    
    # Проверяем, что в DataFrame есть нужные колонки
    assert 'x' in df.columns, "Колонка 'x' должна быть в DataFrame"
    assert 'y' in df.columns, "Колонка 'y' должна быть в DataFrame"
    
    # Проверяем, что значения в колонке 'x' в правильном диапазоне
    assert (df['x'].min() >= 0) and (df['x'].max() <= 10), "Значения 'x' должны быть в диапазоне от 0 до 10"

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
