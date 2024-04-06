import pygame
from ship import Ship
from alien import Alien
from settings import Settings
import game_functions as gf
from pygame.sprite import Group

def run_game():
    
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, settings)
    aliens = Group()
    gf.create_fleet(settings, screen, aliens, ship)
    bullets = Group()
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens, settings, screen, ship)
        gf.update_aliens(aliens,settings, ship)
        gf.update_screen(settings, screen, ship, bullets, aliens)

        

run_game()