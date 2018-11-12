import shelve, os

class GameStats():
	"""Monitorowanie danych statystycznych w grze 'Inwazja obcych'."""
	
	def __init__(self, ai_settings):
		"""Inicjalizacja danych statystycznych."""
		self.ai_settings = ai_settings
		self.reset_stats()
		#Uruchomienie gry 'Inwazja obcych' w stanie mieaktywnym.
		self.game_active = False
		#Najlepszy wynik nigdy nie powinien zostać wyzerowany.
		self.get_high_score()
		
		
	def reset_stats(self):
		"""Inicjalizacja danych statystycznych, które mogą się zmieniać 
		w trakcie gry."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
	
	def get_high_score(self):
		"""Wczytanie najlepszego wyniku lub utworzenie nowego pliku z 
		wynikiem jeśli taki nie istnieje."""
		if os.path.isfile('data/score'):
			self.file = shelve.open('data/score')
			self.high_score = self.file['high_score']
			self.file.close()
		else:
			self.file = shelve.open('data/score', writeback = True)
			self.high_score = 0
			self.file['high_score'] = self.high_score
			self.file.close()
	
	def write_high_score(self):
		"""Zapisanie najlepszego wyniku w pliku"""
		self.file = shelve.open('data/score', writeback = True)
		self.file['high_score'] = self.high_score
		self.file.close()
			
