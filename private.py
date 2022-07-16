# Private class
import logging

logging.basicConfig(filename='private.log',level=logging.DEBUG,
                    format= '[%(levelname)s] : %(asctime)s: %(name)s:%(message)s')

#Example1
class private:

    def fun(self):
        print("Public method")

    def __fun(self):
        print("Private method")


obj = private()

obj._private__fun()

#Example2
class Company:

    def __init__(self,company,type):
        logging.debug('Wer are initializing the private company')
        self.__company = company
        self.type = type

    def company_info(self):
        logging.debug('company_info describe about information about company')
        try:
            if type(self.type) == str:
              print(self.__company + ' is a '+ self.type + ' company ')
            else:
                raise ValueError('Entered values must be string')
        except Exception as e:
            print(e)
            logging.exception(e)

c = Company('Ineuron','Edtech')
print(c._Company__company)
c.company_info()

#Example 3
class Area:

    def __init__(self, length, breath):
        logging.debug('We are Initializing the Area method')
        self.__lenght = length
        self.__breath = breath

    def __area_of_comp(self):
        logging.info('area_of_comp describe about the area of rectangle ')
        try:
            if type(self.__lenght) == int and type(self.__breath) == int :
                logging.debug('this function is called from private method')
                print('Area of the rectangle is '+ str(self.__lenght * self.__breath))
            else:
                raise ValueError('Entered values must be integers')
        except Exception as e:
            print(e)
            logging.exception(e)

a = Area(12,5)
a._Area__area_of_comp()
a1 = Area('a','b')
a1._Area__area_of_comp()

#Example 4
class Student:
    logging.debug('Initializing the values outside of __init__')
    __name = 'Murali'
    __roll = 423
    __course = 'FSDS'

    def __init__(self):
        logging.info('name: '+ self.__name)
        logging.info('rollno'+str(self.__roll))
        logging.info('Course'+ self.__course)

s = Student()
print(s._Student__name,s._Student__roll,s._Student__course)
s._Student__name = 'Radha Krishana'  #Changing private variables
s._Student__roll = 195
s._Student__course ='Full Stack JavaScript'
print(s._Student__name,s._Student__roll,s._Student__course)

#Example 5
class Jobs:

    def __init__(self, company, jobs):
        logging.debug('We are initiating the Jobs class')
        self.__company = company
        self._jobs = jobs

    def __job_info(self):
        logging.info('we initialized protected method')
        try:
            if type(self.__company) == str and type(self._jobs) == str:
                print(self.__company + ' is providing '+ self._jobs +'opportunity from different companies')
            else:
                raise ValueError('both values should be string')
        except Exception as e:
            logging.exception(e)

j = Jobs('Ineuron','Datascience')
j._Jobs__job_info()
j1 = Jobs('Ineuron', 678)
j1._Jobs__job_info()

#Example 6
class Employee:

    def __init__(self, name, salary):
        logging.debug('We are initializing employee class')
        self.__name = name
        self._salary = salary

    def __emp_info(self):
        logging.info('This method describe about the employee info')
        try:
            if type(self.__name) == str:
                print(self.__name + ' is working in Ineuron an datascience ')
            else:
                raise ValueError('value should be string')
        except Exception as e:
            logging.exception(e)

    def _emp_salary(self):
        logging.info('This method describe about the employee salary info')
        try:
            if type(self._salary) == int:
                print(self.__name + ' salary is ' + str(self._salary))
            else:
                raise ValueError('value should be integer')
        except Exception as e:
            logging.exception(e)

    def emp_details(self):
        try:
            logging.info('This method describe about the employee details')
            self.__emp_info()
            self._emp_salary()
        except Exception as e:
            logging.exception(e)

e = Employee('murali','45000')
e.emp_details()
e._emp_salary()

#Example 7
class Fruit:

    def __init__(self, name):
        logging.debug('Initialize the Fruit class')
        self.__name = name

    def __fruit_info(self):
        logging.info('fruit info ')
        try:
            if type(self.__name) == str:
               print(self.__name)
               return  self.__name
            else:
                raise ValueError('Please enter string values only')
        except Exception as e:
            print(e)
            logging.exception(e)

    def fruit_details(self,type_of_fruit):
        logging.info('This method describe about fruit details')
        try:
            if type(type_of_fruit) == str:
                print(self.__fruit_info() + 'is a '+ type_of_fruit + ' Fruit.')
            else:
                raise ValueError('Please enter string values only')
        except Exception as e:
            logging.exception(e)

f = Fruit('Mango')
f._Fruit__fruit_info()
f.fruit_details('sweet')
f1 = Fruit('Lemon')
f1.fruit_details('citrus')

#Example8
class Ineuron_Affliation:

    def __init__(self):
        logging.debug("We just initiated iNeuron Affliate")
        print('Ineuron Affliatae has started')

    def __affliate_info(self):
        return 'The who purchase either one neuron/kids neuron can affliate to others'

    def __create_affliate(self,program):
        return 'Affliation link for '+program+ ' is htttps://course.ineuron.afflication'+program

    def __use_of_affliate(self):
        return 'As a strudent you can also earn money by affliating others'

    def refer_affliate(self, program, name):
        try:
            logging.debug('This method describes about the refering of affliate')
            if len(program) == 0 or len(name) == 0:
                raise ValueError('The value of program/name is null')
            if type(program) == str and type(name) == str:
                return 'This is '+self.__create_affliate(program)+' for your friend '+ name
            else:
                raise Exception('The given values are not string please enter string only.')
        except Exception as e:
            logging.exception(e)

    def affliate_earning(self):
        logging.debug('This method describes about the earning of affliate')
        print(self.__affliate_info())
        print(self.__use_of_affliate())
        print("You have earned 10% who ever purchase any of program")

a = Ineuron_Affliation()
print(a._Ineuron_Affliation__affliate_info())
print(a.refer_affliate('FSDS', 'kiran'))
print(a.refer_affliate(78,909))
print(a.affliate_earning())

#Example 9
class Bank:

    def __init__(self,name):
        logging.debug('We are initialzing the Bank class')
        self.__name = name

    def __bank_info(self):
        logging.info('bank info method describe about bank class')
        try:
            if type(self.__name) == str:
                print('Bank name is '+ self.__name)
            else:
                raise ValueError('Please Enter string only')
        except Exception as e:
            logging.exception(e)#

b = Bank('SBI')
b._Bank__bank_info()

#Example 10
class Country:

    logging.debug('Initializing with out init class')
    __name = 'India'
    __logo = '3 Lions'

    def __info(self):
        logging.info('info describe about the country ')
        try:
            if type(self.__name) == str and type(self.__logo) == str:
                print(self.__name + ' is My Country and its logs is '+ self.__logo)
            else:
                raise ValueError('Please Enter string only')

        except Exception as e:
            logging.exception(e)
c = Country()
c._Country__info()
