# def delete_nth(order, max_e):
#     # print(type(order))
        
#     if type(order) == list and type(max_e) == int:

#         myList = []

#         for i in range(0, len(order)):
#             if myList.count(order[i]) < max_e:
#                 myList.append(order[i]) 
#         print(myList)
#     else:
#         print("please submit a list and integer")

# delete_nth([1,2,3,1,2,1,2,3], 2)

# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

# def newList(list):

#     my_list = []
#     i= 0
#     while i < len(list):
#         if list[i] < 10:
#             my_list.append(list[i])

#         else:
#             pass

#         i+=1

#     print(my_list)

# newList([1,11,14,5,8,9])

# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method
# l_1 = [1,2,3,4,5,6]
# l_2 = [3,4,5,6,7,8,10]


# def listCombine(list1, list2):

#     aList = list1 + list2
#     aList.sort()

#     print(aList)

# listCombine([1,2,3,4,5,6], [3,4,5,6,7,8,10])
