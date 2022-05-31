import numpy as np
from numpy import pi, exp, sign, cos, sin, sqrt
from numpy.fft import fft, fftshift
from typing import Sequence
from config import SignalParams
from signal_models import Signal, SignalSpectrum


def correlation_count(code1: np.ndarray,
                      code2: np.ndarray = None) -> np.ndarray:
    if code2 is not None:
        return np.correlate(code1, code2, mode='full')
    return np.correlate(code1, code1, mode='full')


def spd_count(acf_value: np.ndarray) -> SignalSpectrum:
    """
    Данная фнкция рассчитывает СПМ от АКФ
    """
    df = SignalParams.fs/len(acf_value)
    freq_arr = np.arange(start=-SignalParams.fs/2, step=df,
                         stop=SignalParams.fs/2)
    spd = fftshift(fft(acf_value))

    return SignalSpectrum(amplitude_arr=spd, freq_arr=freq_arr)


def bpsk_modulation_complexed(code: np.ndarray) -> Signal:
    return Signal(exp(1j*SignalParams.carr_phases1) *
                  [code[i] for i in SignalParams.code_phase_indexes1],
                  SignalParams.tt)


def time_multiplexing(*signals: Sequence[np.ndarray]) -> Signal:
    code_arr = np.array([])
    tt = np.arange(
        start=0, step=1/SignalParams.fs,
        stop=len(signals)*SignalParams.dt-1/SignalParams.fs)
    car_phases = 2*pi*(SignalParams.fif +
                       SignalParams.fd_carr1)*tt + SignalParams.carr_ph1
    code_phases = (SignalParams.code_ph1 +
                   (SignalParams.fc * SignalParams.fd_code1) * tt)
    code_phase_indexes = code_phases.astype(int) % SignalParams.code_len

    for i, _ in enumerate(signals[0]):
        for signal in signals:
            code_arr = np.append(code_arr, signal[i])

    return Signal(exp(1j * car_phases) *
                  [code_arr[i] for i in code_phase_indexes], tt)


def alt_boc_multiplexing(signal1: np.ndarray, signal2: np.ndarray) -> Signal:
    # Косинусная и синусная поднесущие
    sc_cos = sign(cos(2*pi*SignalParams.f_sin*SignalParams.tt))
    sc_sin = sign(sin(2*pi*SignalParams.f_sin*SignalParams.tt))

    sc_ssb = 1/sqrt(2)*(sc_cos+1j*sc_sin)  # Однополпсная поднесущая
    # Комлексно-сопряжённая однополоссная поднесущая
    sc_ssb_conj = 1/sqrt(2)*(sc_cos-1j*sc_sin)

    signal_alt_boc = signal1*sc_ssb_conj + signal2*sc_ssb

    return Signal(signal_alt_boc, SignalParams.tt)


def spectrum_alt_boc(signal: Signal) -> SignalSpectrum:
    ydfft = fftshift(fft(signal.amplitude_arr))
    df = SignalParams.fs/len(signal.amplitude_arr)
    freq_arr = np.arange(start=-SignalParams.fs/2,
                         step=df,
                         stop=SignalParams.fs/2)
    return SignalSpectrum(ydfft, freq_arr)
