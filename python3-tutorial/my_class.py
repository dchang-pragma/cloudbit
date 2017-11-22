class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

# print(x.f())
# print(x.i)

xf = x.f
for j in range(5):
    print(xf())