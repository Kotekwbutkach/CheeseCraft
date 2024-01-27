from abc import abstractmethod

from pygame import Surface

from game_object.position import Position


class GameObject:
    position: Position

    def __init__(self, x: int, y: int):
        self.position = Position(x, y)

    def move(self, dpos: Position):
        self.position += dpos

    @abstractmethod
    def draw(self, surface: Surface):
        raise NotImplementedError
