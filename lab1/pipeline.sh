#!/bin/bash

# Запуск скрипта data_creation.py
python data_creation.py

# Запуск скрипта data_preprocessing.py
python data_preprocessing.py

# Запуск скрипта model_preparation.py
python model_preparation.py

# Запуск скрипта model_testing.py и вывод оценки модели
python model_testing.py
