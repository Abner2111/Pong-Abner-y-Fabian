import pygame

def main():
    pygame.init()

    pygame.display.set_mode([800, 400])
    pygame.display.set_caption("Pong")
    salir =  False

    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        pygame.display.update()
    pygame.quit()


main()