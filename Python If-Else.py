# n = int(input("Enter Number: ").strip())
#
# check = {True: "Not Weird", False: "Weird"}
# print(check[n%2==0 and (n in range(2,6) or n > 20)])
#
# # print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")
#
# n = int(input())
# for i in range(0, n):
#     print(i*i)
#
# n = int(input())
# i=1
# while i<=n:
#     print(i,end="")
#     i=i+1

# a, b, c, n = [int(raw_input()) for _ in xrange(4)]
# print [[x,y,z] for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]

# x, y, z, n = int(input()), int(input()), int(input()), int(input())
# # print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
#
# print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))
#


#
# n = int(input())
# arr = list(map(int, input().split()))
# zes = max(arr)
# i=0
# while(i<n):
#     if zes ==max(arr):
#         arr.remove(max(arr))
#     i+=1
# print(max(arr))

# n = int(input())
# arr = map(int, input().split())
# arr = list(arr)
# x = max(arr)
# y = -9999999
#
# for i in range(0, n):
#     if arr[i] < x and arr[i] > y:
#         y = arr[i]
#
# print(y)
#
# n = int(input())
# arr = map(int, input().split())
# arr = list(arr)
# x= max(arr)
# print (max(arr))
# x.remove()
# print (max(arr))
# # y = -9999999
# #
# for i in range(0,n):
#     if arr[i]<x  : # and arr[i] > y:
#         y = arr[i]

# print(y)
# stud_details = []
# scores = []
# for n in range(int(input())):
#         name = input()
#         score = float(input())
#         stud_details.append([name,score])
#         scores.append([score])
#
# print(stud_details)
# print(sorted((scores))[1])
# second_hight = sorted(list(set(scores)))[1]
# for nam,sco in sorted(stud_details):
#     if sco == second_hight:
#         print(nam)

# marksheet=[]
# scorelist=[]
#
# for n in range(int(input())):
#         name = input()
#         score = float(input())
#         marksheet+=[[name,score]]
#         scorelist+=[score]
# b=sorted(list(set(scorelist)))[1]
#
# for a,c in sorted(marksheet):
#      if c==b:
#             print(a)



# # students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# Student_rercord = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# Marks = [37.21, 37.21, 37.2,41,39]
# # for _ in range(int(input())):
# #     # name = input()
# #     # score = float(input())
# #     # Student_rercord.append([name, score])
# #     Marks.append([score])
#
# Marks = sorted(Marks)[1]
# for name,score in sorted(Student_rercord):
#     if score == Marks:
#         print(name)

marksheet = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#
# if __name__ == '__main__':
#     Student_rercord= []
#     Marks= []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         Student_rercord.append([name,score])
#         Marks.append(score)
#
#     # Marks=sorted(Marks)[1]
#     # for name,score in sorted(Student_rercord):
#     #     if score == Marks:
#     #         print(name)
#
#
#     second_highest = sorted(list(set([marks for name, marks in Student_rercord])))[1]
# #     print('\n'.join([a for a,b in sorted(Student_rercord) if b == second_highest]))
#
# n = int(input())
# A = set(map(int, input().split()))
# N = int(input())
# for _ in range(N):
#     command, args = input().split()
#     B = set(map(int,input().split()))
#     getattr(A, command)(B)
# print(sum(A))


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
# def birthdayCakeCandles(ar):
    # ar = sorted(ar)
# ar_count = int(input())
# ar = list(map(int, input().rstrip().split()))
# # maxCandle= (max(ar))
# # print(maxCandle)
# cnt = 0
# maxCandle = max(ar)
# print(maxCandle)
# for i in ar:
#     print(i)
#     if i == maxCandle:
#         cnt += 1
# print(cnt)


#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     ar_count = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = birthdayCakeCandles(ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
#
# s = input()
# print (s[-2:])
# print (s[:2])
# print (s[2:-2])
# if s[-2:] == "AM" and s[:2] == "12":
#     print("11111""00" + s[2:-2])
# elif s[-2:] == "AM":
#     print("22222",s[:-2])
# elif s[-2:] == "PM" and s[:2] == "12":
#     print("33333",s[:-2])
# else:
#     print("444444",str(int(s[:2]) + 12) + s[2:8])
#
# # 07:05:45PM

# import string
# alpha = string.ascii_lowercase
# n = int(input())
# L = []
# print(alpha)
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     # print(s)
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print(s[::-1])
#     print("oooooooooooooooooooooooo",s[::-1]+s[1:])
#     print("************************",s[1:])
# print('\n'.join(L))
# print('\n'.join(L[:0:-1]))
# print('\n'.join(L[:0:-1]+L))

s = "hello world"
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)
















