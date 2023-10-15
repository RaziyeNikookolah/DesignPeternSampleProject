from abc import ABC, abstractmethod


class Tool(ABC):
    @abstractmethod
    def mouse_down():
        ...

    @abstractmethod
    def mouse_up():
        ...
