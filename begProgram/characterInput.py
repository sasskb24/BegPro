#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old
from datetime import datetime

name = input('Enter your name: ')
age = int(input('Enter your age: '))

year = datetime.now().year
result = str(year - age + 100)
number = int(input('Please enter your number: '))
print(('ou will be 100 years in ' + result + '\n') * number)
print('The End!')