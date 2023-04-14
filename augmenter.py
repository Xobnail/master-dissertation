import os
import numpy as np
import plotter
# Uchidalab
import time_series_augmentation.utils.augmentation as aug
import time_series_augmentation.utils.helper as helper

def augment(dataFolder, pngFolder, jitterSigma, scalingSigma):
    """
    Аугментирует временные ряды и сохраняет в файл

    Аргументы:
    dataFolder: Путь к папке для сохранения аугментированных данных
    pngFolder: Путь к папку для сохранения графиков
    jitterSigma: Гиперпараметр sigma для метода Дрожание
    scalingSigma: Гиперпараметр sigma для метода Масштабирование
    """

    # валидация
    if (dataFolder is None or pngFolder is None):
        print("Не указан путь к папке с данными (dataFolder или pngFolder)")
        return

    if (jitterSigma is None or scalingSigma is None):
        print("Не указаны гиперпараметры для аугментации")
        return

    for fileName in os.listdir(dataFolder):
        if not fileName.startswith('aug_'):
            normFile = os.path.join(dataFolder, fileName)
            if os.path.isfile(normFile):
                # загружаем временной ряд в одномерный массив
                X_src = np.loadtxt(normFile)

                # создаем пустой 3D массив в формате, необходимом для работы с Uchidalab
                X = np.zeros((X_src.size, X_src.size, 1))

                # заполняем 3D массив
                j = 0
                while j < X_src.size:
                    X[0, j, 0] = X_src[j]
                    j += 1

                # аугментируем данные
                X_aug_jitter = aug.jitter(X, sigma=jitterSigma)
                X_aug_scale = aug.scaling(X_aug_jitter, sigma=scalingSigma)

                # заполняем 1D массив для отрисовки и для корректной записи в файл
                X_result = np.zeros(X_src.size)
                i = 0
                while i < X_src.size:
                    X_result[i] = X_aug_scale[0, i, 0]
                    i += 1

                # сохраняем данные в файл
                with open(dataFolder + 'aug_' + fileName, 'w') as aug_file:
                    np.savetxt(aug_file, [X_result],
                               delimiter=' ', fmt='%01.16f')

                # сохраняем графики в png
                plotter.save(X_result, 'aug_' + fileName.replace('.txt',''), pngFolder)