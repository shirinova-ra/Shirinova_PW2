import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_data(num_points=100):
    """Генерирует случайные данные для DataFrame."""
    x = np.linspace(0, 10, num_points)
    y = np.sin(x) + np.random.normal(0, 0.1, num_points)  # Синусоида с шумом
    return pd.DataFrame({'x': x, 'y': y})

def plot_data(df):
    """Строит график для данных из DataFrame."""
    plt.figure(figsize=(10, 5))
    plt.plot(df['x'], df['y'], label='Синус с шумом')
    plt.title('График синусоиды с шумом')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    data = generate_data()
    plot_data(data)
