# Q37. Consider an array/list of sheep where some sheep may be missing from their place. We
# need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True, True, True, False,
# True, True, True, True ,
# True, False, True, False,
# True, False, False, True ,
# True, True, True, True ,
# False, False, True, True]
# # The correct answer would be 17.Hint: Don't forget to check for bad values like null/

# def sheep(a):

#     i=0
#     c=0
#     while i<len(a):
#         if a[i]==True:
#             c=c+1
#         i=i+1        
#     print(c)

# a=[ True, True, True, False,
#         True, True, True, True ,
#         True, False, True, False,
#         True, False, False, True ,
#         True, True, True, True ,
#         False, False, True, True]
# sheep(a)