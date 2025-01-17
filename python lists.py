# __________________________________________CODES FOR LISTS____________________________________________
#--------------------------------------------Reversing the first and last elements of a list-----------------------------------
'''test_list=[]
x=0
a=int(input("Enter the range of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))        #user should give us all the elements in one go rather than individually entering them
    test_list.append(num)
test_list=list(input("Enter the range of elements in the list: "))
x=test_list[0]
test_list[0]=test_list[-1]
test_list[-1]=x
print(test_list'''
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------Length of the list------------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
print("The number of elements in the list is",len(my_list))'''
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------Check if elements exist in list----------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
num1=int(input("Enter the number to be chedcked: "))
if num1 in my_list:
    print("Number exists in the list")
else:
    print("Number does not exist in the list")'''
#----------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------Reversing a list#---------------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers in the list: "))
    my_list.append(num)
print("Your list is: ",my_list)
rev_list=my_list[::-1]
print("Your reversed list is: ",rev_list)'''
#------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------Sum of elements in the list-------------------------------------------------------------------------
'''sum=0
my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
print("My list is: ",my_list)
for i in my_list:
    sum+=i

print("The sum of elements in the list is: ",sum)'''
#--------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------Multiply elements of the list-------------------------------------------------------------------
'''mul=1
my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
for i in my_list:
    mul*=i
print("The multiplication of all the elements is: ",mul)'''
#--------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------Smallest in the list-----------------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
b=my_list[0]
for j in my_list:
    if j<b:
        b=j

print("The smallest element in the list is: ",b)'''
#---------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------Largest in the list-----------------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
b=my_list[0]
for j in my_list:
    if j>b:
        b=j

print("The largest element in the list is: ",b)'''
#-----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------Second largest in the list----------------------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
b=my_list[0]
for j in my_list:
    if j>b:
        b=j
my_list.remove(b)
b=my_list[0]
for j in my_list:
    if j>b:
        b=j
print("The second largest number from the list is: ",b)'''
#----------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------Remove multiple elements from a list-------------------------------------------------------------
'''my_list=[]
a=int(input("Enter the number of elements in the list: "))
for i in range(0,a):
    num=int(input("Enter the numbers: "))
    my_list.append(num)
for i in my_list:
    if i % 2==0:
        my_list.remove(i)
print("The updated list is: ",my_list)'''
#-----------------------------------------------------------------------------------------------------------------------------------------

#                                           OOPS
'''
class Line():

    def __init__(self,coord1,coord2,):

        self.coord1 = coord1
        self.coord2 = coord2


    def calc_distance(self):
        return ((self.coord2[1]-self.coord1[1])**2+(self.coord2[0]-self.coord1[0])**2)**0.5

    def calc_slope(self):
        return (self.coord2[1]-self.coord1[1]) / (self.coord2[0]-self.coord1[0])

my_line=Line((3,2),(8,10))

print(my_line.calc_slope())
print(my_line.calc_distance())
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------

'''
class Cylinder():

    pi = 3.141592653589793


    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.pi * self.height * self.radius * self.radius

    def surface_area(self):
        return  2 * self.pi * self.radius * self.radius + 2 * self.pi * self.height * self.radius

my_cylinder=Cylinder(3,2)
print(my_cylinder.volume())
print(my_cylinder.surface_area())
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# class Bank_Account():
#
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
#
#     def withdraw(self,amount):
#
#         if amount < self.balance:
#             self.balance -= amount
#             return self.balance , "Withdrawal Possible"
#
#
#         else:
#             return "Withdrawal Failed"
#
# my_account = Bank_Account("Vivek",100)
# print(my_account.deposit(100))
# print(my_account.withdraw(100))
# print(my_account.withdraw(500))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                       ERRORS AND EXCEPTION HANDLING

# try:
#     for i in ['a','b','c']:
#         print(i**2)
#
# except:
#     print("Something went wrong")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# try:
#     x = 5
#     y = 0
#     z = x/y
#     print("We got it right")
#
# except:
#     print("Whoops an error occurred!")
#
# finally:
#     print("All done!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# def ask(n):
#     print(n**2)
# while True:
#     try:
#         n=int(input("Enter the number: "))
#
#     except:
#         print("Sorry an error occurred!")
#
#     else:
#         print("Tahank you!")
#         break

#-----------------------------------------------------------------------------------------------------------------------------------------------------



