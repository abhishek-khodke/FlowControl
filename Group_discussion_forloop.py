#  Control Flow
    #- conditional statements - if, elif, else
    #- iterative statements - for, while
    #- transfer statements - pass, break, continue


    # for loop
# -- iterative statements - iterable - can fetch single single elements
# -- list , tuple, set, frozenset, range, str, bytes, bytearray, dict

# list

# s1 = [100, 200, 300, 400, 500]

# for num in s1:
#     # print(num)            #- print list in different lines
#     print(num, end=", ")    #- print list in same line


# tuple

# t1 = (11, 12, 13, 14, 15, 16, 12, 13, 14)

# for num in t1:
#     print(num, end= ", ")

# set

# s1 = {22, 23, 24, "address", "mobilenumber", 23, 24}

# for elem in s1:
#     print(elem, end= ", ")             # duplicates elements will not be printed


# frozenset

# fs = ({22, 33, 44, 55, "Hello", "How r u", 33, 55, 22})
# for i in fs:
#     print(i, end=",")                      # duplicates elements will not be printed


# range

# r1 = range(22, 99)
# for ran in r1:                            # to print each element of range in different line
#     print(ran)

# for i in range(22, 99, 2):                # to print range directly with step of 2
#     print(i, end=",")


# # string
# st1 = "My name is Python and i am here to help you code"

# for i in st1:
#     # print(i, end="")                        # to get same output in one line 


# bytes

# l1 = [110 , 20, 255, 254]
# bt1 = bytes(l1)

# for i in bt1:
#     print(i)


# bytearray

# l1 = [20, 30, 255, 200]

# ba1 = bytearray(l1)

# for i in ba1:
#     print(ba1)


# dictionary


# d1 = {"1":"10", "2":"20", "3":"30", "4":"40"}

# for dict1 in d1:
#     print(dict1, end=", ")       # will return only keys

# for dict2 in d1.values():
#     print(dict2)                 # will print only values

# for dict3 in d1.items():       
#     print(dict3)                   # print keys and values
 
#-------------------------------------------------------------------------------------------------------------------------------------------------

# for loop session

# s1 = "Python Language Fundamentals"

# for i in s1:
#     # print(i)
#     # print(i, end=",")      # print in same line with comma
#     print(i, end=", ")       # print in same line with comma and space



# s1 = [2, "20", 33, 55, "abcd"]       #-- if list contains string

# for element in s1:
#     print(type(element))                #-- to print type of each element

# for element in s1:
#     if type(element) == str:
#         pass                         #-- use pass if you want to add code later
#     else:
#         pass


# lt1 = [3, 23, "22", 43, "33", "qwerty"]

# for num in lt1:
#     if type(num) == str:                   # using if , else with .format
#         print(num * 2)
#     else:
#         print(f"Square of {num} is {num ** 2}")    # using .format



# Checks

# s2 = [11, 9, "Hello", 45, "World", 65, [1, 2, 3, 4]]

# for i in s2:
#     if type(i) == str:                       # using if ,elif and else with .format
#         print(i * 2)
#     elif type(i) == int:
#         print(i ** 2)
#     else:
#         print(f"{i} is invalid value")

#-----------------------------------------------------------

# Dictionary

# d1 = {"a":"abhay", "b":"brijesh", "c":"caty", "d":"dinesh"}

# for val in d1:             # fetch index
#     print(val)

# for val in d1.values():    # fetch values
#     print(val)

# for val in d1.items():
#     print(val)             # to fetch all the items


# d1 = {"a":"abhay", "b":"brijesh", "c":"caty", "d":"dinesh"}

# counter = 0

# for val in d1.items():       # to fetch all the items 
#     counter += 1             # to calculate for loop rotating value
#     print(counter)
#     print(val)

# print("Finish")


# d1 = {"a":"abhay", "b":"brijesh", "c":"caty", "d":"dinesh"}

# for key, value in d1.items():
#     print(f"key is {key} and value is {value}")      # to fetch key and there value


# d1 = {"a":"abhay", "b":"brijesh", "c":"caty", "d":"dinesh"}

# for key in d1:
#     print(f"key is {key} and value is {d1[key]}")      # to fetch key and value directly by using indexing


#-------------------------------------------------------------

# Range                            # range(start, stop, step)   , stop is excluded

# val = range(0, 22)
# print(list(val))                 # print in list

# val = range(0, 22)
# for i in val:
#     print(i, end=", ")           # using for loop in range


# for val in range(0, 22) :        # direct way to use for loop
#     print(val)


# for val ialn range(0, 22, 2):        # using step in range
#     print(v)

#--------------------------------------------------------------------

# string

# st1 = "Python Language Fundamentals"

# for i in st1:
#     print(i, end="")                 # print string



# st1 = "Python Language Fundamentals"

# import time                            # import time module

# for i in st1:
#     time.sleep(1)                      # for 1 sec delay in each element output
#     print(i)



# st1 = "Python Language Fundamentals"

# #     ##Print Using indexing

# value = range(0, len(st1))                # 0 - 28
# for i in value:
#     print(st1[i], end=", ")    



# value1 = range(0, len(st1))
# for i in value1:
#     if i % 2 == 0:                        # get alternate values
#         print(st1[i], end=", ")


# for i in range(0, len(st1)):
#     if i % 2 == 0:
#         print(st1[i], end=", ")            # use for loop directly


 
# st1 = "Python Language Fundamentals"

# #      # Remove spaces

# # for i in range(0, len(st1)):
# #     if st1[i] != " ":                    # to remove spaces    
# #         print(st1[i], end="")


# for i in st1:
#     if i != " ":
#         print(i, end="")                   # to remove spaces directly
