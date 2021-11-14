# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# years_left = 90 - int(age)
# x = years_left * 365
# y = years_left * 52
# z = years_left * 12

# print(f"You have {x} days, {y} weeks, and {z} years left.")

# Teacher's solution
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remainig = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remainig} months left."
print(message)



