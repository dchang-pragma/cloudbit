import os # The os module provides dozens of functions for interacting with the operating system
import shutil # For daily file and directory management tasks, the shutil module provides a higher level interface that is easier to use
import glob # The glob module provides a function for making file lists from directory wildcard searches:
import re # regular expression
#dir()
#rint(os.getcwd())      # Return the current working directory
#os.system('mkdir -p today/executables')   # Run the command mkdir in the system shell
#os.chdir('./today')   # Change current working directory
#print(dir(os))
#help(os)



#shutil.copyfile('data.db', 'archive.db')
#shutil.move('/Users/bunmaster/python/aws/today/executables', './today/archive')

#print(glob.glob('*.py')) # create a list of python file

# regular expression
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# import math
# print(math.tan(math.pi / 4))
# print(math.log(1024, 2))

# import random
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.choice(range(100)))
# print(random.sample(range(100), 10))  # sampling without replacemnt
# print(random.random())    # random float
# print(random.randrange(6))    # random integer chosen from range(6)

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data)) #平均值
# print(statistics.median(data)) #中位數
# print(statistics.variance(data))

# dates are easily constructed and formatted
# from datetime import date
# now = date.today()
# print(now)

# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


# dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

# data compression
# import zlib
# s = b'witch which has which witches wrist watch'
# print(s, len(s))
# t = zlib.compress(s)
# print(t, len(t))
# zlib.decompress(t)
# zlib.crc32(s)

# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# In contrast to timeit’s fine level of granularity, the profile and pstats modules provide tools for identifying time critical sections in larger blocks of code.


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest # The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings.
print(doctest.testmod())   # automatically validate the embedded tests 

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

print(unittest.main())  # Calling from the command line invokes all tests







