import numpy as np
from matplotlib import pyplot as plt
from typing import Iterable
from config import SignalParams


def primary_code_plot(code: np.ndarray) -> None:
    expans = 5
    plot_code = code.copy()
    t_arr = np.arange(start=0,
                      step=(SignalParams.t_pc/len(plot_code)/expans),
                      stop=SignalParams.t_pc)
    plt.plot(t_arr, np.repeat(plot_code, expans))
    plt.xlim((0, 0.003))
    plt.title('График дальномерного кода № 10')
    plt.show()


def correlation_plot(cor_val: np.ndarray, name: str = None) -> None:
    x_range = np.arange(start=-len(cor_val)/2,
                        step=1, stop=len(cor_val)/2)
    plt.plot(x_range, cor_val)
    plt.xlim((-200, 200))
    if name:
        plt.title(name)
    plt.show()


def spd_plot(spm: np.ndarray, freq: np.ndarray, name: str = None) -> None:
    plt.plot(freq, spm)
    if name:
        plt.title(name)
    plt.xlabel('Frequancy, Hz')
    plt.ylabel('SPD')
    plt.show()


def complexed_bpsk_plot(bpsk_signal: np.ndarray, t_arr: np.ndarray) -> None:
    plt.plot(t_arr, bpsk_signal)
    plt.xlim((1.5e-6, 3e-6))
    plt.title('BPSK сигнал, полученный через exp')
    plt.show()


def multiplexed_signals_plot(*signals: Iterable[np.ndarray],
                             time_arr: np.ndarray = None) -> None:
    if time_arr is None:
        time_arr = SignalParams.tt
    for signal in signals:
        plt.plot(time_arr, signal)
    plt.xlim((1.5e-6, 3e-6))
    plt.show()


def spectrum_plot(spectrum: np.ndarray, freq: np.ndarray,
                  name: str = None) -> None:
    plt.plot(freq, np.abs(spectrum))
    if name:
        plt.title(name)
    plt.xlabel('Frequancy, Hz')
    plt.ylabel('Spectrum')
    plt.xlim((0, 0.1e9))
    plt.ylim(0, 30e3)
    plt.show()
