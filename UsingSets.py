odd = set ((1, 3, 5, 7, 9))
even = set((2, 4, 6, 8, 10))
prime = set ((1, 3, 5, 7))

#3a)
print(odd.union(even))

#3b)
print(even.union(prime))

#3c)
print(odd.symmetric_difference(prime))

#3d)
print(odd.issubset(prime))

#3e)
print(prime.issubset(odd))

#3f)
print(odd.intersection(prime))

#4a)
print (odd.intersection(prime))

#4b)
print (odd.issuperset(prime))

#4c)
a = even
a.add(12)
print (a)