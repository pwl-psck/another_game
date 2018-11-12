import pygame

class Target():
	""" Klasa opisująca cel i jego właściwości."""
	def __init__(self, ag_settings, screen):
		# Inicjalizacja prostokąta celu na górze ekranu.
		self.settings = ag_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.rect = pygame.Rect(0, 0, self.settings.target_width,
		self.settings.target_height)
		self.rect.top = 0
		self.rect.right = self.screen_rect.right - 10
		# Cel porusza się na początku w dół.
		self.move_down = True
		self.move_up = False
	
	
	def update(self):
		# Cel porusza się zgodnie z ustawionym kierunkiem, a po dotarciu
		# do krawędzi zmienia kierunek ruchu.
		if self.move_down:
			self.rect.centery += self.settings.target_speed_factor
			if self.rect.bottom >= self.screen_rect.bottom:
				self.move_down = False
				self.move_up = True
		elif self.move_up:
			self.rect.centery -= self.settings.target_speed_factor
			if self.rect.top <= 0:
				self.move_down = True
				self.move_up = False
		
	def draw_target(self):
		# Wyświetlenie celu w aktualnej pozycji.
		self.screen.fill(self.settings.target_color, self.rect)

	def reset(self):
		# Resetowanie pozycji i kierunku celu.
		self.move_down = True
		self.rect.top = 0
