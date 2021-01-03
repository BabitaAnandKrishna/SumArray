#
# import os
# import sys
#
# def simpleArraySum(ar):
#     sum=0;
#     for i in range(len(ar)):
#         sum+=ar[i]
#     return (sum)
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ar_count = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = simpleArraySum(ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# !/bin/python3

import os
import sys


#
# Complete the simpleArraySum function below.
#
# def simpleArraySum(ar):
#     #
#     # Write your code here.
#     sum = 0;
#     for i in range(len(ar)):
#         sum += ar[i]
#     return (sum)
#     #
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ar_count = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = simpleArraySum(ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

# arr = int(input("Enter arr range"))
# sum = []
# for i in range(len(arr) - 2):
#     for j in range(len(arr) - 2):
#         sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] +
#                    arr[i + 2][j + 2])
#
# print(max(sum))

sentance = "Coding IS Awesome"
s= ""
for i in sentance.split(' '):
    s+=i[::-1]+' '

print(s[-2::-1].swapcase())