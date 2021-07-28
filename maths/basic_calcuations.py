
from typing import Union


class BasicCalculation():
    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b

    def addition(self) -> int:
        return self._a + self._b

    def substract(self) -> int:
        return self._a - self._b

    def multiply(self) -> int:
        return self._a * self._b

    def divide(self) -> Union[float, str]:
        try:
            return self._a / self._b
        except ZeroDivisionError:
            return f'Can not divide {self._a} by {self._b}'
