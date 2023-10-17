from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress():
        ...
