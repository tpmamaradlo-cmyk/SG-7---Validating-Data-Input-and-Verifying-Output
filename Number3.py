#Number 3

#Valid Grade Levels
glist=[7,8,9,10,11,12]
#Get Grade Level
glevel=int(input("Enter your grade level: "))
#Output if Valid or Invalid Gradelevel
if glevel in glist:
    print("Valid grade level.")
else:
    print("Invalid grade level.")