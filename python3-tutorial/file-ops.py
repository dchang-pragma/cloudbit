#f = open('workfile', 'w')


with open('/Users/bunmaster/python/aws/testfile','r+') as f:
	#read_data = f.read()
	#print(f.closed)
	f.write('this is a test\n')
	#print(f.readline())
	for line in f:
	 	print('print here',line, end='')

print(f.closed)