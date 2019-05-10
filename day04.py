# sum = 0
#
# for x in range(101):
#     sum += x
# print(sum)

#-------------------------------------

# sum1 = 0
# for y in range(0,101,2):
#     sum1 += y
# print(sum1)

#-------------------------------------

# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

#-------------------------------------

# sum = 0
#
# for x in range(1,101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

#-------------------------------------

# from random import randint
#
# num = randint(1,101)
# counter = 0
#
# while(True):
#     called = int(input("Please enter a number: "))
#     counter += 1
#     if(called > num):
#         print("Smaller than your num!")
#     elif(called == num):
#         print("Cool!")
#         break
#     else:
#         print("Bigger than your num!")

#-------------------------------------

# for i in range(1,10):
#     for j in range(1,10):
#         print("%d x %d = %d " % (i,j,i*j))
#     print('\n')

#-------------------------------------

# from math import sqrt
#
# temp = int(input("Please enter a number: "))
#
# #for x in range(2,temp):
# for x in range(2, int(sqrt(temp)+1)):
#
#     if(temp % x == 0):
#         print("Not a Prime number!")
#         break
#     else:
#         print("Prime number!")
#         break

#-------------------------------------