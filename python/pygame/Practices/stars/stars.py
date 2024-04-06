import pygame
import sys

SCREENSIZE = (400, 600)


def star_cols(screen, star_width):
    col_num = screen.get_rect().width / star_width
    return int(col_num)


def run_game():
    pygame.init()

    screen = pygame.display.set_mode(SCREENSIZE)

    # Set the caption for the game window
    pygame.display.set_caption("My game window")

    # Load the image
    background = pygame.image.load("background.png")
    star = pygame.image.load("star.png")

    star_width = star.get_rect().width
    star_height = star.get_rect().height
    cols = star_cols(screen, star_width)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Draw the background at the top left corner
            screen.blit(background, (0, 0))

            for col in range(0, cols):
                star_x = star_width + col * star_width
                background.blit(star, (star_x, 10))

            # Update the display
            pygame.display.update()


run_game()