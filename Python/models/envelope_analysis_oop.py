from abc import ABC, abstractmethod
from typing import Any


class Input(ABC):

    @abstractmethod
    def input_side(self) -> Any:
        pass


class FloatInput(Input):
    def __init__(self, value: str):
        self._value = value

    def input_side(self) -> float:
        while True:
            try:
                entered_side = float(input('Enter {0} of the envelope: '.format(self._value)))
                return entered_side
            except ValueError:
                print('Invalid value. Please try again.\n')


class Rule(ABC):

    @abstractmethod
    def passed(self, value: Any) -> bool:
        pass


class GreaterThenZero(Rule):
    def passed(self, value: float) -> bool:
        return value > 0


class CheckingRules(Rule):
    def __init__(self, *rules: Any):
        self._test = rules

    def passed(self, value: float) -> bool:
        passed = True
        for rule in self._test:
            if not rule.passed(value):
                print(f'{rule.__class__.__name__} is failed. Please try again.\n')
                passed = False
        return passed


class Envelope:
    def __init__(self, first_side: float, second_side: float):
        self._first_side = first_side
        self._second_side = second_side
        self._diagonal = first_side ** 2 + second_side ** 2

    def __lt__(self, other) -> bool:
        return self._diagonal < other._diagonal


class Choice:
    def do_continue(self) -> bool:
        response = input('Do you want to continue? [y / yes]\n')
        if (response.lower() == 'y') or (response.lower() == 'yes'):
            return True
        else:
            return False