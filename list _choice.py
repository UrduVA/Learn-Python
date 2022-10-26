county = ['in','uk','us','sa','jp']
c = ['Rs','pnd','$','ryl','jpp']
index = 0
while True:
    choice = input("Enter county code: or q to quit: ")
    if choice == "q" : break
    if choice not in county:
        print("Invalid Choice")
        continue
    index = county.index(choice)
    print(c[index])
