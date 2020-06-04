

# name = "arpita546468"

# print(name[12])  #it gives error

# length of string


# print(len(name))


# string is immutable


# lis=[1,2,3,4]

# lis[2]=5

# name[3] = 'k' #it gives error
# print(name)


# string concatenate


# first_name = "vaibhav"
# second_name ="dhingra"

# full_name = first_name + " " + second_name

# # print(full_name)
# print(len(full_name))


# string slicing

# name = "pikachu"

# print(name[2:5])

# print(name[:5])

# print(name[2:])

# print(name[-1])

# print(name[-3:-1])

# print((name[-1:-3]))
# print(type(name[-1:-3]))


# lis=[2,5,6,8,9]

# print(len(lis))

# name = "pikachu"

# print(name[2:12])

# print(name[-1:5])

# print(name[5:-1])





# name = "pikachu"


# index=name.find('kaa')

# print(index)


# -----------------class doubt YASHWANT

name = "sushant sharma"
index=0
global_index=0
lis=[]
while(global_index<len(name)):
    index=name[global_index:len(name)].find('s')
    if(index==-1):
        break
    else:
        lis.append(global_index+index)
        global_index=global_index+index+2
print(lis)

# print(name[:].find('s'))

# --------------------------------


# upper lower


# name = "harleen singh"
# name = name.upper()
# print(name)


# name = "AVINASH MISHRA"

# name = name.lower()
# print(name)


# char = 'ABX'

# print(char.islower())


# print(char.isupper())








