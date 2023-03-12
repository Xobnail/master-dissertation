# %%
import os
import numpy as np
import time_series_augmentation.utils.augmentation as aug
# from tsaug import Drift, AddNoise
from tsaug.visualization import plot

normFolder = '../Src/Норма/onlyTxt/'
deviationFolder = '../Src/Отклонение/onlyTxt/'

# %%
i = 0
for fileName in os.listdir(normFolder):
    if not fileName.startswith('aug_'):
        normFile = os.path.join(normFolder, fileName)

        if os.path.isfile(normFile):
            # загружаем временной ряд в одномерный массив
            X_src = np.loadtxt(normFile)
            # создаем пустой 3D массив в формате, необходимом для работы с Uchidalab 
            X = np.zeros((X_src.size, X_src.size, 1))

            # заполняем 3D массив
            j = 0
            while j < X_src.size:
                X[0,j,0] = X_src[j]
                j+=1

            # if i < 1:
            #     print(type(X))
            #     print(X.shape)
            #     print(X)

            # аугментируем данные
            X_aug_jitter = aug.jitter(X, sigma=0.005)
            X_aug_scale = aug.scaling(X_aug_jitter, 0.1)

            # сохарняем данные в файл
            with open(normFolder + 'aug_' + fileName, 'w') as aug_file:
                np.savetxt(aug_file, X_aug_scale[0], delimiter=' ', fmt='%01.16f')

            # заполняем 1D массив для отрисовки
            X_after = np.zeros(X_src.size)
            p = 0
            while p < X_src.size:
                X_after[p] = X_aug_scale[0,p,0]
                p+=1

            print(i)

            if i < 2:
                print(normFile)
                print("Before:")
                plot(X_src)
                print("After:")
                plot(X_after)

        i += 1

# %%
