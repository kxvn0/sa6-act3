sum_of_digits = lambda x: sum(int(y) for y in str(x))

number = 78912
result = sum_of_digits(number)

print(result)
