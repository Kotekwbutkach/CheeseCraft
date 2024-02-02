import pygame
from pygame import Vector2

from board.board import Board
from game_object.game_object_factory import GameObjectFactory
from game_object.game_object_manager import GameObjectManager

if __name__ == "__main__":
    pygame.init()

    tiles = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3],
        [3, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3],
        [3, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3],
        [3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3],
        [3, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3],
        [3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3],
        [3, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3],
        [3, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3],
        [3, 2, 3, 3, 3, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 3],
        [3, 2, 2, 2, 2, 2, 3, 1, 0, 1, 0, 1, 0, 1, 0, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    ]

    board = Board(tiles, 50)

    game_manager = GameObjectManager()
    mouse = GameObjectFactory.create(75, 125, "Mouse")
    game_manager.add(mouse)
    cat = GameObjectFactory.create(225, 75, "Cat")
    game_manager.add(cat)
    cheese = GameObjectFactory.create(275, 325, "Cheese")
    game_manager.add(cheese)
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('CheeseCraft')

    clock = pygame.time.Clock()
    running = True

    frame = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("grey25")

        frame = (frame + 1) % 1200

        delta = Vector2(0, -1)
        if frame < 200:
            delta = Vector2(1, 0)
        elif frame < 600:
            delta = Vector2(0, 1)
        elif frame < 800:
            delta = Vector2(-1, 0)

        mouse.move(delta)
        board.draw(window)
        game_manager.draw(window)

        pygame.display.flip()
        clock.tick(90)
