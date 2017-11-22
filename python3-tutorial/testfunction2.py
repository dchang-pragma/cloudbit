def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# print('provide input')
# volInput=input()
# parrot(volInput)
#parrot()                     # required argument missing
parrot(10000,'dead',type='super')
#parrot(voltage=5.0,'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument