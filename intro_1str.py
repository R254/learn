
singleline = 'This is a single line string'
multi_line = '''
This is a multi-line
string'''


#message = 'Hello world!'

#message=message.replace('world', 'Ruto') # replaces world with ruto in the message variable


#print(singleline)
#print(multi_line)
#print(len(message)) # This gives the length of the string characters.
#print(message[0]) # This will bring out the string in index zero. You can as well replace zero with another index within the given string. Python will bring an index error.
#print(message[0:5]) # This brings out values of indices 0-4; index 5 is not inclusive despite indication in the range.
#print(message[:5]) # This gives us the string from the beginning to index for giving us the result as in the above line of code.
# Similarly we can output the statement from a given index to the end as given below
#print(message[6:])


#print(message.lower()) # This print the string in lower case
#print(message.upper())# This print the string in upper case
#print(message.capitalize())# make the first character have upper case and the rest lower case.
#print(message.count('l'))# counts the number of words or strings parsed in
#print(message.find('world'))# Gives us the index of the first character of the string parsed in
#print(message.find('ruto')) # Finding a string that doesn't exist in the variable gives the negative -1

#Below are ways to concatinate strings
greeting = 'Hello'
name = 'Ruto'
#message = greeting + name # This will output "HelloRuto"
#message = greeting + ', '+ name+'. welcome'
#message= '{}, {}. Welcome'.format(greeting,name)


message= f'{greeting}, {name}. Welcome' # Using f-string simplify the concatination. This is used in python 3.6 and above
# f-strings makes it easier to add methods to the variable for example as shown below
message= f'{greeting}, {name.upper()}. Welcome'
#print(message)
#print(dir(name)) # Gives all available methods that are available to be used.


#print(help(str)) #- gives us the descriptions of methods which are being used with strings
#To be more specific, you can parse in str.method for easy access of the specific method as shown below.
#print(help(str.capitalize))