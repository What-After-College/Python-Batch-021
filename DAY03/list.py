
 # list is almost like array



#  list is a collection objects


# x=[4, 5, 6, 8, "neeraj", True]

# # type()


# print(type(x))


# use of .split()

# n = "4 8 7 9"


# [4,8,7,9]

# l = n.split()

# print(l)



# st = "my-name-is-sushant"  #'my-', "ame-is-susha", "t"

# # n = st.split('-')
# n = st.split('n')

# print(n)



# student1=85
# student2=80
# student3=85
# student4=85
# student5=85
# student6=85
# student7=85


# lis = [4, 'neeraj', True, [4,'s', 2.0 ,False,[1]]]


# print(lis[3][4])


# update in list

# lis = [4, 'neeraj', True, [4,'s', 2.0 ,False,[1]]]

# print(lis)

# lis[1] = 'vaibhav'

# print(lis)



# delete element



# lis = [4, 'neeraj', True, [4,'s', 2.0 ,False,[1]]]

# print(lis)

# del(lis[2])

# print(lis)

# add in list


# lis = [4, 'neeraj', True, [4,'s', 2.0 ,False,[1]]]

# print(lis)

# lis[3][4].append(['vaibhav', 'anjali', 'arpita', 'avinash'])

# # lis.append('ranjan')

# print(lis)


# lis = [4, 5, 6, 7]

# print(lis[-3])


# ______list slicing_______


# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis[3:])



# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis[:3])




# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis[:])


# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis[-3:-1])




# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis[-1:-3])


# lis=[1, 4, 5, 8 ,9 ,10, 15]

# print(lis)

# lis=[]
# for i in range(4):
#     n=input()
#     lis.append(n)
# print(lis)



# functions 

# def is_even(n):
#     if (n%2)==0:
#         return True
#     else:
#         return False


# m = int(input())
# print(is_even(4))


# def f_to_c(f):
#     return (f - 32)*(5/9)


# f = int(input())
# c = f_to_c(f)
# print(c)

# def add(s1, s2):
#     print(str(s1+s2))


# print(type(add(5, 6)))




# lis = [4,5,6,7,8,9,10,1]
# print(sum(lis))
# lis.sort()
# print(lis)


# import math

# print(math.ceil(5.6))
# print(math.floor(5.62))


lis=[2,5,6,4,7,8]
lis.append([1,2,3,4])
print(lis)
