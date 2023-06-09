import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

# Загрузка предобработанных данных из файла
train_data = np.load("train/train_data_preprocessed.npy")
train_labels = np.random.randint(2, size=len(train_data))  # Пример меток классов

# Создание и обучение модели
model = LogisticRegression()
model.fit(train_data, train_labels)

# Сохранение модели в файл
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
