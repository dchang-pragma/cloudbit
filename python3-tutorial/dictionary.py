tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))

teldic=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(teldic)
teldic2=dict(sape=4139, guido=4127, jack=4098)
print(teldic2)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}?  It is {1}.'.format(q, a))