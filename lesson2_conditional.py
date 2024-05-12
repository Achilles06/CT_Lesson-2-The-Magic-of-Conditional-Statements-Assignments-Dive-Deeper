# 1. Decisions at the Crossroad
# Task 1: Code Correction

number = int(input("Enter a number:"))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")

#2. The Greatest Showdown
number_1 = int(input("Enter number one:"))
number_2 = int(input("Enter number two:"))
number_3 = int(input("Enter number three:"))

greatest_number = 0
least_number = 0

if number_1 >= number_2 and number_1 >= number_3:
    greatest_number = number_1
elif number_2 >= number_1 and number_2 >= number_3:
    greatest_number = number_2
else: greatest_number = number_3

print(greatest_number)

if number_1 <= number_2 and number_1 <= number_3:
    least_number = number_1
elif number_2 <= number_1 and number_2 <= number_3:
        least_number = number_2
else: least_number = number_3

print(least_number)



print("The smallest number is", least_number,". The largest number is ", greatest_number,".")

if number_1 == number_2 and number_1 == number_3:
    count_number = number_1
    count = 3
    print("There are three numbers equal to each other.")
elif number_2 == number_3:
    count_number = 2
    count = 2
    print("There are two numbers equal to each other.")
elif number_1 == number_3:
        count_number = number_1
        count = 2
        print("There are two numbers equal to each other.")


#Leap Year Explorer
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()












