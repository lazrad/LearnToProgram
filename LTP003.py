# Problem: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers 

# Ask the user to input the number of miles and assign it to the miles variable
miles = input("Enter the number of miles you wish to convert: ")



# Convert from string to integer
miles = int(miles)


# Perform caclulation by multiplying 1.60934

kilometers = miles * 1.60934

# Print the result to the screen

#print(miles, "miles equals", kilometers, "kilometers")
print("{} miles equals {} kilometers".format(miles, kilometers))