from abc import abstractmethod
from typing import Callable
from venv import logger


class FOOD():
    def __init__(self, price, **kwargs):
        self.price=price
    @abstractmethod
    def sale(self, num) -> int:
        return self.price * num


class FOODFACTORY():
    """The factory for creating food"""
    registry = {}  # Internal registry for available food
    @classmethod
    def register(cls, name: str) -> Callable:
        def inner_wrapper(wrapped_class:FOOD) -> Callable:
            if name in cls.registry:
                logger.warning('Food %s already exists. Will replace it', name)
            cls.registry[name] = wrapped_class
            return wrapped_class
        return inner_wrapper

    @classmethod
    def create_food(cls, name:str, **kwargs) -> FOOD:
        if name not in cls.registry:
            logger.warning('Food %s does not exist in the registry', name)
            return None
        food_class = cls.registry[name]
        food = food_class(**kwargs)
        return food


@FOODFACTORY.register('heytea')
class HEYTEA(FOOD):
    pass

heytea = FOODFACTORY.create_food('heytea', price=30)
print(heytea.sale(2))