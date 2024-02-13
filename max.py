def find_max(numbers, compare):
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers[1:]:
        if compare(num) > compare(max_number):
            max_number = num
    return max_number
    

numbers = [255, 4, 9, 27, 36]
lamb = lambda x: x
max_number = find_max(numbers, lamb)
print(max_number)

