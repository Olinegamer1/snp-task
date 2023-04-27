from typing import Union


class Dessert:
    _name: str
    _calories: Union[int, float]

    def __init__(self, name: str = 'unknown', calories: Union[int, float] = 0):
        self._name = name
        self._calories = calories

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def calories(self) -> Union[int, float]:
        return self._calories

    @calories.setter
    def calories(self, calories: Union[int, float]):
        self._calories = calories

    def is_healthy(self) -> bool:
        return self._calories < 200

    def is_delicious(self) -> bool:
        return True
