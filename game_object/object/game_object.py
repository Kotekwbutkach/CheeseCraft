from abc import abstractmethod

from pygame import Surface, Vector2


class GameObject:
    position: Vector2

    def __init__(self, x: int, y: int):
        self.position = Vector2(x, y)

    def move(self, dpos: Vector2):
        self.position += dpos

    @abstractmethod
    def draw(self, surface: Surface):
        raise NotImplementedError
