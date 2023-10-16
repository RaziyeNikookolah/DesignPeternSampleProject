from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...
