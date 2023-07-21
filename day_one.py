
# exercise 1 - printing

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#######################################################################################
# exercise 2 - debugging practice

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#######################################################################################
# exercise 3 - input function

name = input("What is your name? " )
print(len(name))

#######################################################################################
# exercise 4 - variables

# Don't change the code below 
a = input("a: ")
b = input("b: ")
# Don't change the code above 

####################################
#Write your code below this line 

c = a
a = b
b = c

#Write your code above this line 
####################################

# Don't change the code below 
print("a: " + a)
print("b: " + b)


#######################################################################################
# day 1 project - band name generator

print("Band name generator")
city = input("What's the city you grew up in? \n")
pet = input("What's your favorite animal? \n")
print(f"Your band name could be {city} {pet}")

