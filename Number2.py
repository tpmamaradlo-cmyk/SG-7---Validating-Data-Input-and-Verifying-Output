#Trams P. Mamaradlo
#8-Camia


#Input
username = input("Enter username: ")

#Check correct length
correct_length = 5 <= len(username) <= 10

alphanumeric_only = username.isalnum()
if correct_length and alphanumeric_only:
    print("Valid username")

else:
    print("Invalid username. ")





