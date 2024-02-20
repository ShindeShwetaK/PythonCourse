#!/usr/bin/env python
# coding: utf-8

# # Variables 

# In[1]:


x=3


# In[209]:


get_ipython().run_line_magic('whos', '')


# In[3]:


print(type(x))


# In[4]:


x=5.7


# In[5]:


get_ipython().run_line_magic('whos', '')


# In[6]:


print(type(x))


# In[7]:


abcd = 555.36


# In[9]:


get_ipython().run_line_magic('whos', '')


# In[11]:


a,b,c,d,f=3,5,6,-7,0.9


# In[12]:


get_ipython().run_line_magic('whos', '')


# In[13]:


del abcd


# In[15]:


print(abcd)


# In[18]:


c=5+6j


# In[19]:


print(type(c))


# In[20]:


s='hello'


# In[21]:


print(type(s))


# In[22]:


a=-5


# In[23]:


print(a)


# In[25]:


print(b%a)


# In[26]:


print(b)


# In[27]:


s='hello'


# In[28]:


u='world'


# In[29]:


print(s+u)


# # Operators

# In[30]:


get_ipython().run_line_magic('whos', '')


# In[31]:


a


# In[32]:


3x=5


# In[33]:


@=0


# In[34]:


get_ipython().system('c=9')


# In[35]:


get_ipython().system('v=9')


# In[36]:


get_ipython().system('2x=9')


# In[1]:


34/9


# In[2]:


34//9


# In[3]:


10/9


# In[4]:


10//9


# In[5]:


2^2


# In[6]:


2**2


# In[7]:


x=input("enter a number:")


# In[8]:


type(x)


# In[9]:


print(x)


# In[10]:


x=int(x)


# In[11]:


type(x)


# In[12]:


get_ipython().run_line_magic('pinfo', 'pow')


# In[13]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if b>a:
    print a
    print "I m inside if"


# In[14]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if b>a:
    print (a)
    print ("I m inside if")
print("I m outside If")


# In[15]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if b>a:
    print (a)
    print ("I m inside if")
print("I m outside If")


# In[17]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
if b>a:
    print (b)
    print ("B is greater I m inside if2")
print("I m outside")


# In[19]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
if b>a:
    print (b)
    print ("B is greater I m inside if2")
print("I m outside")


# In[20]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
if b>a:
    print (b)
    print ("B is greater I m inside if2")
print("I m outside")


# In[25]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[26]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[27]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[29]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
elif a == b:
    print("Both the numbers are equal i m inside elif")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[30]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
elif a == b:
    print("Both the numbers are equal i m inside elif")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[31]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
elif a == b:
    print("Both the numbers are equal i m inside elif")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[32]:


a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
if a>b:
    print (a)
    print ("A is greater I m inside if1")
elif a == b:
    print("Both the numbers are equal i m inside elif")
else:
    print (b)
    print ("B is greater I m inside else")
print("I m outside")


# In[33]:


a= 9
b=10
print("A") if a>b else print("=") if a==b else print("B")


# In[34]:


a= 100
b=50
print("A") if a>b else print("=") if a==b else print("B")


# In[35]:


a= 100
b=100
print("A") if a>b else print("=") if a==b else print("B")


# In[36]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[37]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[38]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[39]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[40]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[41]:


a=int(input("Enter Your Marks:"))
if a>=85:
    print("You have A+ Grade")
elif (a<85) and (a>=80):
    print("You have A Grade")
elif a<80 and a>=75:
     print("You have B+ Grade")
elif a<75 and a>=70:
    print("You have B Grade")
else:
    print("Below Avg")


# In[43]:


a=3
if a>10:
    print("a>10")
elif not(a>10):
    print("a<10 else part")


# In[44]:


a=10
if a>10:
    print("a>10")
elif not(a>10):
    print("a<10 else part")


# In[45]:


a=100
if a>10:
    print("a>10")
elif not(a>10):
    print("a<10 else part")


# In[46]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    else:
        print("but not greater then 20.")
else:
    print("Number less then 10 ")


# In[47]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    else:
        print("but not greater then 20.")
else:
    print("Number less then 10 ")


# In[48]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    else:
        print("but not greater then 20.")
else:
    print("Number less then 10 ")


# In[49]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[50]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[51]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("and also greater then 20.")
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[52]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("also greater then 20.")
        if x>30:
            print("and 30")
        elif x==30:
             print("and equal 30")
        else:
            print("but less the 30")      
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[53]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("also greater then 20.")
        if x>30:
            print("and 30")
        elif x==30:
             print("and equal 30")
        else:
            print("but less the 30")      
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[54]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("also greater then 20.")
        if x>30:
            print("and 30")
        elif x==30:
             print("and equal 30")
        else:
            print("but less the 30")      
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")


# In[60]:


x=int(input("Enter Number:-"))
if x>10:
    print("Number >10,")
    if x>20:
        print("also greater then 20.")
        if x>30:
            print("and 30")
        elif x==30:
             print("and equal 30")
        else:
            print("but less the 30")      
    elif x==20:
        print("and also equal to 20.")        
    else:
        print("but not greater then 20.")
elif x==10:
    print("Number is equal to 10")
else:
    print("Number less then 10 ")
print("Bye")


# In[1]:


#single line comment
"""
Multiline 
comment
"""


# In[4]:


"""
User will enter a floating point number 
lets say 238.915 your task is to find out the 
interger portion before the decimal in this case 238
and then chcek weather if that interger potion is odd or even?
"""
x=float(input('Enter a floating point number:-'))
roundx= round(x)
print(roundx)
if roundx>x:
    intportion=roundx-1
    print("The number you entered:-",x)
    print('The integer portion:-',intportion)
elif x==y:
     print("The number you entered:-",x)
     print('The integer portion:-',intportion)
    
print('bye')
    
    
    
    


# In[7]:


x=float(input('Enter a floating point number:-'))
roundx= round(x)
print(roundx)
if roundx>x:
    intportion=roundx-1
    print("The number you entered:-",x)
    print('The integer portion:-',intportion)
else:
     print("The integer portion:-",roundx)
    
print('bye')


# In[8]:


x=float(input('Enter a floating point number:-'))
roundx= round(x)
print(roundx)
if roundx>x:
    intportion=roundx-1
    print("The number you entered:-",x)
    print('The integer portion:-',intportion)
else:
     print("The integer portion:-",roundx)
    
print('bye')


# In[31]:


x=float(input('Enter a floating point number:-'))
roundx= round(x)
print(roundx)
if x>0:
    if roundx>x:
        intportion=roundx-1
        print("The number you entered is positive:-",x)
        print('The integer portion:-',intportion)
    else:
        intportion=roundx
        print("The number you entered is positive:-",x)
        print("The integer portion:-",roundx)
else:
    if roundx<x:
        intportion=roundx+1
        print("The number you entered is negative:-",x)
        print('The integer portion:-',intportion)
    else:
        intportion=roundx
        print("The number you entered is negative:-",x)
        print("The integer portion:-",roundx)
        
if(intportion%2==0):
    print("The number given is even")
else:
    print("The number given is odd")
        
print('bye')


# In[32]:


get_ipython().run_line_magic('whos', '')


# In[35]:


a= int(input("Enter max iteration:"))
i=1
while i<a:
    print(i)
    i+=1
print("Done")


# In[36]:


a= int(input("Enter max iteration for square of the number:"))
i=1
while i<a:
    print(i**2)
    i+=1
print("Done")


# In[39]:


a= int(input("Enter max iteration for even numbers:"))
i=1
while i<a:
    if i%2==0:
        print(i)
    i+=1
print("Done")


# In[ ]:


n=10
i=1
while True:
    if i%5==0:
        print(i,"Divisible by 5")
        break
    else:
        print(i,"Not Divisible by 5")
        i+=1
print("done")
        
    


# In[1]:


n=10
i=1
while True:
    if i % 9 != 0:
        print(i)
        i+=1
        continue
        print("Continue skipped")# will never get printed as it is in continue indendation
        print("Continue skipped again")# will never get printed as it is in continue indendation
    print("Will print after the if is false")
    break
        
           
print("done")
        


# In[4]:


l=[]
for i in range(10):
    print(i);
    l.append(i**2)
    print(l)


# In[6]:


l=[]
for i in range(0,10,2): # start from(0):smaller then(10):jump(2 ie 2 4)
    print(i);
    l.append(i**2)
    print(l)


# In[8]:


l=[]
for i in range(1,20,3): # start from(0):smaller then(10):jump(2 ie 2 4)
    print(i);
    l.append(i**2)
    print(l)


# In[11]:


S={"apple",4.9,"cherry"}
for x in S:
    print(x)
else:
    print("loop completes its iteration")
print("everything inside S is printed")


# In[13]:


S={"apple",4.9,"cherry"}
i=1
for x in S:
    print(x)
    i+=1
    if i==3:
        break ##will break everything for and its respective else
    else:
        pass
else:
    print("loop completes its iteration")
print("everything inside S is printed")


# In[15]:


D={"apple":44, "cherry":"game"} #here apple stores value 44 D[apple]
for x in D:
    print(x,D[x])


# In[16]:


F={"A":"10","B":"-5","C":"8"}
for x in F:
    print(x,F[x])


# In[32]:


## Given  a list of numbers sort it in ascending order
L =[100,6,56,78,2,5,9,10,600,543,6,0,-800,-5,-6,34]
for j in range(len(L)):
        minno=L[j]
        idx=j
        c=j
        for i in range(j,len(L)):
                if L[i]<minno:
                    minno=L[i]
                    idx=c
                c+=1
        temp=L[j]
        L[j]=minno
        L[idx]=temp
print(L)
        

        




# # Functions

# In[1]:


def printsuccess():
    print("I am done")
    print("Please send next task")


# In[2]:


printsuccess()


# In[15]:


def description():
    """ This Function is an example on how to get the description written in any function.
        It is a good practice to always describe any function
        This function is just printin "hello"
    """
    print("hello")


# In[4]:


description()


# In[5]:


description()?


# In[11]:


get_ipython().run_line_magic('pinfo', 'description')
##will only show us the desciption written in comments not the code


# In[12]:


get_ipython().run_line_magic('pinfo2', 'description')
##will show us the desciption written in comments along with the code


# In[13]:


help(description)
##will only show us the desciption written in comments not the code


# In[14]:


description()


# In[16]:


def printmessage(msg):
    """Will simply type the user msg and tell if it is string or not"""
    if isinstance(msg,'str'):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is what you have supplied",msg)


# In[17]:


printmessage(HelloWorld)


# In[18]:


printmessage("HelloWorld")


# In[29]:


def printmessage(msg):
    """Will simply type the user msg and tell if it is string or not"""
    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is what you have supplied:",msg,"of type:",type(msg))


# In[26]:


printmessage("HelloWorld")


# In[21]:


printmessage("6756Hello")


# In[30]:


printmessage(6756)


# In[24]:


printmessage(6756Hello)


# In[31]:


y=1234567
printmessage(y)


# In[32]:


y=PythonCoding
printmessage(y)


# In[33]:


y="PythonCoding"
printmessage(y)


# In[34]:


def mypow(a,b):
    """This fun is like inbuilt pow function"""
    c=a**b
    print(c)


# In[35]:


mypow(2,4)


# In[78]:


def checkarg(a,b,c):
    """this function will chcek if the given argument is of type int or float and perform some calculation
      or will throw an error"""
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        d=a*b+c
        print("All the arguments are int or float.", a,"*",b,"+",c,"=",d)
    else:
        if not(isinstance(a,(int,float))):
            print("Error:1st argument is not int or float",a, "is",type(a),"so no proceeding ahead")
        elif not(isinstance(b,(int,float))):
            print("Error:2nd argument is not int or float",b ,"is",type(b),"so no proceeding ahead")
        else: 
            print("Error:3rd argument is not int or float",c, "is",type(c),"so no proceeding ahead")               


# In[67]:


checkarg(1,2,4)


# In[79]:


checkarg("a",2,4)


# In[80]:


checkarg(1,"b",4)


# In[81]:


checkarg(1,2,"c")


# In[84]:


def function1(a,b,c,d,e):
    print(a,b,c,d,e)


# In[85]:


function1(1,4,5,3,2)


# In[88]:


#here we want 1 to go in a, 2 to go in b, 3 in c, 4 in d, 5 in e here we can use assigmnet while calling function.
##1st check the argument name defined for the function by using function? once you get the names then use below
get_ipython().run_line_magic('pinfo', 'function1')
function1(a=1,b=2,c=3,d=4,e=5)


# In[92]:


function1("morning","good","awesome","Hellow","everyone")


# In[93]:


function1(a="Hellow",b="good",c="morning",d="everyone",e="awesome")


# In[94]:


function1(e=10,b=7,d=9,a=6,c=8)# assigned variable can be called in any order


# In[95]:


def myadd(a,b):
    sum=a+b
    return sum


# In[96]:


catchsum=myadd(2,4)
print(catchsum)


# In[102]:


print(myadd(2,4))
type(myadd(2,4)) #Type of the return


# In[98]:


def fun():
    a=1


# In[99]:


print(fun()) #any function will always return none


# In[101]:


print(type(fun())) #type of the none return


# In[103]:


variableoutsidefunction=100


# In[104]:


def demo():
    print(variableoutsidefunction);


# In[105]:


demo()


# In[106]:


def demo2():
    variableoutsidefunction=200
    print(variableoutsidef unction);


# In[107]:


demo()


# In[108]:


demo2()


# In[109]:


demo()


# In[110]:


def h():
    print(1)
    print(2)
    return
    print("a")
    print("ccc")


# In[111]:


h()


# In[112]:


print(h())


# In[113]:


print(type(h()))


# In[114]:


def return1():
    a=1
    b="happy"
    c=7.99
    return a,b,c


# In[116]:


x,y,z=return1()
print(x,y,z) #will catch in the order it is returned


# In[119]:


def return2():
    a=1
    b="happy"
    c=7.99
    return c,a,b


# In[121]:


x,y,z=return2()
print(x,y,z) 


# # arbritery number of arguments function

# In[126]:


def add(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum


# In[127]:


print(add(1,2,3,4,5,6))


# In[129]:


print(add(1,'a',3,4,5,6))


# In[130]:


print(add(20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1))


# In[131]:


def printvariablenamesandvalues(**args):
    for x in args:
        print("variable name is :",x,"and the value is:",args[x])


# In[132]:


printvariablenamesandvalues(a='qwe',b=9.8,c='hello',d=6)


# In[133]:


printvariablenamesandvalues(1='qwe',b=9.8,c='hello',d=6)


# # Default values in function

# In[134]:


def gg(value=6):
    print(value)# if no value is given during call the by default it wil print 6 if giv then the given value


# In[135]:


gg()


# In[136]:


gg(88)


# In[138]:


L=[1,2,3,4,5]
L2=L
L[0]=-9 #both share same memory location so change made in any is reflected in both
print(L)


# In[141]:


def ff(L=[1,2,3]):
    for i in L:
        print(i)


# In[142]:


ff()


# In[143]:


L3=[56,78,90,'a']
ff(L3)


# In[144]:


ff() #L will not take L3 values forever it will again pick the default value once the function scope is over


# In[145]:


gg(L3)


# In[146]:


gg()


# In[171]:


#import any function file from a location
import sys
sys.path.append('F:/MyPythonModules/')
import MyModules as UniFuns


# In[160]:


get_ipython().run_line_magic('pinfo2', 'UniFuns.checkifnotnum')


# In[172]:


print(UniFuns.universaladdallnums(6,9,90,100))


# In[173]:


#import only 1 function from the function file
from  MyModules_Functions import checkifnotnum as numFuns


# In[174]:


numFuns(1,2,3)


# In[175]:


numFuns(1,2,'ggg')


# In[208]:


UniFuns.myname
#sortLL([9,8,56,85,0,-1])


# # Practice Function

# In[211]:


## Given  a list of numbers find Min
def findmin(L):
    min=L[0]
    idx=0
    i=0
    for x in L:
        if x<min:
            min=x
            idx=i
        else:
            pass
        i+=1
    #print("The min value is:-",min,"at index:-",idx)
    return min,idx


# In[184]:


findmin([100,200,-5,8,1002362,6,2,4,50,-45])


# In[189]:


def swapvalues(L,idx1,idx2):
    """Swap 2 given index values in a List"""
    temp=L[idx1]
    L[idx1]=L[idx2]
    L[idx2]=temp
    return L


# In[191]:


OL=[2,3,5,8,9]
NL=swapvalues([2,3,5,8,9],3,4)
print("Old List:-",OL)
print("New List:-",NL)


# In[226]:


#from  MyModules_Functions import checkifnotnum as numFuns
def sortList(LL):
    if not(numFuns(LL)):
        print("All values enterted are not numeric")
        return
    else:
        c=0
        for x in LL:
            min,ind=findminFun(LL,c)
            LL=swapvalues(LL,c,ind)
            c+=1
    return LL 


# In[203]:


def sortLL(L):
    """This function will sort any list given in ascending order"""
    for j in range(len(L)):
        minno=L[j]
        idx=j
        c=j
        for i in range(j,len(L)):
                if L[i]<minno:
                    minno=L[i]
                    idx=c
                c+=1
        temp=L[j]
        L[j]=minno
        L[idx]=temp
    return(L)
        


# In[224]:


sortLL([9,8,56,85,0,-1])


# In[213]:


def numFuns(L):
    for x in L:
        if not(isinstance(x,(int,float))):
            return False
    return True


# In[228]:


print(sortList([9,8,56,85,0,-1]))


# In[222]:


## Given  a list of numbers find Min
def findminFun(L,stridx):
    min=L[stridx]
    idx=stridx
    for i in range(stridx,len(L)):
        x=L[i]
        if x<min:
            min=x
            idx=i
        else:
            pass
        i+=1
    #print("The min value is:-",min,"at index:-",idx)
    return min,idx


# In[229]:


print(sortList([10,9,67,45,10000,54647,-8,-99,-67]))


# In[230]:


word=input()
listofinput=[]

for letter in word:
    listofinput.append(letter)
    
print(listofinput)


# In[231]:


print(range(20))


# In[232]:


print(*range(20))


# # "Python" and 'Python' is the same do not mix "Python' or 'Python"

# In[249]:


s="Pythn is a good language"
p='It is good for data science'
type(s)


# In[236]:


print(s)


# In[245]:


if  2==2.0:
    print (True)
else:
    print (False)


# In[253]:


v = s+p
print(v)

v1=s+" "+p
print(v1)


# In[261]:


price = 12
f="The price of the book"
#g1= f+" is :" + price  #here we canno concat int only string can be done using +
g2= f+" is: " + str(price) #convert it to string

print(g2)
print(f,"is:",price) #Without converting we c=can achive the same by using print also proce adds spaces by itself


# In[262]:


multi ="""This is Line 1
This is line 2
This is last line 3""" ##for multiline we use """"""
print(multi)


# In[264]:


print("""the following options are availabe:
            -a    : does nothing
            -b    : does anything
            -c    : doeseverting """)


# In[273]:


indexing="Game of programming"
print(indexing[5])
type(indexing[5]) 


# In[271]:


type(indexing[4])


# In[274]:


indexing[5]


# In[277]:


indexing


# In[278]:


print(indexing)


# In[282]:


print(indexing)
indexing[-1]


# In[283]:


print(indexing)
indexing[-7]


# In[285]:


print(indexing)
indexing[-7:-1]


# In[286]:


print(indexing)
indexing[-13:-1]


# In[287]:


print(indexing)
indexing[-13:0]


# In[306]:


print(indexing)
print(indexing[-13:1:-1]) #need to specify -ve jump if we use any -ve start or end
print(indexing[-1:13:-2])#-1 to 13(12) with 2 jumps


# In[289]:


print(indexing)
indexing[-1:13]


# In[302]:


print(indexing)
print(indexing[-1:-13]) # will not print reverse
indexing[-1:-13:-2] # if jum is specified then it will


# In[291]:


indexing[2]='X' #once a string is created it is not changeable we need to created another changed string(immutable string)


# In[293]:


print(indexing)
indexing[0:12:2] # 0 to 12(till 11) jump of 2


# In[294]:


indexing[:12]# 0 is by default


# In[295]:


indexing[3:]# here till the end is by default it will include the end str as well


# In[296]:


indexing[::-1] # will reverse the string


# In[307]:


print(len(indexing))


# In[312]:


print(indexing)
print(indexing[3:8])
print(len(indexing[3:8]))


# In[319]:


spaces="       abcdes        hdgjagfjag      lasjlalknv       "
print(spaces)
print(len(spaces))
b=spaces.strip() #will remove spaves form front and back but will not remove in middle spaces
print(b)
print(len(b))


# In[323]:


zz='   ABC 90909 :::     kajshkjasgfjasfb GHFRCDSCDJNFHUJFVN'
print("Given:",zz)
Low=zz.lower()
Up=zz.upper()
print("Lower:",Low)
print("Upper:",Up)


# In[338]:


bb='HGFVHFYF ::: -0098776556##$%%^ lasjkashfkjfbxcjbvjb ;;;                  ;;;;'
print("Given:",bb)
Rep1=bb.replace(':','*')
Rep2=bb.replace(' ','^%^')#Space
Rep3=bb.replace('','+')#blank so it will add in between ever char

print(Rep1)
print(Rep2)
print(Rep3)



# In[341]:


SP="bgbf%uygdvf%1234%ijhgbfvdcrscdfv%8987654"
NewSP=SP.split("%")#will make a list on the bases of % as delimiter
print(NewSP)
print(NewSP[1])


# In[342]:


tt="tkshfksfhGFVdjdsbdjsbf"
dd=tt.capitalize()
print(dd)


# In[344]:


tt.a #here we can type an alphabet and tab to chcek if there is anyother function 


# In[345]:


"dagfacYTGGRDVBNJHGCasasas".capitalize()


# In[346]:


help(tt.count)


# In[1]:


"abc" in "hkajfjfhjabc68875sjbcb"


# In[2]:


"1234" in "hkajfjfhjabc68875sjbcb"


# In[4]:


"67676767" not in "454322434243"


# In[5]:


"@@@@" not in "@@@@&^&%&()"


# In[6]:


"abc"<"def"


# In[7]:


"abc">"def"


# In[9]:


print("We are learning \"Strings\" today")


# In[10]:


print("We are learning 'Strings' today")


# In[11]:


print('We are learning "Strings" today')


# In[14]:


print("We are \nnow on new line")
print("We are \n now on new line")


# In[15]:


print("We are \t now on new Tab")


# In[16]:


print("c:\name:\drive\tablet") #we want to print as it is no need of new line and tab


# In[17]:


print(r"c:\name:\drive\tablet") # r here means raw keep everything as it is dnt consider \ char


# In[60]:


def getDataFromUser():
    D={}
    while True:
        studentID= input("Enter Student ID:")
        Marks=input("Enter student marks by comma seperated values:")
        Morestud=input("Do you want to enter more students type y or n:")
        if studentID in D:
            Reenter=input("""You have already entered the student details.
               Do you want to delete old entries and enter new type y or n:""")
            if Reenter.lower() == "y":
                del D[studentID]
                D[studentID]=Marks.split(",")
        else:
            D[studentID]=Marks.split(",")
            
        if Morestud.lower() == "n":
            return D
        
                
                  


# In[62]:


studdata=getDataFromUser()


# In[63]:


studdata


# In[64]:


studdata=getDataFromUser()


# In[65]:


studdata


# In[66]:


studdata2=getDataFromUser()


# In[67]:


studdata2




# In[79]:


def getavgmrks(D):
    avgmarks={}
    for x in D:
        L=D[x]
        print(L)
        s=0
        for marks in L:
            s +=int(marks)
            print(int(marks))
            avgmarks[x]=s/len(L)
            print("x:",x)
    return avgmarks


# In[80]:


avgM=getavgmrks(studdata2)


# In[74]:


avgM


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


import numpy as np


# In[19]:


a1=np.array([1,2,3,4,5,6])


# In[20]:


b1=np.array((8,9,10))


# In[21]:


print(a1)


# In[22]:


print(b1)


# In[23]:


type(a1)


# In[24]:


a1.dtype


# In[28]:


a1=np.array([1,2,3,4,5,6],dtype='f')


# In[26]:


a1.dtype #64bit avaibale too


# In[29]:


ad2=np.array([[1,2,3],[4,5,6]])


# In[30]:


ad2.ndim


# In[31]:


ad2[0,2]


# In[37]:


bd1=np.array([[1,2,3],[5,6,7,8]]) #It shoukd have same no. of elements in each array


# In[36]:


bd1.ndim


# In[38]:


bd1=np.array([[1,2,3,-1],[5,6,7,8]])


# In[39]:


bd1.ndim


# In[41]:


bd1[1,3]


# In[42]:


cd3=np.array([[[4,6,7],[0,1,-1],[0,0,0]],[[-1,-2,-3],[9,4,3],[-5,-6,-4]]])


# In[44]:


cd3.ndim


# In[45]:


cd3[0,1,2]


# In[46]:


cd3[1,2,1]


# In[47]:


type(cd3)


# In[48]:


cd3.shape[0] #0 will tell you how many anrry list


# In[49]:


cd3.shape[1] # 1 will tell you each array has how may number of arrays in it


# In[50]:


cd3.shape[2]#2 will tell each arry has how many elemets in it


# In[56]:


cd3.shape[4]


# In[52]:


AA=np.array([2])


# In[53]:


AA.ndim


# In[54]:


BB=np.array(2)


# In[55]:


BB.ndim


# In[57]:


cd3.size #total number of elemets in the whole array


# In[59]:


cd3.nbytes


# In[81]:


AR=np.arange(100)


# In[82]:


AR


# In[83]:


AR1=np.arange(20,120)


# In[84]:


AR1


# In[85]:


AR2=np.arange(10,50,3) #for in in range(10,50,3)


# In[86]:


AR2


# In[87]:


print(range(10))


# In[89]:


print(list(range(10)))


# In[90]:


print(*range(10))


# In[91]:


E=np.random.permutation(np.arange(10)) # arranges the number 0-9 in random order
print(E)


# In[93]:


np.random.randint(20,30) #will return any random int between 20 to 30


# In[102]:


R=np.random.rand(1000) #random no. between 0 and 1


# In[97]:


R


# In[98]:


import matplotlib.pyplot as plt


# In[103]:


plt.hist(R)


# In[104]:


plt.hist(R,bins=100)


# In[105]:


RR=np.random.randn(10000)
plt.hist(RR,bins=200)


# In[110]:


RRR=np.random.rand(2,3) #created 2D array with 3 elements


# In[111]:


RRR


# In[112]:


RRR1=np.random.rand(3,2) #created 3D array with 2 elements


# In[113]:


RRR1


# In[123]:


RRR1.ndim


# In[115]:


RRR.ndim


# In[124]:


RRR2=np.random.rand(2,3,4,2)#(2Darrays, 3subarrays in the 2Darray, 4 subarrays in 3arrays, 2elemsnt in each array )


# In[121]:


RRR2


# In[122]:


RRR2.ndim


# In[125]:


RRR3=np.random.rand(3,4,5,6) #(3(4(5(6))))


# In[126]:


RRR3


# In[127]:


DD=np.arange(100).reshape(4,25)


# In[128]:


DD.shape


# In[130]:


DD=np.arange(100).reshape(4,5,5)


# In[131]:


DD.shape


# In[133]:


DD


# In[137]:


np.zeros(3,int)


# In[142]:


np.zeros(3)


# In[143]:


np.zeros((3,2))


# In[144]:


np.ones(4,int)


# In[145]:


np.ones(6)


# In[146]:


np.ones((6,8))


# In[147]:


np.ones(5)#5elemets


# In[148]:


np.ones((4,5),int)#4arrays of 5elemets


# In[149]:


np.ones((3,4,5),int)#3d array of 4arrays with 5 elemets


# In[150]:


np.ones((2,3,4,5),int)#3d array of 4arrays with 5 elemets


# In[156]:


NS=np.arange(100)


# In[157]:


ns=NS[3:10] #no copy is created it both referse to the same data address ns is a view to same array NS
print(ns)


# In[158]:


ns[0]=-45 #NS is also changed


# In[159]:


NS


# In[163]:


ns1=NS[10:20].copy() #will created seperate copy then NS


# In[164]:


ns1


# In[165]:


ns1[2]=-12 # this change will not be reflected in NS


# In[166]:


ns1


# In[167]:


NS


# In[168]:


# to get index of a particuler element in a array
index=np.argwhere(NS==-45)


# In[169]:


index


# In[170]:


index=np.argwhere(NS==-45)[0][0]


# In[171]:


index


# In[172]:


NS[index]=3


# In[173]:


NS


# In[174]:


ns


# In[175]:


T=np.round(10*np.random.rand(5,4)) #* by 10 and then rount it


# In[176]:


T


# In[178]:


T[2,2]


# In[187]:


T[2:]


# In[189]:


T[:3]


# In[188]:


T[2,:] #the whole 2nd row only


# In[197]:


T[:,3]# the whole 3rd column only


# In[195]:


T[1:3,2:4]# to pick sub columns


# In[196]:


T.T #T is for transporse conver rows o columns


# In[198]:


import numpy.linalg as la


# In[199]:


la.inv(np.random.rand(3,3))


# In[200]:


T.sort(axis=1) #Ascending


# In[201]:


T


# In[206]:


A=np.arange(100)


# In[207]:


A


# In[208]:


B=A[[5,9,8,12,78,54,99]] #Get only the given index values


# In[209]:


B


# In[210]:


B[3]=-9090


# In[213]:


B# this is not like B[4:5] where it referes the same array. Here by default different copy is created so A will not be changed


# In[212]:


A


# In[214]:


C=A[A<40] # all elements <40


# In[215]:


C


# In[219]:


D=A[(A<40) and (A>30)] #and cannot be used for arrays it is used for single object


# In[220]:


D=A[(A<40) & (A>30)]


# In[221]:


D


# In[222]:


#single object   Array
# and              &
# or               |
#not               ~


# In[223]:


EE=np.round(10*np.random.rand(2,3))


# In[224]:


EE


# In[225]:


EE+3


# In[227]:


EE+(np.arange(2).reshape(2,1))


# In[228]:


S=np.arange(2).reshape(2,1)


# In[229]:


S


# In[231]:


B=np.round(10*np.random.rand(2,2))


# In[232]:


B


# In[233]:


c=np.hstack((EE,B))


# In[234]:


c


# In[235]:


d=np.vstack((EE,B)) # it should be of same dimention 


# In[246]:


A=np.random.permutation(np.arange(10))


# In[247]:


A


# In[248]:


A.sort()


# In[249]:


A 


# In[250]:


np.sort(A)


# In[251]:


A=A[::-1] #sort in decending order


# In[252]:


A


# In[255]:


Y=np.array(["abc","tyr","how","zxc",23,78])


# In[256]:


Y


# In[257]:


Y.sort()


# In[258]:


Y


# In[259]:


BBB=np.random.rand(1000000)
get_ipython().run_line_magic('timeit', '#will give the time it took to execute sum(BBB)')
get_ipython().run_line_magic('timeit', 'np.sum(B) #B.sum()')


# In[260]:


def mysum(G):
    s=0
    for x in G:
        s+=x
    return s   


# In[264]:


get_ipython().run_line_magic('timeit', 'mysum(BBB)')


# In[266]:


LL=[1,2,34,56,7]
len(LL)-1


# In[275]:


i=0
j=1
for x in LL[i]
    print(x,y)


# In[3]:


def twoSum(nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []


# In[8]:


print(twoSum((5,6,3,4,6,7,8,9,30,87),36))


# In[62]:


import numpy as np
L1=[2,4,3]
L2 = [str(x) for x in L1]
print(L2[0])
#Con=L2[0]+L2[1]+L2[2]
Con="".join(L2)
print(Con)
L3=[5,6,4]
L4 = [str(x) for x in L3]
print(L4[0])
#Con1=L4[0]+L4[1]+L4[2]
Con1="".join(L4)
print(Con1)
New=int(Con)
print(type(New))
New1=int(Con1)
print(type(New1))
final=New+New1
print(final)
new_list= [int(x) for x in str(final)]
print(new_list[::-1])



#New=[str.replace(',','') for str in L2]
#print(New)
#print(New[0])







#L2=[564]
#L1[0]+L2[0]


# In[67]:


def addnumbers(l1,l2):
        l1new=[str(x) for x in l1]
        Conl1="".join(l1new)
        print(Conl1)
        l2new=[str(x) for x in l2]
        Conl2="".join(l2new)
        print(Conl2)
        intConl1=int(Conl1)
        intConl2=int(Conl2)
        Final=intConl1+intConl2
        Add_list= [int(x) for x in str(Final)]
        Final_list=Add_list[::-1]
        print(Final_list)
        return(Final_list)

L1=[9,9,9,9,9,9,9]
print(type(L1))
L2=[9,9,9,9]
print(addnumbers(L1,L2))


# In[90]:


x=121
x1=x
R=0
digit=0
while x1!=0:
    digit=x1 %10
    print("digit",digit)
    R=R*10+digit
    print("R",R)
    x1//=10
    print("x",x1)
if R==x:
    print(True)
else:
    print(False)


# In[79]:


x=121
m=x%10
m


# In[91]:


121/10


# In[92]:


121//10


# In[94]:


x=121
print(str(x)==str(x)[::-1])


# In[ ]:




