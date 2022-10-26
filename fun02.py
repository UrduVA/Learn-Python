# Return
def add(a,b):
    return a+b,a*b
x = 10
y = 20
c = add(x,y)
print(c)

d,e = add(x,y) # tuple unpacking
print(d)
print(e)

#lambda arg : exp
add = lambda x,y:x+y
add(50,20)
