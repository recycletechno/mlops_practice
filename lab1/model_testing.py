import numpy as np
import pickle

# Загрузка предобработанных данных из файла
test_data = np.load("test/test_data_preprocessed.npy")
test_labels = np.random.randint(2, size=len(test_data))  # Пример меток классов

# Загрузка модели из файла
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Оценка модели на тестовых данных
accuracy = model.score(test_data, test_labels)
print("Model test accuracy is:", accuracy)
