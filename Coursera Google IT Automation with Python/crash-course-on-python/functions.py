# example 1
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# example 2


def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is " + str(sum))

# Quiz 1
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(2*my_trip_km))

# Quiz 2

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

# Quiz 3

def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)
