from typing import Tuple

import pygame

from game_object.game_object_factory import GameObjectFactory
from game_object.game_object_manager import GameObjectManager
from game_object.position import Position

if __name__ == "__main__":
    pygame.init()

    game_manager = GameObjectManager()
    mouse = GameObjectFactory.create(75, 75, "Mouse")
    game_manager.add(mouse)
    cat = GameObjectFactory.create(225, 75, "Cat")
    game_manager.add(cat)
    cheese = GameObjectFactory.create(150, 150, "Cheese")
    game_manager.add(cheese)
    window = pygame.display.set_mode((300, 200))
    pygame.display.set_caption('CheeseCraft')

    clock = pygame.time.Clock()
    running = True

    frame = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("grey25")

        frame = (frame + 1) % 300

        delta = Position(0, -1)
        if frame < 75:
            delta = Position(1, 0)
        elif frame < 150:
            delta = Position(0, 1)
        elif frame < 225:
            delta = Position(-1, 0)

        mouse.move(delta)
        game_manager.draw(window)

        pygame.display.flip()
        clock.tick(60)
