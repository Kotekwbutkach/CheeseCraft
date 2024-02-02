import pygame
from pygame import Surface

from game_object.object.game_object import GameObject


class Mouse(GameObject):

    def draw(self, surface: Surface):
        x, y = self.position[0], self.position[1]

        pygame.draw.circle(surface, "grey60", (x, y), 25, 0)
        pygame.draw.circle(surface, "grey45", [x - 20, y - 20], 15, 0)
        pygame.draw.circle(surface, "grey45", [x + 20, y - 20], 15, 0)
        pygame.draw.circle(surface, "grey70", [x - 10, y], 5, 0)
        pygame.draw.circle(surface, "grey70", [x + 10, y], 5, 0)
        pygame.draw.circle(surface, "grey30", [x - 10, y], 2, 0)
        pygame.draw.circle(surface, "grey30", [x + 10, y], 2, 0)
        pygame.draw.circle(surface, "grey30", [x, y + 10], 3, 0)