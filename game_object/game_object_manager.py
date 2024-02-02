from typing import List

from pygame import Surface

from game_object.object.game_object import GameObject


class GameObjectManager:
    objects: List[GameObject]

    def __init__(self):
        self.objects = []

    def add(self, other: GameObject):
        self.objects.append(other)

    def draw(self, surface: Surface):
        for obj in self.objects:
            obj.draw(surface)
