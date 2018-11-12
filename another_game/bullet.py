from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
	""" Klasa odpowiadająca za wyświetlanie i ruch pocisku."""
	def __init__(self, ag_settings, screen, ship):
		# Inicjacja prostokąta pocisku i ustawienie go pod dziobem statku.
		super().__init__()
		self.settings = ag_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ship = ship
		self.ship_rect = self.ship.rect
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
		self.settings.bullet_height)
		self.rect.right = self.ship_rect.right
		self.rect.centery = self.ship_rect.centery
		
	def update(self, bullets, ag_settings):
		# Poruszenie pocisku i usunięcie go jeśli wyjdzie za ekran gry.
		self.rect.centerx += self.settings.bullet_speed_factor
		if self.rect.left >= self.screen_rect.right:
			bullets.empty()
			ag_settings.lost_life()
			if ag_settings.lives_left == 0:
				ag_settings.game_active = False
	
	def draw_bullet(self):
		# Narysowanie pocisku w aktualnej pozycji.
		self.screen.fill(self.settings.bullet_color, self.rect)	
		
