from typing import Tuple

import pygame
from pygame import Surface, Rect, Vector2


class Tile:
    tile_type: int
    position: Vector2
    size: Vector2
    tile_type_to_color: dict[int, str] = {
        0: "grey90",
        1: "grey70",
        2: "grey30",
        3: "grey10"
    }

    def __init__(self, tile_type: int, position: Vector2, size: Vector2):
        self.position = position
        self.tile_type = tile_type
        self.size = size

    def draw(self, surface: Surface):
        pygame.draw.rect(surface, self.tile_type_to_color[self.tile_type], Rect(self.position, self.size), 0)
