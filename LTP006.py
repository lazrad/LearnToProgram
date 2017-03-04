# If age is 5 Go to Kindergarten
# Ages 6 throught 17 goes to grades 1 throught 12
# If age is greater then 17 say go to college
# Try to complete with 10 or less lines

# Ask for the age
age = eval(input('Enter age: '))


# Handle if age < 5
if age < 5:
    print("You're a kid! ")
elif age == 5:
    print("You should be going to kindergarten.")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("You should be going to grade {}!".format(grade))
elif age > 17:
    print("You should be going to college!")


# Special output just for age 5


# Since a number is the result for  ages 6 - 17 we can check them  all with 1 condition

# Handle everyone else