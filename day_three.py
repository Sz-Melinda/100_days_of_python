
# exercise 1 - odd or even

# Don't change the code below 
number = int(input("Which number do you want to check? "))
# Don't change the code above 

#Write your code below this line 

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#######################################################################################
# exercise 2 - BMI calculator 2.0

# Don't change the code below 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above 

#Write your code below this line 

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")



#######################################################################################
# exercise 3 - leap year

# Don't change the code below 
year = int(input("Which year do you want to check? "))
# Don't change the code above 

#Write your code below this line 

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
            
    else:
        print("Leap year.")

else:
    print("Not leap year.")


#######################################################################################
# exercise 4 - pizza order

# Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above 

#Write your code below this line 

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")


#######################################################################################
# exercise 5 - love calculator

# Don't change the code below 
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above 

#Write your code below this line 

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



#######################################################################################
# day 3 project - treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. \n") 

#Write your code below this line 


choice_one = str(input('''You are standing on the docks, waiting for a boat to take you to the treasure island, but it's taking too long. 
You see the island on the horizon, you could swim there, or you can wait some more. What do you do? (swim or wait) \n'''))

if choice_one.lower() == "swim":

    print("While swimming a shark grabbed you and pulled you down. \n Game Over")

else:
    print("After a while a boat arrived, and took you to the island.")

    choice_two = str(input('''On the island you see two paths, one leading to the dark jungle, the other seems to be leading to a mountain. 
    Where do you go? (jungle or mountain) \n'''))

    if choice_two.lower() == "jungle":
        print("You got lost in the dark dense jungle. \n Game Over")

    else:
        print("You start to make you way up on the mountain path.")

        choice_three = str(input("On your way you come to a crossing of three roads. Which way do you go? (left or midle or right) \n")) 


        if choice_three.lower() == "left":
            print('''You went left, continued to go up. You reached the top of the mountain where you see a treasure chest. 
            You open it and see it's full with gold. \n You Win!''')
            # in games it's always left :D
        elif choice_three.lower() == "middle":
            print("The road ends in a cliff, leading nowhere.\n Game Over!")
        else:
            print("The road leads to a rock wall.\n Game Over!")

