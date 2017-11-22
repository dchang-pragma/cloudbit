import math
#An optional ':' and format specifier can follow the field name. This allows greater control over how the value is formatted. The following example rounds Pi to three places after the decimal.
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
# old string formatting. The % operator can also be used for string formatting. It interprets the left argument much like a sprintf()-style format string to be applied to the right argument, and returns the string resulting from this formatting operation.
print('The value of PI is approximately %5.3f.' % math.pi)



#Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making tables pretty.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
     print('{0:10} ==> {1:10d}'.format(name, phone))


#If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

#This could also be done by passing the table as keyword arguments with the ‘**’ notation.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


