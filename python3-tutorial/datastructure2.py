# squares = []
# for x in range(10):
# 	squares.append(x**2) #first way
# print(squares)

#squares = [x**2 for x in range(10)] #second way
# squares = list(map(lambda x: x**2, range(10))) #third way
# print(squares)
#f = lambda x, y : x + y
# def f(x,y):
# 	return x + y

# print(f(1,2))

# def fahrenheit(T):
#     return ((float(9)/5)*T + 32)
# def celsius(T):
#     return (float(5)/9)*(T-32)
# temp = (36.5, 37, 37.5,39)

# F = map(fahrenheit, temp)
# C = map(celsius, F)

# print(fahrenheit(36.5))
# print(celsius(36.5))
#print(map(fahrenheit, temp))
#print (F)
# a = [1,2,3,4]
# b = [17,12,11,10]
# c = [-1,-4,5,9]
# print(map(lambda x,y:x+y, a,b))
# print(list(map(lambda x,y:x+y, a,b)))
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)]) # the tuple must be parenthesized, otherwise an error is raised
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

#from math import pi
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


