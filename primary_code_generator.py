import numpy as np
from config import E6PrimaryCodes


def get_primary_code_from_file(path: E6PrimaryCodes) -> np.array:
    code = __open_file(path.value)
    code = __format_code(code)
    code = __code_to_bin(code)
    code = __code_convert(code)
    return code


def __open_file(path: str) -> str:
    with open(path) as file:
        return file.read()


def __format_code(code: str) -> str:
    code = code.split(';')[1]
    code = code.replace('\n', '')
    return code


def __code_to_bin(code: str) -> str:
    return bin(int(code, 16))


def __code_convert(code: str) -> np.ndarray:
    """Перевод кода из формата 0/1 в -1/+1"""
    code = str(code).replace('0b', '')
    code = [int(chip) for chip in code]
    return np.array([-1 if element == 0 else element for element in code],
                    dtype=int)
