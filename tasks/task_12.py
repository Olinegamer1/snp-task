from tasks.task_11 import Dessert
from typing import Union


class JellyBean(Dessert):
    _flavor: str

    def __init__(self, name: str = 'unnamed',
                 calories: Union[int, float] = 0,
                 flavor: str = 'unknown'):
        super().__init__(name=name, calories=calories)
        self._flavor = flavor

    @property
    def flavor(self) -> str:
        return self._flavor

    @flavor.setter
    def flavor(self, flavor: str):
        self._flavor = flavor

    def is_delicious(self) -> bool:
        return self._flavor.lower() != 'black licorice'

    def __repr__(self) -> str:
        return super().__repr__() + f', flavor={self.flavor}'
