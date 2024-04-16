from abc import ABC

class Shape(ABC):
    def __init__(self) -> None:
        self.name

    def generate_mesh(self):
        raise NotImplementedError