import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_visualize_data():
    # Генерация простых данных
    np.random.seed(0)  # Для повторяемости
    data = np.random.randn(100)  # 100 случайных чисел из нормального распределения

    # Создаем DataFrame с данными
    df = pd.DataFrame(data, columns=['Value'])

    # Добавляем новую колонку с накопленной суммой
    df['Cumulative Sum'] = df['Value'].cumsum()

    # Выводим основные статистики
    print("Summary statistics:")
    print(df.describe())

    # Визуализируем данные
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(df['Value'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Histogram of Values')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.plot(df['Cumulative Sum'], color='orange')
    plt.title('Cumulative Sum Over Time')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')

    plt.tight_layout()
    plt.show()

# Вызов функции
analyze_and_visualize_data()
