import matplotlib.pyplot as plt
import numpy as np

# Плотность пикселей для расчета размера изображения
DPI = 100

def save(x, filename, path, ylim=(0, 1), xlabel="Frame_num", ylabel="Pupil_size"):
    """
    Сохраняет временной ряд в виде графика

    Аргументы:
    x: Временной ряд
    filename: Названия файла для сохранения
    path: Путь для сохранения
    ylim: Область значений временного ряда
    xlabel: Метка оси x
    ylabel: Метка оси y
    """

    # Устанавливаем размер графика
    plt.figure(figsize=(640/DPI, 480/DPI), dpi=DPI)
    # Устанавливаем метки осей
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # Устанавливаем область определений и область значений
    plt.xlim(-5, x.shape[0]+5)
    plt.ylim(ylim)
    # Формируем график
    steps = np.arange(x.shape[0])
    plt.plot(steps, x)
    # Сохраняем график в файл
    plt.ioff()
    if filename is not None and path is not None:
        plt.savefig(f'{path}{filename}.png', dpi=DPI)
    else:
        print("Не указан путь для сохранения графика.")
    plt.close()
    # plt.show()