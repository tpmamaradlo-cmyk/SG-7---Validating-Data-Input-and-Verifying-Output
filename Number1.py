#Getting user input
age = int(input("Enter your age: "))
#Selection
try:
    if 12 <= age <= 18 :
        print("Valid age.")
    else:
        print("Invalid age.")

except ValueError:
    print("Invalid input, Please enter an integer")