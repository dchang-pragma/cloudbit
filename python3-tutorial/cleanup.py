# f = open('myfile.txt')
# #for line in open("myfile.txt"):
# for line in f:
#     print(line, end="")
# print(f.closed)
# f.close()
# print(f.closed)


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
    #print(err)
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise