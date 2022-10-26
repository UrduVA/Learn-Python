def add(num1,num2): # Positional
    print(f"Addition of {num1} and {num2} is {num1+num2}")

add(10,20)
add(10.25,20.50)
#********************************************#
print("*"*20)
def add(num1=100,num2=200): # Defualt
    print(f"Addition of {num1} and {num2} is {num1+num2}")

add() 
add(10,20)
add(10)
add(num2=10,num1=20) # Keyword
add(10,num2=10)
#********************************************#
def add(*num): # arbitary parameter | variable lenght
    sum = 0
    for i in num:
       sum += i
    print(sum)

add()
add(10)
add(10,20,30)
