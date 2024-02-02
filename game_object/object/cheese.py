import pygame
from pygame import Surface

from game_object.object.game_object import GameObject


class Cheese(GameObject):

    def draw(self, surface: Surface):
        x, y = self.position[0], self.position[1]
        pygame.draw.polygon(surface, "yellow", ((x - 20, y - 25), (x - 30, y - 10), (x + 30, y - 10)), 0)
        pygame.draw.rect(surface, "yellow3", ((x - 30, y - 10), (60, 30)), 0)
        pygame.draw.circle(surface, "yellow4", [x - 15, y], 5, 0)
        pygame.draw.circle(surface, "yellow4", [x - 23, y + 11], 3, 0)
        pygame.draw.circle(surface, "yellow4", [x + 10, y + 10], 8, 0)
        pygame.draw.circle(surface, "yellow4", [x + 20, y - 5], 3, 0)