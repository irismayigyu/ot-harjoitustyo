
import sys
import pygame
from ui.start import Start


def init():
    '''Funktio, joka kutsuu pelin alkua

    Args:
            clock: aika
            fps: frames-per-second
            start: Start-luokan olio
            start_loop: Start-luokan metodi

    '''
    pygame.init()
    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()
    fps = 60
    clock.tick(fps)
    start = Start()
    start.start_loop()


def quit_game():
    sys.exit()


if __name__ == "__main__":
    init()
