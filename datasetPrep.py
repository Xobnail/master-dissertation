# %%
import os
import numpy as np
from tsaug import Drift, AddNoise
from tsaug.visualization import plot

normFolder = '../Src/Норма/onlyTxt/'
deviationFolder = '../Src/Отклонение/onlyTxt/'

noiseAugmenter = AddNoise(0.015, 0.025)

# TODO: check nan values in source files
# and fix formatting float numbers 

# %%
i = 0
for fileName in os.listdir(normFolder):    
    if not fileName.startswith('aug_'):
        normFile = os.path.join(normFolder, fileName)

        if os.path.isfile(normFile):     
            X = np.loadtxt(normFile)
            X_aug = noiseAugmenter.augment(X)

            with open(normFolder + 'aug_' + fileName, 'w') as aug_file:
                np.savetxt(aug_file, [X_aug], delimiter=' ')

            if i < 2:
                print(normFile)
                print("Before:")
                plot(X)
                print("After:")
                plot(X_aug)  
            
            if i < 25:
                print(X.size, X_aug.size)

        i += 1

# %%

directory = '../Src/Норма/onlyTxt/'

X1 = np.loadtxt(directory + "20210917-143238_0.txt")
X2 = np.loadtxt(directory + "20210917-143238_1.txt")
print("Before:")
plot(X1)
plot(X2)
# %%
driftAugmenter = AddNoise(0.015, 0.025)
X1_aug = driftAugmenter.augment(X1)
X2_aug = driftAugmenter.augment(X2)
print("After:")
plot(X1_aug)
plot(X2_aug)
# %%
Drift(max_drift=0.3, n_drift_points=3)
AddNoise(0.015, 0.025)
