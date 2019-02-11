x = [1,2,3]

len(x) #gives the length of characters
x.append(4) # adds 4 to the list
x.pop() # removes the last value in the list


newlist = list() # a way of creating new objects
newstring = str()
type(newstring) # checking the type of data type


#Classes and how they work with objects
class Car:
	color = "blue"
	def drive(self):
		print("Driving car!")
	def paint_car(self, color):
		self.car_color = color
mycar=Car()
mycar.color

#Using init function
class Car:
	def __init__(self,color):
		self.color = color
mycar=Car("red") #Assign a red color to mycar
othercar=Car("green") #Assign a green color to othercar