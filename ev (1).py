entered_std=set()
rejected_std=set()
n=int(input("enter the attempts "))
for i in range (n):
    name =input("enter your name")

    if name in entered_std:
        print (name,"enter rejected.already entered" )
        rejected_std.add(name)
    else:
        print(name,"entry allowed")
        entered_std.add(name)
print("--entered tracker --")
print("--total entered --")
for name in entered_std:
    print(name,"entered names :")
for name in rejected_std:
    print(name,"rejected name")



