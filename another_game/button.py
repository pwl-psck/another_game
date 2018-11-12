import pygame.font
pygame.font.init()
class Button():
	""" Klasa opisująca przycisk rozpoczęcia gry"""
	def __init__(self, screen):
		# Inicjacja początkowych ustawień.
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.msg = 'Start'
		# Wymiary i kolory przycisku.
		self.width = 200
		self.height = 50
		self.button_color = (210, 10, 10)
		self.text_color = (255, 255, 255)
		# Czcionka napisu.
		self.font = pygame.font.SysFont(None, 48)
		# Prostokąt przycisku wyśrodkowany na ekranie gry.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# Renderowanie komunikatu na środku przycisku.
		self.msg_image = self.font.render(self.msg, True, self.text_color,
		self.button_color)
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.center = self.rect.center
		
	def draw_button(self):
		# Rysowanie przycisku i komunikatu na nim.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_rect)
		
		
