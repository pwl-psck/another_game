class Settings():
	""" Klasa przechowywująca ustawienia gry Another Game."""
	def __init__(self):
		# Ustawienia ekranu gry.
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (10, 10, 210)
		
		# Ustawienia statku.
		self.ship_speed_factor = 1
		self.lives_left = 3
		
		# Ustawienia pocisków.
		self.bullet_speed_factor = 6
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (210, 10, 10)
				
		# Ustawienia celu.
		self.target_speed_up_factor = 1.4
		self.target_speed_factor = 1
		self.target_width = 10
		self.target_height = 400
		self.target_color = (100, 100, 10)
		self.target_hits = 0
		# Ustawienia gry.
		self.game_active = False
	
	def reset(self):
		# Resetowanie liczby żyć, szybkości celu i ilości trafień.
		self.lives_left = 3
		self.target_speed_factor = 1
		self.target_hits = 0
		
	def lost_life(self):
		# Strata życia.
		self.lives_left -= 1
	
	def target_speed_up(self):
		self.target_speed_factor *= self.target_speed_up_factor
		
