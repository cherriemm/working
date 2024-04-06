import pygame
import sys
from bullet import Bullet
from alien import Alien

def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def check_keydown_events(settings, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, settings, screen, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(settings, screen, event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets, aliens, settings, screen, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        create_fleet(settings, screen, aliens, ship)


def fire_bullet(bullets, settings, screen, ship):
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(settings, screen):
    alien = Alien(settings, screen)
    available_space_x = settings.screen_width - alien.rect.width * 2
    number_aliens_x = int(available_space_x / (alien.rect.x * 2))
    return number_aliens_x


def get_number_aliens_y(settings, screen, ship):
    alien = Alien(settings, screen)
    available_space_y = settings.screen_height - 3 * alien.rect.height - ship.rect.height
    number_aliens_y = int(available_space_y / (2 * alien.rect.height))
    return number_aliens_y


def create_alien(settings, screen, alien_number, row_number, aliens):
    alien = Alien(settings, screen)
    alien.x = alien.rect.width + alien.rect.width * 2 * alien_number
    alien.y = alien.rect.height + alien.rect.height * 2 * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(settings, screen, aliens, ship):
    number_aliens_x = get_number_aliens_x(settings, screen)
    row_numbers = get_number_aliens_y(settings, screen, ship)
    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, alien_number, row_number, aliens)


def change_fleet_direction(aliens, settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(aliens, settings):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(aliens, settings)
            break


def update_aliens(aliens, settings, ship):
    check_fleet_edges(aliens, settings)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")