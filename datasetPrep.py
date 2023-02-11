# %%
import os
import numpy as np
import time_series_augmentation.utils.augmentation as aug
# from tsaug import Drift, AddNoise
from tsaug.visualization import plot

normFolder = '../Src/Норма/onlyTxt/'
deviationFolder = '../Src/Отклонение/onlyTxt/'

# noiseAugmenter = AddNoise(0.015, 0.025)

# %%
i = 0
for fileName in os.listdir(normFolder):
    if not fileName.startswith('aug_'):
        normFile = os.path.join(normFolder, fileName)

        if os.path.isfile(normFile):
            X = np.loadtxt(normFile)
            X_aug_jitter = aug.jitter(X, sigma=0.005)
            X_aug_warp = aug.magnitude_warp(X_aug_jitter)

            with open(normFolder + 'aug_' + fileName, 'w') as aug_file:
                np.savetxt(aug_file, [X_aug_warp], delimiter=' ', fmt='%01.16f')

            if i < 2:
                print(normFile)
                print("Before:")
                plot(X)
                print("After:")
                plot(X_aug_warp)

            # if i < 25:
            #     print(X.size, X_aug.size)

        i += 1

# # %%
# directory = '../Src/Норма/onlyTxt/'

# X1 = np.loadtxt(directory + "20210917-181304_0.txt")

# i = 0
# while i < 5:
#     X1[i] = np.nan
#     i += 1

# X_aug_test = aug.jitter(X1, sigma=0.005)
# print(X_aug_test)
# plot(X1)
# plot(X_aug_test)
# %%
