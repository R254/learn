class Car:
	def __init__(self):
		self.engine= False

	def start_engine(self):
			print("Starting Engine!")
			self.engine = True

	def stop_engine(self):
			print("Stopping the car engine")
			self.engine = False

	def drive(self):
		if self.engine:
			print("Driving the car")
		else:
			print("Please start the engine first!")
class BlueCar:
	color = 'Blue'

class Honda(Car,BlueCar): # a child class can inherit from several classes.
	model="Honda" # car = HondaCivic()
# Overriding is shown below where the child class use the specific start engine method.
	#def start_engine(self):
	#	print("Starting the engine of our Honda")
	#	self.engine = True

#Calling a parent class methods and modifying its functionality.
	def start_engine(self):
		super().start_engine()
		print("Honda! Start Engine!")
class HondaCivic(Honda):
	model = "Honda Civic"