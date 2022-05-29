import numpy as np
from dataclasses import dataclass


@dataclass
class Signal:
    amplitude_arr: np.ndarray
    time_arr: np.ndarray


@dataclass
class SignalSpectrum:
    amplitude_arr: np.ndarray
    freq_arr: np.ndarray
