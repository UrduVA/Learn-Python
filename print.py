print("Hello World!")
print()
num1 = 100
num2 = 200
print(num1 + num2)
print("The addition of ",num1," and ",num2, " is ",num1 + num2)

print("The Addition of {} and {} is {}".format(num1,num2,num1+num2))
print("The Addition of {0} and {1} is {2}".format(num1,num2,num1+num2))
print("The value of {x} and {y}".format(x=50,y=25))
print("The value of {x} and {y}".format(x=num1,y=num2))

add = num1 + num2
print(f"The Addition of {num1} and {num2} is {add}") # f-string

print(15,5,2022,sep=" / ")
print(15,5,2022,sep=" @ ")
print("Hello World"+" Hello Universe",end='')
