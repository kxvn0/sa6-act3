def power_raise(numbers, num):
    powered_num = list(map(lambda x: x** num, numbers))
    return powered_num

numbers = [1, 3, 5, 7, 9]
n = 2
print(power_raise(numbers, n))

x = [2, 4, 6, 8, 10]
print(power_raise(x, n))

