# value = ('the answer', 42)
# s = str(value)  # convert the tuple to string
# print(s)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
print(f.seek(5))      # Go to the 6th byte in the file
(f.read(1))
print(f.seek(-2, 2))  # Go to the 3rd byte before the end
print(f.read(1))