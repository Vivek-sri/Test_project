#--------------------------------------------------------------CODES FOR STRINGS----------------------------------------------------------------
#-----------------------------------------------Planidrome-------------------------------------------------------------------------------------


'''def fibo(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

# Define the value of x
x = 5

# Call the function and print the result
print(fibo(x))

#Python has 1000 limit of recursion, recursion depth
#Know stacks, heaps, hashmaps, value type and reference type
#Clas, attributes and methods, getter and setter, self


#TRYING TO WRITE A CLASS:
'''
'''
class Human:
    
    def __init__(self,age,name,gender,progeny):
        self.age=age
        self.name=name
        self.gender=gender
        self.progeny=progeny

    def what_is_age(self):
        return self.age

    def what_is_name(self):
        return self.name

    def what_is_gender(self):
        return self.gender

    def do_children_exist(self):
        return self.progeny

human= Human(23,'Vivek','Male',0)
print(human.what_is_name())










class Math:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        return self.x+ self.y

    def multiply(self):
        return self.x* self.y

math=Math(3,6)
print(math.add())
'''

'''
class Employee:

    def __init__(self,emp_id,emp_name,emp_salary_per_day,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary_per_day=emp_salary_per_day
        self.emp_department=emp_department

    def salary(self):
        return self.emp_salary_per_day * 30

    def name(self):
        return self.emp_name

    def id(self):
        return self.emp_id

    def dept(self):
        return self.emp_department

    def details(self):
        return self.emp_name, self.emp_id,  self.emp_department,  self.emp_salary_per_day * 30


employee1= Employee('E7876', 'ADAMS', 50000, 'ACCOUNTING')
employee2= Employee('E7499','Jones', 45000,'Research')
employee3= Employee('E7900','Martin',50000,'Sales')
employee4= Employee('E7698','Smith', 55000,'Operations')


print(employee1.details(), 
      employee2.details(),
      employee3.details(),
      employee4.details()),'''

'''
class Vehicle:
    def __init__(self,mileage,initial_fuel,fuel_left):
        self.mileage=mileage
        self.initial_fuel=initial_fuel
        self.fuel_left=fuel_left

    def finding_initial_fuel(self):
        return self.initial_fuel

    def finding_fuel_left(self):
        return self.fuel_left

    def finding_distance_left(self):
        if self.fuel_left<=5:
            print("You havereached reserve fuel")

        else:
            return (self.fuel_left-5)*self.mileage

    def finding_distance_travelled(self):
        return (self.initial_fuel-self.fuel_left)*self.mileage

car=Vehicle(12,30,20)
print(car.finding_distance_travelled())
print(car.finding_distance_left())


class Instructor:
# methods include allocate_course(),check_eligibility(technology),check_avg_feedback()
# attributes include average feedback, instruvtor name, experience,technology skill
    course='Python'

    def __init__(self,name,experience,feedback,technology):
        self.name=name
        self.experience=experience
        self.feedback=feedback
        self.technology=technology

    def check_avg_feedback(self):
        if self.experience<3 and self.feedback >= 4:
            print("Eligible")

        elif self.experience>3 and self.feedback >=4.5:
            print("Eligible")

        else:
            print("Not eligible")

    def allocate_course(self):
        if self.technology==course
            print("The course can be allocated to the instructor")

        else:
            print("Do not allocate")

    def check_eligibility(self):



        



        elif 
'''

'''class Vehicle:
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage

    def drive(self):
        print("You are now in drive mode")

    def stop(self):
        print("You are now in stop mode")


class Car(Vehicle):
    def __init__(self,make,model,year,mileage,num_of_doors):
        self.num_of_doors=num_of_doors
        Vehicle.__init__(self,make,model,year,mileage,)

    def accelerate(self):
        print("You can now accelerate your car")

    def brake(self):
        print("You can now apply brakes to your car")

class Truck(Vehicle):
    def __init__(self,make,model,year,mileage,cargo_capacity):
        self.cargo_capacity=cargo_capacity
        Vehicle.__init__(self,make,model,year,mileage,)

    def loading(self):
        print("You can now load the goods to the truck")

    def unloading(self):
        print("You can now unload the goods from the truck")

x= Car("Grey", "VXI", 2019, 15,4)
x.accelerate()
y= Truck("Yello","WFG",2023,10,150)
y.unloading()
'''

'''class Animal:
    def __init__(self,eyes,tail):
        self.eyes=eyes
        self.tail=tail

    def eye_purpose(self):
        print("Eyes help to see things")

    def tail_purpose(self):
        print("Tail helps to navigate")

class Mammals(Animal):

    def __init__(self,eyes,tail,fur_colour):
        self.fur_colour=fur_colour
        Animal.__init__(self, eyes, tail)

    def fur_purpose(self):
        print("Furs are helpfull to keep warmth in cold places and to keep the skin neat")

class Bird(Animal):

    def __init__(self,eyes,tail,feathers):
        self.feathers=feathers
        Animal.__init__(self, eyes, tail)

    def feather_purpose(self):
        print("Feathers helps in keeping birds warm, show off and blend in")


x= Mammals(2,1,'Brown')
x.fur_purpose()

y= Bird(2,1,'White')
y.tail_purpose()
'''




'''Mini Project: Library Management System

Description:
Create a simple library management system that allows users to manage books, borrowers, and library transactions. The system should consist of the following classes:

Book: Represents a book in the library. Each book should have attributes such as title, author, ISBN, genre, and availability status. Methods could include check_out() 
to mark the book as borrowed, check_in() to mark it as returned, and display_info() to show details about the book.

Borrower: Represents a library borrower. Each borrower should have attributes like name, address, contact information, and a list of borrowed books. 
Methods could include borrow_book() to borrow a book, return_book() to return a book, and display_info() to show borrower details.

Library: Represents the library itself. It should maintain a collection of books and borrowers.
 Methods could include add_book() to add a new book 
to the library, add_borrower() to add a new borrower, find_book() to search for a book by title or author, find_borrower() to search for a borrower 
by name, and display_books() and display_borrowers() to show all books and borrowers in the library.

Transaction: Represents a library transaction, such as borrowing or returning a book. It should keep track of the borrower, the book involved, the 
transaction type (borrow or return), and the date of the transaction.
You can enhance this project by adding features like authentication for borrowers, notifications for overdue books, sorting and filtering
 options for books and borrowers, and data persistence using file handling or a database.
By implementing this project, you'll gain a better understanding of how to design and implement classes in Python, as well as how to create 
interactions between different objects in a system.'''



'''Create a top class and maybe declare the display info in it so that we can use it for the other clsses to display info about the book or the borrower'''


class Book:

    def __init__(self,title,author,genre,availability_status=True):
        self.title=title
        self.author=author
        self.genre=genre
        self.availability_status=availability_status

    def check_out(self):
        if self.availability_status:
            self.availability_status=False
            print("The book {self.title} has been checked out")

        else:
            print("The book has already been checked out")

    def check_i(self):
        if not self.availability_status:
            self.availability_status=True
            print("The book {self.title} has been checked in")

        else:
            print("The book {self.title} has already been checked in")

    def display_info(self):
        return self.title
        return self.author
        return self.genre
        print(display_info())

class Borrower:
    def __init__(self,name,contact_number,membership_number):
        self.name=name
        self.contact_number=contact_number
        self.membership_number=membership_number
        self.borrowed_books=[]

    def borrow_book(self,book):
        if book.availability_status:
            self.borrowed_books.append(book)
            book.checkout()
        else:
            print("Srry the book is unavailable")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.check_in()
        else:
            print("You haven't borrowed this book")

    def display_info(self):
        return self.name
        return self.contact_number
        return self.membership_number
        print(display_info())

class Library:
    def __init__(self,title,author,name):
        self.title=title
        self.author=author
        self.name=name
        self.books=[]
        self.borrower=[]

    def add_book(self,title):
        self.books.append(title)

    def add_borrower(self):
        self.borrower.append(name)

    def search_book(self):
        if self.title in self.books:
            return True
        else:
            return False
    def display_books(self):
        print(self.books)

    def display_borrowers(self):
        print(self.borrower)


x=Library()













