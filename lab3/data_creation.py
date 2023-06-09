import numpy as np
import os

# Создание папок "train" и "test", если они еще не существуют
os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

# Создание набора данных
data = np.random.randn(1000, 2)  # Пример случайных данных

# Добавление аномалий или шума к данным если нужно
# ...

# Разделение данных на обучающую и тестовую выборки
train_data = data[:800]
test_data = data[800:]

# Сохранение данных в папках "train" и "test"
np.save("train/train_data.npy", train_data)
np.save("test/test_data.npy", test_data)