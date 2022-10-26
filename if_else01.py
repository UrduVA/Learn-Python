print("Start")
age = int(input("Enter your age: ") )
if age >= 18:
    # True | if block-clause
    print("Congrats, You are eligible to vote")
else:
    # False | else block-clause
    age = 18 - age
    print(f"You can apply after {age} years")
print("Bye")
