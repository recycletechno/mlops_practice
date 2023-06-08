import numpy as np
from sklearn.preprocessing import StandardScaler

# Загрузка данных из файла
train_data = np.load("train/train_data.npy")
test_data = np.load("test/test_data.npy")

# Предобработка данных с использованием StandardScaler
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# Сохранение предобработанных данных
np.save("train/train_data_preprocessed.npy", train_data)
np.save("test/test_data_preprocessed.npy", test_data)
