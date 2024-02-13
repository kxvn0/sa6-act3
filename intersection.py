def _find_inter(l1, l2):
    intersection = list(filter(lambda x: x in l2, l1))
    return intersection

l1 = [2, 4, 6, 8]
l2 = [6, 8, 10, 12]
print(_find_inter(l1, l2))


l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l4 = [3, 6, 9, 12, 15]
print(_find_inter(l3, l4))

