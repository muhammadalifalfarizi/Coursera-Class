# Expressions and Variables
# 1
print("2 + 2 = " + str(2 + 2))

# 2
bill = 47.28  # Assign "bill" variable with bill amount
tip = bill * .15  # Multiply by stated tip rate
total = bill + tip  # Sum the "total" of the "bill" and "tip"
share = total / 2  # Divide "total" by number of friends dining
# Enter the required string and "share"
print("Each person needs to pay:" + str(share))
# Hint: Remember to convert incompatible data types

# 3
numerator = 10
denominator = 10
result = numerator / denominator
print(result)

# 4
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(' '.join([eval(str('word'+str(i+1))) for i in range(7)]))
