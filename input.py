num = input("Enter a Value: ")
print(num)
print(type(num))
num_int = int(num) #num = int(num)
print(num_int)
print(type(num_int))

num2 = int(input("Enter a value : "))
print(num_int + num2)

print("You Typed: ",input("Enter a msg: "))

print(num+num2)

##Enter a Value: 10
##10
##<class 'str'>
##10
##<class 'int'>
##Enter a value : 20
##30
##Enter a msg: Hello
##You Typed:  Hello
##Traceback (most recent call last):
##  File "E:\Udemy\input.py", line 13, in <module>
##    print(num+num2)
##TypeError: can only concatenate str (not "int") to str


