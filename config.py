import numpy as np
from numpy import pi
from enum import Enum


class E6PrimaryCodes(Enum):
    __root_path: str = 'primary_codes/'
    E6_C_10_PATH = __root_path + 'E6-C_Code_No_10.txt'
    E6_C_11_PATH = __root_path + 'E6-C_Code_No_11.txt'
    E6_C_12_PATH = __root_path + 'E6-C_Code_No_12.txt'
    E6_C_13_PATH = __root_path + 'E6-C_Code_No_13.txt'


class SignalParams:
    t_pc = 100.0e-3  # Период дальномерного кода
    fs: float = 90e7  # Частота дискретизации
    fif: float = 20e6  # Промежутояная частота
    f_sin: float = 7*1.023e6  # Частота символьной последовательности
    fc: float = 5.115e6  # Тактовая частотадальномерного кода
    dt: float = 1*1.0e-3  # Шаг модели по времени
    code_len: int = 5116
    fd_carr1: float = 1.6*1.25e3  # Доплер несущей
    fd_code1: float = fd_carr1/1540  # Доплер несушей
    carr_ph1: float = 0.0  # Начальная фаза
    code_ph1: float = 5000

    # Формирование вектора отсчетов времени
    tt = np.arange(start=0, step=1/fs, stop=dt-1/fs)

    # Формировапние векторов фаз промежуточной частоты
    carr_phases1 = 2*pi*(fif+fd_carr1)*tt + carr_ph1

    # Формированеи векторов фаз кодового сигнала
    code_phases1 = code_ph1 + (fc*fd_code1)*tt
    code_phase_indexes1 = (code_phases1.astype(int) % code_len)
