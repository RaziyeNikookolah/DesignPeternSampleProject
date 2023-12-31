from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def apply():
        ...
