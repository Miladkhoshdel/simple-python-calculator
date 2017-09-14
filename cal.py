#Created By: Milad Khoshdel
#Blog: https://blog.regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkho5hdel

import os

os.system('CLS')
print('')
print(' _______ _______ _       _______         _       _______________________ _______ ')
print('(  ____ (  ___  | \     (  ____ \\     /( \     (  ___  )__   __(  ___  |  ____ )')
print('| (    \/ (   ) | (     | (    \/ )   ( | (     | (   ) |  ) (  | (   ) | (    )|')
print('| |     | (___) | |     | |     | |   | | |     | (___) |  | |  | |   | | (____)|')
print('| |     |  ___  | |     | |     | |   | | |     |  ___  |  | |  | |   | |     __)')
print('| |     | (   ) | |     | |     | |   | | |     | (   ) |  | |  | |   | | (\ (   ')
print('| (____/\ )   ( | (____/\ (____/\ (___) | (____/\ )   ( |  | |  | (___) | ) \ \__')
print('(_______//     \(_______(_______(_______|_______//     \|  )_(  (_______)/   \__/')
print('')
																				 
# This function adds two numbers 
def add(x, y):
    return x + y

# This function subtracts two numbers 
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print('')
print("Select operation.")
print('')
print("1.Add\t\t[two numbers]")
print("2.Subtract\t[two numbers]")
print("3.Multiply\t[two numbers]")
print("4.Divide")
print('')

# Take input from the user 
choice = str(input("Enter choice(1/2/3/4):"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print('')
    print "\t" + str(num1) + "+" + str(num2) + "=" + str(add(num1,num2))

elif choice == '2':
    print('')
    print "\t" + str(num1) + "-" + str(num2) + "=" + str(subtract(num1,num2))

elif choice == '3':
    print('')
    print "\t" + str(num1) + "*" + str(num2) + "=" + str(multiply(num1,num2))

elif choice == '4':
    print('')
    print "\t" + str(num1) + "/" + str(num2) + "=" + str(divide(num1,num2))
else:
    print('')
    print("Invalid input")