import pygame
import sys
from bullet import Bullet

def fire_bullet(ship, screen, bullets, ag_settings):
	# Wystrzelenie pocisku.
	new_bullet = Bullet(ag_settings, screen, ship)
	bullets.add(new_bullet)
	
def check_keydown_event(event, ship, bullets, screen, ag_settings):
	# Funkcja obsługująca naciśniecie klawisza.
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_DOWN:
		ship.moving_down_active = True
	elif event.key == pygame.K_UP:
		ship.moving_up_active = True
	elif event.key == pygame.K_SPACE and len(bullets) == 0:
		fire_bullet(ship, screen, bullets, ag_settings)

def check_keyup_event(event, ship):
	# Funkcja obsługująca zwolnienie klawisza.
	if event.key == pygame.K_DOWN:
		ship.moving_down_active = False
	elif event.key == pygame.K_UP:
		ship.moving_up_active = False

def start_game(ag_settings, ship, target, bullets):
	# Wystartowanie gry, reset położenia przedmiotów oraz statystyk.
	ag_settings.game_active = True
	ag_settings.reset()
	ship.reset()
	target.reset()
	bullets.empty()
	
def check_play_button(screen, play_button, ag_settings, ship, target, 
bullets, mouse_x, mouse_y):
	# Sprawdzenie czy przycisk startu został kliknięty.
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not ag_settings.game_active:
		start_game(ag_settings, ship, target, bullets)

def check_events(ship, bullets, screen, ag_settings, play_button, target):
	# Funkcja przechwytująca i obsługująca zdarzenia myszy i klawiatury.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ship, bullets, screen, ag_settings)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(screen, play_button, ag_settings, ship,
			target, bullets, mouse_x, mouse_y)

def update_screen(screen, ag_settings, ship, bullets, target, play_button):
	# Wyświetlenie przedmiotów na ekranie w aktualnych pozycjach.
	screen.fill(ag_settings.bg_color)
	ship.blitme()
	for bullet in bullets:
		bullet.draw_bullet()
	target.draw_target()
	# Przycisk startu gry jest wyświetlany, gdy gra jest nieaktywna.
	if not ag_settings.game_active:
		play_button.draw_button()
	
	pygame.display.flip()
	
def check_bullet_target_collision(bullets, target, ag_settings):
	# Sprawdzenie czy cel został trafiony pociskiem.
	if pygame.sprite.spritecollideany(target, bullets):
			bullets.empty()
			ag_settings.target_hits += 1
			if ag_settings.target_hits == 3:
				ag_settings.target_speed_up()
				ag_settings.target_hits = 0

def move_items(ship, bullets, target, ag_settings):
	# Aktualizacja położenia statku, pocisku i celu.
	ship.update()
	for bullet in bullets:
		bullet.update(bullets, ag_settings)
	target.update()
	check_bullet_target_collision(bullets, target, ag_settings)
				
