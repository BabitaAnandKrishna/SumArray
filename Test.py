numbers = [4, 5, 6, 9, 11]
sum = 0
for n in numbers:
    sum += n
print("Sum is now", sum)

sum = 0
for n in [1,2,3]:
    sum += n
print(sum)

print = 12
# HackerRanck _Day9
# n, Enter number of record you need to insert in dict
n = int(input())
d = dict()

# enter name and number by separate space
for i in range(0, n):
    name, number = input().split()
    d[name] = number
# print(d)      #print dict, if needed

# enter name in order to get phone number
for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break