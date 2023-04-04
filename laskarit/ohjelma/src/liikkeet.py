
import pygame

class Liikkeet:
    pygame.init()
    naytto = pygame.display.set_mode((400,400))
    # x = leveys/2-robo.get_width()/2
    # y = korkeus/2-robo.get_height()/2
    oikealle = False
    vasemmalle = False
    ylos = False
    alas = False
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = True
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = True
                if tapahtuma.key == pygame.K_UP:
                    ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    alas = True
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = False
                if tapahtuma.key == pygame.K_UP:
                    ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    alas = False
            if tapahtuma.type == pygame.QUIT:
                exit()

        if oikealle:
            x += 2
        if vasemmalle:
            x -= 2
        if ylos:
            y -= 2
        if alas:
            y += 2
        x = max(x,0)
        x = min(x,leveys-robo.get_width())
        y = max(y,0)
        y = min(y,korkeus-robo.get_height())

        pygame.display.flip()

