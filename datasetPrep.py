# from tsaug import Drift, AddNoise
# from tsaug.visualization import plot
import augmenter

NORM_FOLDER_DATA = '../Src/Норма/onlyTxt/'
NORM_FOLDER_PNG = '../Src/Норма/onlyPng/'
DEVIATION_FOLDER_DATA = '../Src/Отклонение/onlyTxt/'
DEVIATION_FOLDER_PNG = '../Src/Отклонение/onlyPng/'
JITTER_SIGMA = 0.0015
SCALING_SIGMA = 0.1
WARPING_SIGMA = 0.03
WARPING_KNOT = 4

augmenter.augment(NORM_FOLDER_DATA, NORM_FOLDER_PNG, JITTER_SIGMA, SCALING_SIGMA, WARPING_SIGMA, WARPING_KNOT, show=False, experiment=1)
augmenter.augment(DEVIATION_FOLDER_DATA, DEVIATION_FOLDER_PNG, JITTER_SIGMA, SCALING_SIGMA, WARPING_SIGMA, WARPING_KNOT, show=False, experiment=1)

print("Done!")