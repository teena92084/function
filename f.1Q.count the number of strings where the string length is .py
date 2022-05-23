# def match_word(words):
#     c=0
#     for word in words:
#         if len(word)>1 and word[0]==word[-1]:
#             c=c+1
#     return c   
# print(match_word(['abc', 'xyz', 'aba', '1221']))         


# def math(a):
#     c=0
#     for x in a:
#         if len(x)>1 and x[0]==x[-1]:
#             c=c+1
#     return c
# print(math(['abc', 'xyz', 'aba', '1221']))

# def sum(a):
#     c=0
#     for p in a:
    
#         if p[0]==p[-1]:    
#             c=c+1
#     return c
# print(sum(["appoja","alia","ahina","aaka","123","atina"]))            


# def sum(f,s,t):

#     if f>s and f>t:
#         print(f,"f st is greatr")
#     elif s>f and s>t:
#         print(s,"s is greater")
#     else:
#         print(t,"t is greate") 
    
# f=int(input("enter the fnumbr"))
# s=int(input("enter tne s number"))
# t=int(input("enter the tnumber"))    
# sum(f,s,t)               


# def word(a):
#     c=0
#     # b=[]

#     for i in a:

#         if i[0]==i[-1]:
#             c=c+1
#         return c 

# print(word(["anma","ajina","apiya","123"] ))  


#   
    

# def sum(a):
#     c=0
#     for p in a:
    
#         if p[0]==p[-1]:    
#             c=c+1
#     return c
# print(sum(["appoja","alia","ahina","aaka","123","atina","piya"]))     



# def sum (a):
#     c=0
#     for i in a:
#        if i[0]==i[-1]:
#            c=c+1
#     return c
# print(sum(["annua","apiya","aliya","123","pooa"]))  
# 
# 
# def sum(a):
#     i=0
#     s=0
#     while i<len(a):
#         s=s+a[i]
#         # print(s)
#         i=i+1    
#     print(s)



# a=[1,2,3,4,5]
# sum(a)


def re():
    a=["abcd123"]
    c=0
    i=0
    while i<len(a[0]):
        c=c+1
    # print(a[0][-c])
        i=i+1
    print(a[0][-c])