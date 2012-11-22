x = 1
print(x) # OUTPUT: 1

def f():
    x = 3
    print(x)

f() # OUTPUT: 3(f shadows x, so print(x) refers to the value 3)
print(x) # OUTPUT: 1 (the global x isn't affected by f)

def g():
    print(x)

g() # OUTPUT: (g doesn't shadow x, so print(x) uses the global x)
