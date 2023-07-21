
# exercise 1 - data types

# Don't change the code below 
two_digit_number = input("Type a two digit number: ")
# Don't change the code above 

####################################
#Write your code below this line 

digit_one = int(two_digit_number[0])
digit_two = int(two_digit_number[1])

print(digit_one + digit_two)


#######################################################################################
# exercise 2 - BMI calculator

# Don't change the code below 
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above 

#Write your code below this line 

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)


#######################################################################################
# exercise 3 - life in weeks

# Don't change the code below 
age = input("What is your current age? ")
# Don't change the code above 

#Write your code below this line 

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")




#######################################################################################
# day 2 project - tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line 

bill = float(input("What was the total bill?  $"))
tip = int(input("How much tip do you want to give? (10% 15% 20%)  "))
people = int(input("How many people will split the bill?  "))

tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
per_person = total_bill / people
final = round(per_person, 2)

print(f"Each person should pay ${final}")

