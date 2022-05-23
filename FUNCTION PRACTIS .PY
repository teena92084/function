# def man(fst,x,y):
#     print("linx",fst)
#     print("linx",x)
#     print("linx",y)
# man("emai","pooja","teena")    




# def duf(a,b,c):
#     d=a+b+c
#     print(d)
#     print(c,b,a)
# duf(2,5,6)    


# def gu(**a):
#     print("jina"+a["teena"])
# gu(teena="seena",pooja="meena")    


# def assin(tina1,tina3,tina2):
#     print("1",tina3)
#     print("2",tina2)
#     print("3",tina1)
# assin(tina1=5,tina2=10,tina3=11)    

# x=lambda a,b:a+b
# print(x(20,10))


# def nested():
#    t="teena kanawar" 
#    print(t)
    
# nested()    
      




# def f1():
#     s="teena"
#     def f2():
#         b="my name is"
#         def f3():
#             print(b)
#         f3()    
#         print(s)  
#     f2()
# f1()            



# def age(n):
#     if n>=18:
#         print("eigible to vote")
#     else:
#         print("not")
# n=int(input("enter the number"))
# age(n)   



# n=int(input("enter the numbr"))
# d=dict()
# for x in range(n,n+1):
#     d[x]=x*x
# print(d)    


# def s(*a):
    
#         print("hello  "+a[1])
# s("pooja","piya","sona","bhulbul","seena") 
# 
#        

# def table():
#     num=int(input("enter the number"))
#     i=1
#     while i<=num:
#         j=1
#         while j<=10:
#             print(i,"x",j,"=",j*i,end=" ")
#             j=j+1
#         print()
#         i=i+1
# table()            



# def sum():
#     n=int(input("enter the number"))
#     if n%2==0:
#         print("yes")
#     else:
#         print("no")    
       
# sum()




# print("kon banega krodpati me")
# print("ye rha apka sawal")
# qu=["Q.1 who is the prime minister of india?",
# "Q.2 which language is used most in maharastra",
# "Q.3 what is the national flower of india?",
# "Q.4 what is the national animal of india?"]
# op=[["nerandear modhi","apj abdul kalam","lal bhadur sastri","ashok ghlod"],
# ["hindi","english","marathi","bangeli"],
# ["rose","lotus","sunflower","hibiscus"],
# ["lion","elephant","dog","tiger"]]
# sol=[1,3,2,4]
# anslist=[
#     ["1.nerandear mode","2.apj abudal klam"],
# ["2.crow","3.peocock"],
# ["1.rose","2.lotus"],
# ["1.lion","4.tiger"]]
# i=0
# count=0
# price=0
# while i<len(qu):
#     print(qu[i])
#     j=i
#     sno=0
#     while (sno<len(op[i])):
#         a=op[j][sno]
#         print(sno+1,a)
#         sno+=1 
#     if count==0:   
#         lifeline=input("do u want lifeline:-yes/no  :")
#         if lifeline=="yes":
#             # print("select your option") 
#         # if count<=0:
#             count=count+1
#             print("select your option")
#             se=0
#             b=i
#             while se<len(anslist[i]):
#                 c=anslist[b][se]
#                 se+=1
#                 print(c)
#             ans=int(input("choose your answer:-")) 
#             if ans==sol[i]:
#                 price+=1000
#                 print("your answer is correct, and your winning price is",price)
#                 print("congraculation")
#                 print("your next que is:")
#             else:
#                 print("your answer is wrong")
#                 print("your next que is:")
#                 break
                 
            
#         else:
            
#             # print("you dont use life line you already use life line")
          

#             ans1=int(input("plz enter your answer"))
#             if ans1==sol[i]:
#                 price+=1000
#                 print("your answer is correct, and your winning price",price) 
#                 print("congraculation")
#             else:
#                 print("your answer is wrong")
#                 print("your next que is")
#                 break
#     else:
#         ans2=int(input("enter your answer:"))
#         if ans2==sol[i]:
#             price+=1000
#             print("your answer is correct and your winning price is",price)   
#         else:
#             print("wrong answer")  
#             break  
#     i+=1




# # def sum(n):
# #     i=1
# #     while i<=n:
# #         j=1
# #         while j<=10:
# #             # print(j,"x",i,"=",j*i)
# #             print(j*i , end="    ")
# #             j=j+1
# #         print()    
# #         i=i+1

# # n=int(input("enter the number"))
# # sum(n)     

# # def sum(st):  
    
# #     i=0
# #     for a in st:
#       if len(a)>1 and a[i]==a[-1]:
          
#         i=i+1
#     print(i)
# print(st=['abc', 'xyz', 'aba', '1221'])    
# sum()



# 4.Write a Python program to reverse a string.
# Sample String : "1234abcd"

# a=["1234abcd"]
# i=0
# c=0
# while i<len(a[0]):
#     c=c+1
#     print(a[0][-c],end="")
#     i=i+1
    








# a=["teena"]
# # i=0
# # c=0
# # while i<len(a[0]):
# #     c=c+1
# #     print(a[0][-c],end='')
# #     i=i+1    


# def unque(a):
#     i=0
#     b=[]
#     for p in a:
#         if a[i] not in b:
#             b.append(a[i])
#         i=i+1
#     print(b)
#     # i=i+1    

# a= ([1,2,3,3,3,3,4,5])
# unque(a)
# Unique List : [1, 2, 3, 4, 5].

# generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
# generate_range(1, 10, 3) # should return list of [1,4,7,10]
# generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
# generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]


# def sum():
#     # a=[]
#     s=int(input("enter the start "))
#     stop=int(input("enter the stop value"))
#     diff=int(input("enter the diifrance"))
#     a=[]
#     for i in range(s,stop,diff):
#         a.append(i)
#         print(a)
# sum()        


# "4", "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.



# def sun(n,n1):
#     v=str(int(n)+int(n1))
#     print(v)
# n=(input("enter the numbr n"))
# n2=(input("enter the number n2 "))
# sun(n,n2)

# def sum(list1):
#     # list1 = [2, -7, 5, -64, -14]
#     i=0
#     c=0
#     c2=0
#     while i<len(list1):
#         if list1[i]>=0:
#             c=c+1
#         else:
#             c2=c2+1
#         i=i+1
#     print(c,c2)
#     # print(c2) 
# list1=[2, -7, 5, -64, -14]               
# sum(list1)

# Output: pos = 2, neg = 3



# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.

# def max_v():
#     a=[4,6,2,1,9,63,-134,566]
#     i=0
#     max=a[i]
#     min=a[i]
#     while i<len(a):
#         if a[i]>max:
#             max=a[i]
#         elif a[i]<min:
#             min=a[i]    
#         i=i+1
#     print(max)
#     print(min)
# max_v()   
# 
# 
#          

# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

# def sr(a):
#     i=0
#     c=[]
#     while i<len(a):
#         v=a[i]%10
#         a[i]=a[i]//10
#         c.append(a[i]+v)
#         i=i+1
#     print(c) 
# a=[12,67,98,34]
# sr(a)       


# def asd(a):
#     i=0
#     b=[]
#     while i<len(a):
#         n=a[i]%10
#         a[i]=a[i]//10
#         b.append(a[i]+n)
#         i=i+1
#     print(b)    
# a=[12, 67, 98, 34] 
# asd(a)   


# 31. Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50.

# def num(a):
#     i=1
#     while i<=10:
#         v=i*a
    
#         print(i,"x",a,"=",v)
#         i=i+1
# a=int(input("enter the number")) 
# num(a)   

# def squre(a):
#     # a=[1,9,9,1]
#     i=0
#     while i<len(a):
#         v=a[i]**2
#         # i=i+1
#         print(v,end="")
#         i=i+1 
# a=[1,9,9,1]       
# # a=int(input("enter the numer"))
# squre(a)



# def table():
#     n=int(input("enter the number"))
#     i=1
#     while i<=n:
#         j=1
#         while j<=10:
#             print(j,"x",i,"=",j*i)
#             j=j+1
#         print()
#         i=i+1
# table()            




# def vu(a): 
#     # a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#     i=0
#     max=0
#     min=1
#     b=[]
#     d=[]
#     c=0
#     c2=0
#     while i<len(a):
#         if max<len(a[i]):
#             max=len(a[i])
#             d=a[i]
#         if min >=len(a[i]):
#             min=len(a[i])
#             b=a[i]
#         i=i+1
#     print(d)
#     print(b)
    
# a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]  
# vu(a)             




# a=[1,23,5,6,4,-7]
# def mu(a):
#     i=1
#     max=a[0]
#     while i<len(a):
#         if a[i]<max:
#             max=a[i]
#         i=i+1
#     print(max) 
# a=[2,23,5,6,4,7]
# mu(a) 


                                                                                                                   
# (-12, 2, -5) -> false
# (45, 1, 6) -> false
# (45, 5, 15) -> true
# (4, 1, 4) -> true
# (15, -5, 3) -> true    


# def du(a,b,c):
#     if a%c==0 and b%c:
#         print("true")
#     else:
#         print("false")
# du(-12, 2,-5)       
# du(-12, 2,6) 
# du(45,1,6) 
# du(45, 5,15)
# du (4, 1,4) 
# du (15, -5,3)        



# def mu(a):
#     i=1
#     max=a[0]
#     while i<len(a):
#         if a[i]<max:
#             max=a[i]
#         i=i+1
#     print(max) 
# a=[2,23,5,6,4,7]
# mu(a) 



# def num(n,n2):
#     v=n**n2
#     print(v)
# n=int(input("enter the wher we start"))
# n2=int(input("enter the stop" )) 
# num(n,n2)   



# a=["44een","04po","98u"]
# i=0
# b=[]

# while i<len(a):
#     s=""
#     j=0
#     while j<2:
#         s=s+a[i][j]
#         j=j+1
#     b.append(s)    
#     i=i+1
# print(b)    


# a=["12","teena","13","piya"]
# i=0
# b=[]
# while i<len(a):
#     if a[i]>="0" and a[i]<="9":
#         b.append(a[i])
#     i=i+1
# print(b)    

# a=[12,"teena",13,"pooja"]
# b=a[0]
# # a[0]="pooja"
# # a[3]="12"
# # print(a)
# a[0]=a[len(a)-1]
# a[len(a)-1]=b
# print(a)



# def re(a):
    
#     i=0
#     b=[]
#     while i<len(a[0]):
#         c=c+1
#         print(a[0][-c],end="")
#         i=i+1
# a=["abcd123"]        
# re(a)        
    

# def du(x=1,y=2):
#     x=x+1
#     y=y+1
#     print(x,y)
# du(y=2,x=1)    


# i=0
# a=[]
# b=[]
# while i<=30:
#     if i>=1 and i<=5:
#         a.append(i*i)
#     elif i>=26 and i<=30:
#         b.append(i*i)


#     i=i+1
# print(a,",",b)  
              
# def sum(n):
#     i=0
#     min=n[0]
#     while i<len(n):
#         if n[i]<min:
#             min=n[i]
#         i=i+1
#     print(min)        


# n=[1,3,5,7,8,0]
# sum(n)


# def sum(a,b):
#     v=str(int(a)+int(b))
#     print(v)
#     print(type(v))
# # a=int(input("enterr the numbe"))
# # b=int(input("enterr the numbe"))
# sum("4","5")





# def sum():

#     st=int(input("enter strt va"))
#     stop=int(input("ente stop"))
#     diff=int(input("enter the diif"))
    
#     b=[]
#     for i in range(st,stop,diff):
#         b.append(i)
#     print(b) 
# sum()       


# def sum():
    
#     a=["i am anjali"]
#     for i in a:
#         b=i.split()
        
#     print(b)
# sum()        

# a=[12,34,"pooja"]
# b=a.index(12)
# print(b)


# f= open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())



# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - delhi
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - jaipur