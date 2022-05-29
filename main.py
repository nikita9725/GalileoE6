import numpy as np
from config import E6PrimaryCodes, SignalParams
from signal_models import Signal
from primary_code_generator import get_primary_code_from_file
from plots import (primary_code_plot, correlation_plot, spd_plot,
                   complexed_bpsk_plot, multiplexed_signals_plot,
                   spectrum_plot)
from count_funcs import (correlation_count, spd_count, spectrum_alt_boc,
                         bpsk_modulation_complexed, time_multiplexing,
                         alt_boc_multiplexing)


# Дальномерные коды
code_10 = get_primary_code_from_file(E6PrimaryCodes.E6_C_10_PATH)
code_11 = get_primary_code_from_file(E6PrimaryCodes.E6_C_11_PATH)
code_12 = get_primary_code_from_file(E6PrimaryCodes.E6_C_12_PATH)
code_13 = get_primary_code_from_file(E6PrimaryCodes.E6_C_13_PATH)

# График кода № 10
primary_code_plot(code_10)

# График АКФ кода № 10
acf_value = correlation_count(code_10)
correlation_plot(acf_value, 'АКФ кода № 10')

# Графики ВКФ кодов
ccf_10_11_value = correlation_count(code_11, code_10)
correlation_plot(ccf_10_11_value, 'ВКФ кодов № 10 и 11')

ccf_10_12_value = correlation_count(code_11, code_12)
correlation_plot(ccf_10_12_value, 'ВКФ кодов № 10 и 12')

ccf_10_13_value = correlation_count(code_11, code_13)
correlation_plot(ccf_10_11_value, 'ВКФ кодов № 10 и 13')

# СПМ (Преобразование Фурье от АКФ)
spd = spd_count(acf_value)
spd_plot(np.absolute(spd.amplitude_arr), spd.freq_arr,
         'СПМ (Преобразование Фурье от АКФ10 кода № 10)')

# СПМ (Преобразование Фурье от АКФx10)
acf_value_copy = acf_value.copy()
spd_1 = spd_count(np.repeat(acf_value_copy, 10))
spd_plot(np.absolute(spd_1.amplitude_arr), spd_1.freq_arr,
         'СПМ (Преобразование Фурье от АКФx10 кода № 10)')

# BPSK от кода № 10
bpsk_signal_10_complexed = bpsk_modulation_complexed(code_10)
complexed_bpsk_plot(np.real(bpsk_signal_10_complexed.amplitude_arr),
                    bpsk_signal_10_complexed.time_arr)

bpsk_signal_11_complexed = bpsk_modulation_complexed(code_11)

# Простое уплотнение сигналов
bpsk_10_11_simple_multiplexed = Signal(
    (bpsk_signal_10_complexed.amplitude_arr +
     bpsk_signal_11_complexed.amplitude_arr), SignalParams.tt)

multiplexed_signals_plot(
    np.real(bpsk_10_11_simple_multiplexed.amplitude_arr),
    np.absolute(bpsk_10_11_simple_multiplexed.amplitude_arr))

bpsk_10_11_time_multiplexed = time_multiplexing(code_10, code_11)
multiplexed_signals_plot(
    np.real(bpsk_10_11_time_multiplexed.amplitude_arr),
    np.absolute(bpsk_10_11_time_multiplexed.amplitude_arr),
    time_arr=bpsk_10_11_time_multiplexed.time_arr)


bpsk_10_11_alt_boc_multiplexed = alt_boc_multiplexing(
    bpsk_signal_10_complexed.amplitude_arr,
    bpsk_signal_11_complexed.amplitude_arr)
multiplexed_signals_plot(
    np.real(bpsk_10_11_alt_boc_multiplexed.amplitude_arr),
    np.absolute(bpsk_10_11_alt_boc_multiplexed.amplitude_arr))

bpsk_10_11_alt_boc_multiplexed_spectrum = spectrum_alt_boc(
    bpsk_10_11_alt_boc_multiplexed)
spectrum_plot(bpsk_10_11_alt_boc_multiplexed_spectrum.amplitude_arr,
              bpsk_10_11_alt_boc_multiplexed_spectrum.freq_arr)


