from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def square(self) -> float:
        pass
    
    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        pass
    
    @abstractmethod
    def get_color(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass