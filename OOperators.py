#Assignment Operators:
print("#"*20)
x = 10
x += 1 # or x = x + 1
print(x) # 11
# += -= *= /= //= **= %=

print("#"*20)
#Identity operators -> id() equals id() -> True or False
a=b=20
print(id(a))
print(id(b))
print( a is b)
print( a is  not x)

print("#"*20)
# Membership operators in not in
s = "Hello World!"
print("H" in s) # found = "H" in s; print(found)
print("Z" in s)
