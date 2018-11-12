import pygame

class Ship():
	""" Klasa zarządzająca statkiem."""
	def __init__(self, ag_settings, screen):
		# Wczytanie obrazu statku i ustawienie go w położeniu początkowym.
		self.image = pygame.image.load('images/ship.png')
		self.screen = screen
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.left = 0
		self.rect.centery = self.screen_rect.centery
		self.settings = ag_settings
		
		# Przechowanie punktu środkowego statku w postaci zmiennoprzecinkowej.
		self.center = float(self.rect.centery)
		
		# Na początku statek pozostaje nieruchomy.
		self.moving_up_active = False
		self.moving_down_active = False
		
	def update(self):
		# Zmiana pozycji statku jeśli to możliwe.
		if self.moving_up_active and self.rect.top > 0:
			self.center -= self.settings.ship_speed_factor
			self.rect.centery = int(self.center)
		elif (self.moving_down_active and
		 self.rect.bottom < self.screen_rect.bottom):
			 self.center += self.settings.ship_speed_factor
			 self.rect.centery = int(self.center)
	
	def blitme(self):
		# Wklejenie obrazu statku na ekran gry.
		self.screen.blit(self.image, self.rect)
		
	def reset(self):
		# Resetowanie pozycji statku.
		self.center = float(self.screen_rect.centery)
		self.rect.centery = int(self.center)
		
		
