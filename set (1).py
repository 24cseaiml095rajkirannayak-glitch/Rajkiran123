# a=set()
# b=set()
# n=int(input("enter the number of student:"))
# for i in range(n):
#     name=input("enter the name of the student:")
#     if name in a:
#         b.add(name)
#         print(name, "is FAKE (already exists)")
#     else:
#         a.add(name)
#         print(name, "is REAL (added successfully)")

# print("\nReal students:", a)
# print("Fake students:", b)


def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total         #<
    

print(sum_of_list([1,2,3,4,5]))
