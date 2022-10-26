# Creating Tuple
t1 = 10, # Singlton Tuple, REMEMBER ,
t2 = 10,20,30 # OR t2 = (10,20,30)
t3 = tuple(range(0,25,2))

print(type(t1))
print(type(t2))
print(type(t3))

print(t2)
print(t3[5])
print(t3[-5])

#ERROR t3[2] = 0
print(t3[2:5])
print(t3.index(8))
print(t3.count(8))
print(len(t3))
print(sum(t3))
print(min(t3))
print(max(t3))

