#  Create a simple program that takes user input for their name and age,
# and then outputs a greeting message along with their age after 10 years

name = input("Enter your name ")
age = int(input("Enter your age "))
print('Hello Mr. {}! Your age after 10 years will be {}.'.format(name, age+10))
