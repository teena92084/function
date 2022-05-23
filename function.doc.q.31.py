# 31. Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50.


# def table():
#     x=int(input("enter the number"))
#     y=int(input("enter the number")) 
#     i=0
#     s=0
#     while i<= y:
#         s=s+x
#         i=i+1
#         print(s,"x",i,"=",s)
# # x=int(input("enter the number"))
# # y=int(input("enter the number")) 
# table() 
# table()


      
# def table():
#     num=5
#     for i in range(1,11):
#         print(num,"x",i,"=" ,num*i)
# table()



# def num(a):
#     i=1
#     while i<=10:
#         v=i*a
    
#         print(i,"x",a,"=",v)
#         i=i+1
# a=int(input("enter the number")) 
# num(a)   

def sum():
    a=["anca","aiprkra","apoa",123]
    c=0
    for i in a:
        if i[0]==i[-1]:
            c=c+1
        print(c,end="")        
sum()

