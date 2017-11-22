matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# matrix2 = [[row[i] for row in matrix] for i in range(4)]
# #print([[row[i] for row in matrix] for i in range(4)])
# print(matrix2)

# transposed = []
# for i in range(4):
# 	transposed.append([row[i] for row in matrix])

# print(transposed)

# print(list(zip(*matrix)))

t = 12345, 54321, 'hello!',
s = 1,
print(len(s))

basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(basket)
print('orange' in basket )

a = set('abracadabra')
b = set('alacazam')
print(a)# unique letters in a

print(a - b)    # letters in a but not in b
print(a | b)    # letters in a or b or both
print(a & b)    # letters in both a and b
print(a ^ b)    # letters in a or b but not both
c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)