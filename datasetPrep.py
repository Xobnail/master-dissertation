# %%
import os
import numpy as np
from tsaug import Drift, AddNoise
from tsaug.visualization import plot

normPath = '../Src/Норма/onlyTxt/'
deviationPath = '../Src/Отклонение/onlyTxt/'

noiseAugmenter = AddNoise(0.015, 0.025)

i = 0
for filename in os.listdir(normPath):
    
    relativePath = os.path.join(normPath, filename)

    if os.path.isfile(relativePath):     
        X = np.loadtxt(relativePath)
        X_aug = noiseAugmenter.augment(X)

        with open(normPath + 'aug_' + filename, 'w') as aug_file:
            # !Delimeter doesnt work, try [X_aug]!!!
            np.savetxt(aug_file, X_aug, delimiter=" ")

        if (i < 2):
            print(relativePath)
            print("Before:")
            plot(X)
            print("After:")
            plot(X_aug)  

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
