#Inheritance class
import logging
logging.basicConfig(filename='inheritance.log',level=logging.DEBUG,
                    format='[%(levelname)s] : %(asctime)s : %(name)s : %(message)s')

#example 1
# simple inheritance
class Company:

    def __init__(self):
        logging.debug('We are initializing the Parent Company class')

    def info(self):
        logging.info('info method from company class')
        print('This method is printing from base class')
        pass

class CCompany(Company):

    def __init__(self, name, domain):
        logging.info('We are initializing the child company class')
        self.name = name
        self.domain = domain

    def info(self):
        logging.info('info describe about the child class')
        Company.info(self)

i = CCompany('Ineuron','edtech')
i.info()

#Example2
class Job(CCompany):
    def __init__(self, name, domain):
        logging.info('we are initializing the job class')
        CCompany.__init__(self, name, domain)

    def company_info(self):
        logging.info('logging info describe about the company info')
        try:
            if type(self.name) == str and type(self.domain) == str:
                print(self.name + 'is a '+ self.domain +' company')
            else:
                raise ValueError('The entered values should be string')
        except Exception as e:
            logging.exception(e)

j = Job('Ineuron','edtech')
j1 = Job('SBI','Banking')
j.info()
j.company_info()
j1.company_info()

#Example 3

class Person:
    name = 'Murali'
    def __init__(self, name):
        logging.info('logging info describe about the person info')
        self.name = name

    def getName(self):
        logging.info('logging info describe about the name')
        return self.name

    def isEmployee(self):
        logging.info('logging info describe about the Employee')
        return False

class Employee(Person):
    def isEmployee(self):
        logging.info('logging info describe about the Employee')
        return True
emp = Person("Murali")
print(emp.getName(), emp.isEmployee())

emp = Employee("TCS")
print(emp.getName(), emp.isEmployee())

#Example 4
# multilevel inheritance
class CEO(Employee):

    def is_CEO(self):
        logging.info('logging info describe about the CEO')
        print( self.name+ ' is CEO')

c = CEO('Raj')
c.isEmployee()
c.is_CEO()
c.getName()

#Example 5
class Polygon:
    def __init__(self, no_of_sides):
        logging.info('logging info describe about the Polygon class')
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        logging.info('logging info describe about sides of polygon')
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        logging.info('logging info describe about displaying sides')
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        logging.info('logging info describe about finding the Area')
        try:
            a, b, c = self.sides
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is' + str(area))
        except Exception as e:
            logging.exception(e)


t = Triangle()
t.findArea()

#Example 6