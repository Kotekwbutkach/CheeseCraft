import pygame
from pygame import Surface

from game_object.object.game_object import GameObject


class Cat(GameObject):

    def draw(self, surface: Surface):
        x, y = self.position[0], self.position[1]
        pygame.draw.circle(surface, "darkorange", [x, y], 25, 0)
        pygame.draw.polygon(surface, "darkorange2", ((x - 30, y - 30), (x - 25, y - 5), (x - 5, y - 25)), 0)
        pygame.draw.polygon(surface, "darkorange2", ((x + 30, y - 30), (x + 25, y - 5), (x + 5, y - 25)), 0)
        pygame.draw.polygon(surface, "darkorange4", ((x - 25, y - 25), (x - 20, y - 10), (x - 10, y - 20)), 0)
        pygame.draw.polygon(surface, "darkorange4", ((x + 25, y - 25), (x + 20, y - 10), (x + 10, y - 20)), 0)
        pygame.draw.circle(surface, "moccasin", [x - 10, y], 5, 0)
        pygame.draw.circle(surface, "moccasin", [x + 10, y], 5, 0)
        pygame.draw.circle(surface, "darkred", [x - 10, y], 2, 0)
        pygame.draw.circle(surface, "darkred", [x + 10, y], 2, 0)
        pygame.draw.circle(surface, "darkorange4", [x, y + 10], 2, 0)
        pygame.draw.ellipse(surface, "darkorange4", [x - 3, y + 8, 6, 2], 0)