import pygame

def main():
    pygame.init()

    pygame.display.set_mode([800, 400])
    pygame.display.set_caption("Pong")
    salir =  False
    reloj1 = pygame.time.Clock()

    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
        reloj1.tick(20)
        pygame.display.update()
    pygame.quit()


main()