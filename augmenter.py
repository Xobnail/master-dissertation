import os
import numpy as np
import plotter
# Uchidalab
import time_series_augmentation.utils.augmentation as aug
import time_series_augmentation.utils.helper as helper

def augment(dataFolder, pngFolder, jitterSigma, scalingSigma, warpingSigma, warpingKnot, show=False, experiment=0):
    """
    Аугментирует временные ряды и сохраняет в файл

    Аргументы:
    dataFolder: Путь к папке для сохранения аугментированных данных
    pngFolder: Путь к папку для сохранения графиков
    jitterSigma: Гиперпараметр sigma для метода Дрожание
    scalingSigma: Гиперпараметр sigma для метода Масштабирование
    warpingSigma: Гиперпараметр sigma для метода Деформация магнитуды
    warpingKnot: Гиперпараметр knot (количество узлов) для метода Деформация магнитуды
    show: Показать график
    experiment: Номер опыта
    """

    # Валидация
    if dataFolder is None or pngFolder is None:
        print("Не указан путь к папке с данными (dataFolder или pngFolder)!")
        return

    if jitterSigma is None or scalingSigma is None or warpingSigma is None or warpingKnot is None:
        print("Не указаны гиперпараметры для аугментации!")
        return

    for fileName in os.listdir(dataFolder):
        if not fileName.startswith('aug_'):
            normFile = os.path.join(dataFolder, fileName)
            if os.path.isfile(normFile):
                # Загружаем временной ряд в одномерный массив
                X_src = np.loadtxt(normFile)

                # Создаем пустой 3D массив в формате, необходимом для работы с Uchidalab
                X = np.zeros((X_src.size, X_src.size, 1))

                # Заполняем 3D массив
                j = 0
                while j < X_src.size:
                    X[0, j, 0] = X_src[j]
                    j += 1

                # Аугментируем данные
                X_aug = aug.jitter(X, sigma=jitterSigma)
                X_aug = aug.scaling(X_aug, sigma=scalingSigma)
                X_aug = aug.magnitude_warp(X_aug, warpingSigma, warpingKnot)

                # Заполняем 1D массив для отрисовки и для корректной записи в файл
                X_result = np.zeros(X_src.size)
                i = 0
                while i < X_src.size:
                    X_result[i] = X_aug[0, i, 0]
                    i += 1

                # Сохраняем данные в файл
                with open(dataFolder + 'aug_exp' + str(experiment) + '_' + fileName, 'w') as aug_file:
                    np.savetxt(aug_file, [X_result], delimiter=' ', fmt='%01.16f')

                # Сохраняем графики в png
                plotter.save(X_result, 'aug_exp' + str(experiment) + '_' + fileName.replace('.txt', ''), pngFolder, show)
