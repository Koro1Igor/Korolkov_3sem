from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    name = "геометрическая фигура"

    @abstractmethod
    def area(self):
        pass

    @classmethod
    def figureName(cls):
        return cls.name