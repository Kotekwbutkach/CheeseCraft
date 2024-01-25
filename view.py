from typing import Tuple

import pygame


def draw_mouse(position: Tuple[int, int]):
    x, y = position
    pygame.draw.circle(window, "grey60", [x, y], 25, 0)
    pygame.draw.circle(window, "grey45", [x - 20, y - 20], 15, 0)
    pygame.draw.circle(window, "grey45", [x + 20, y - 20], 15, 0)
    pygame.draw.circle(window, "grey70", [x - 10, y], 5, 0)
    pygame.draw.circle(window, "grey70", [x + 10, y], 5, 0)
    pygame.draw.circle(window, "grey30", [x - 10, y], 2, 0)
    pygame.draw.circle(window, "grey30", [x + 10, y], 2, 0)
    pygame.draw.circle(window, "grey30", [x, y + 10], 3, 0)


def draw_cat(position: Tuple[int, int]):
    x, y = position
    pygame.draw.circle(window, "darkorange", [x, y], 25, 0)
    pygame.draw.polygon(window, "darkorange2", ((x-30, y-30), (x-25, y-5), (x-5, y-25)), 0)
    pygame.draw.polygon(window, "darkorange2", ((x+30, y-30), (x+25, y-5), (x+5, y-25)), 0)
    pygame.draw.polygon(window, "darkorange4", ((x-25, y-25), (x-20, y-10), (x-10, y-20)), 0)
    pygame.draw.polygon(window, "darkorange4", ((x+25, y-25), (x+20, y-10), (x+10, y-20)), 0)
    pygame.draw.circle(window, "moccasin", [x - 10, y], 5, 0)
    pygame.draw.circle(window, "moccasin", [x + 10, y], 5, 0)
    pygame.draw.circle(window, "darkred", [x - 10, y], 2, 0)
    pygame.draw.circle(window, "darkred", [x + 10, y], 2, 0)
    pygame.draw.circle(window, "darkorange4", [x, y + 10], 2, 0)
    pygame.draw.ellipse(window, "darkorange4", [x-3, y + 8, 6, 2], 0)


def draw_cheese(position: Tuple[int, int]):
    x, y = position
    pygame.draw.polygon(window, "yellow", ((x-20, y-25), (x-30, y-10), (x+30, y-10)), 0)
    pygame.draw.rect(window, "yellow3", ((x-30, y-10), (60, 30)), 0)
    pygame.draw.circle(window, "yellow4", [x - 15, y], 5, 0)
    pygame.draw.circle(window, "yellow4", [x - 23, y+11], 3, 0)
    pygame.draw.circle(window, "yellow4", [x + 10, y+10], 8, 0)
    pygame.draw.circle(window, "yellow4", [x + 20, y - 5], 3, 0)


if __name__ == "__main__":
    pygame.init()

    window = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('CheeseCraft')

    running = True

    mouse_x = 75
    mouse_y = 75
    cat_x = 225
    cat_y = 75
    cheese_x = 150
    cheese_y = 150

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("grey25")

        draw_mouse((mouse_x, mouse_y))
        draw_cat((cat_x, cat_y))
        draw_cheese((cheese_x, cheese_y))

        pygame.display.flip()
