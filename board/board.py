from typing import List

from pygame import Surface, Vector2

from board.tile import Tile


class Board:
    tiles: List[List[Tile]]

    def __init__(self, tiles: List[List[int]], tile_size=50):
        self.tiles = list()
        for iy in range(len(tiles)):
            self.tiles.append(list())
            for ix in range(len(tiles[iy])):
                self.tiles[iy].append(
                    Tile(tiles[iy][ix], Vector2(ix * tile_size, iy * tile_size), Vector2(tile_size, tile_size)))

    def draw(self, surface: Surface):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                self.tiles[y][x].draw(surface)
