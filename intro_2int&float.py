num = 3.0 #Float
num = 3 #Integer. The print function gives the last declared variable if those preceding it has same name

#print(type(num))# Gives us the data type stored in num variable

# Arithmetic Operators
# Addition: 5 + 2
# Subtraction: 5 - 2
# Multiplication: 5 * 2
# Division: 5 / 2
# Floor Division: 5 // 2
# Exponent: 5 ** 2
# Modulus: 5 % 2
#print(5+2)
#print(5-2)
#print(5*2)
#print(5/2)
#print(5//2)
#print(5**2)
#print(11%3)
#print((5+2)*2) #It use the Bodmas mathematical technique


#Incrementing a variable
num=1
num += 3 # Incrementing num variable
#num *=3
num = f'{num} - This is the incremented value'
#print(num)

#getting absolute values
#print(abs(-3)) # prints absolute values of every value parsed in abs() method
#print(round(4.574514567, 6))# the round method rounds off the float values to the nearest integer. 
#Adding the value after the coma gives decimal values to round off to.

#Comparison
#Equal: 			3 == 2	
#Not Equal:			3 != 2
#Greater than:		3 >  2	
#Less than:			3 <  2
#Greater or Equal:	3 >= 2
#Less or Equal:		3 <= 2

#num_1 = 3
#num_2 = 2

#print(num_1 == num_2)
#print(num_1 != num_2)
#print(num_1 > num_2)
#print(num_1 < num_2)
#print(num_1 >= num_2)
#print(num_1 <= num_2)

#casting strings to integers
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)