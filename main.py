"""Main entry point. Run with: python main.py"""
import asyncio
import random
import time
import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game.game import Game
from gui.renderer import Renderer
from gui.menu import Menu


async def main() -> None:
    random.seed(time.time_ns())

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('\u81ea\u6478\u00b7\u91e3\u5bf6')

    menu     = Menu(screen)
    renderer = Renderer(screen)
    renderer.setup_fonts()

    game:      Game | None = None
    app_state: str         = 'menu'
    running                = True

    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FPS)

        # -- Event handling --
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break

            if app_state == 'menu':
                result = menu.handle_event(event)
                if result == 'start':
                    game      = Game()
                    app_state = 'game'
            else:
                action = renderer.handle_event_for_game(event, game)
                if action == 'menu':
                    game      = None
                    app_state = 'menu'

        if not running:
            break

        # -- Update & render --
        if app_state == 'menu':
            menu.draw()
        else:
            game.update(dt)
            renderer.draw(game)

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())
