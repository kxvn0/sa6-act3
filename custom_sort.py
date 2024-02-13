strings = ['apple', 'tree', 'car', 'banana', 'people', 'cat']

sorted_strings = sorted(strings, key = lambda x: (len(x), x))

print(sorted_strings)

abc = ['a', 'ab', 'abc', 'dark', 'car']
sorted_abc = sorted(abc, key = lambda x: (len (x), x))
print(sorted_abc)
