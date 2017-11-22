# refences - https://en.wikiversity.org/wiki/Python_Programming/Tuples_and_Sets#Data_Types
for element in [1, 2, 3]: #list; mutable; Example: Your many cats' names.
    print(element)
for element in (1, 2, 3): #tuple; immutable; Example: the names of the months of the year.
    print(element)
for key in {'one':1, 'two':2}: #dictionary; key and value; example - telephone book
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')



def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


sum(i*i for i in range(10))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product


# from math import pi, sin
# sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

# unique_words = set(word  for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
