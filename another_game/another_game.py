import pygame
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from ship import Ship
from target import Target
from button import Button

def run_game():
	# Utworzenie ekranu gry.
	ag_settings = Settings()
	screen = pygame.display.set_mode((ag_settings.screen_width, 
	ag_settings.screen_height))
	pygame.display.set_caption('Another Game')
		
	# Utworzenie statku, grupy pocisku i celu.
	ship = Ship(ag_settings, screen)
	target = Target(ag_settings, screen)
	bullets = Group()
	# Utworzenie przycisku startującego grę.
	play_button = Button(screen)
	
	while True:
		gf.check_events(ship, bullets, screen, ag_settings, play_button,
		 target)
		gf.update_screen(screen, ag_settings, ship, bullets, target,
		 play_button)
		if ag_settings.game_active:
			gf.move_items(ship, bullets, target, ag_settings)
		
		
run_game()
