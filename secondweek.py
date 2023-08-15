# if
def iffunction():
    
    age = int(input("Enter age: "))
    if age>=30:
        print("You have enough experience. ")
    else:
        print("Gain some experience first. ")

# for
def forfunction():
    numbers = [1,2,3,4,5]
    for number in numbers:
        print(number)

# while
    number
def whilefunction(number):
    while input() != "exit":
        print("hello {}".format(number))
        number = number + 1

# is it a leap year
def leapyearfunction():
    year = int(input("Enter year: "))
    leapcheck = year%4
    if year%4 == 0:
        print("leap year")
    else:
        print("{} not a leap year and this is leap `{}".format(year,leapcheck))
        leapyearfunction()

leapyearfunction()