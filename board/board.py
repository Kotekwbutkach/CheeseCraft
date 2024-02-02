from typing import List

from pygame import Surface, Vector2

from board.tile import Tile


class Board:
    tiles: List[List[Tile]]

    def __init__(self, x, y, tile_size=50):
        self.tiles = list()
        for iy in range(y):
            self.tiles.append(list())
            for ix in range(x):
                self.tiles[iy].append(
                    Tile((ix+iy) % 2, Vector2(ix * tile_size, iy * tile_size), (tile_size, tile_size)))

    def draw(self, surface: Surface):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                self.tiles[y][x].draw(surface)
