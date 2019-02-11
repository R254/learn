class Car:
	def __init__(self):
		self.engine= False

	def start_engine(self):
			print("Starting Engine!")
			self.engine = True

	def stop_engine(self):
			print("Stopping the engine")
			self.engine = False

	def drive(self):
		if self.engine:
			print("Driving the car")
		else:
			print("Please start the engine first!")

class HondaCivic(Car):
	model="Honda Civic"
	color="Blue"