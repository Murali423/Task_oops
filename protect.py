#protected class
import logging

logging.basicConfig(filename='protect.log',level=logging.DEBUG,
                    format='[%(levelname)s]: %(name)s : %(asctime)s : %(message)s')

# Example 1
class Company:

    def __init__(self,company, domain, founder):
        logging.debug('We initiated values for Ineuron')
        try:
            if type(company) == str and type(domain) == str and type(founder) == str:
                self._company = company  # protected variable
                self.domain = domain
                self._founder = founder
            else:
                raise ValueError('values should be string')
        except Exception as e:
            logging.exception(e)

    def info(self):
        logging.info('We entered to Info method which describe aobut company')
        try:
            print(self._company, ' is a ', self.domain, ' which is founded by' , self._founder)
        except Exception as e:
            logging.exception(e)
        finally:
            logging.info('Information has delivered')
            print('This statement is from finally class')

c = Company('Ineuron','EdTech', 'Sudanashu and Krish')
print(c.domain)
print(c._company)
print(c._founder)
print(c.info())

#Example2
class Student:
    #protected variables
    logging.info('We are defining the variables directly ')
    _name = 'Murali'
    _rollno = 423
    _batch = 'FSDS'
    logging.info('__init__ method is not initialized even though we can refer them by self.')

    def student_info(self):
        logging.debug('student_info method describe about student information')
        try:
            print('Student name: ', self._name)
            print('Roll number ',self._rollno)
            print('Batch ',self._batch)
        except Exception as e:
            logging.exception(e)
        finally:
            logging.info('This method give info about students')

s = Student()
print(s._name)
s.student_info()

#Example3
class Courses:

    logging.debug('We are initiating the variable directly')
    _course = 'FSDS'
    _mode = 'Online'
    _price = 17500

    def course_info(self):
        logging.debug('course_info method describe about course info information')
        try:
            if type(self._course) == str and type(self._mode) == str:
                print(self._course + ' is  a '+self._mode + 'and price of course is ' + str(self._price))
            else:
                raise ValueError('given couser and mode should be string and price should be integer')
        except Exception as e:
            print(e)
            logging.exception(e)

        finally:
            logging.info('This statement from finally')

c = Courses()
print(c._price)
print(c.course_info())
c._course = 'Full Stack javascript'   #changing protected variable values
c._mode = 'Community'
c._price = 4000
print(c._price)
print(c._course)
print(c.course_info())

#Example4
class Platform:

    def __init__(self,company, platform):
        logging.debug('we are initializing the platform class')
        self._company = company
        self._platform = platform

    def _no_of_platforms(self):
        logging.info('we are entered into private methods')
        try:
            print(self._company + ' is having the '+self._platform)
        except Exception as e:
            logging.exception(e)

    def price_for_platfrom(self):
        try:
            logging.info('we entered into price of each platform')
            self._no_of_platforms()
            print('One Neuron costs about 11500 and Kids Neuron cost about 7000')
        except Exception as e:
            logging.error(e)

p = Platform('Ineuron', '1.One Neuron  2.Kids Neuron')
p._no_of_platforms()
p.price_for_platfrom()

p1 = Platform('Ineuron','Commuinity')
p1.price_for_platfrom()

#Example 5
class Area:
    _radius = 5

    def _area_circle(self):
        logging.info('area of circle returns the area of circle  ')
        try:
            if type(self._radius) == int:
                print('Area of the circle is ',3.14*self._radius*self._radius)
            else:
                raise Exception('Value of radius should be integer')
        except Exception as e:
            logging.exception(e)

a = Area()
a._area_circle()
a._radius = 10
a._area_circle()

#Example 6
class Jobs:

    def __init__(self, company, jobs):
        logging.debug('We are initiating the Jobs class')
        self._company = company
        self._jobs = jobs

    def _job_info(self):
        logging.info('we initialized protected method')
        try:
            if type(self._company) == str and type(self._jobs) == str:
                print(self._company + ' is providing '+ self._jobs +'opportunity from different companies')
            else:
                raise ValueError('both values should be string')
        except Exception as e:
            logging.exception(e)

j = Jobs('Ineuron','Datascience')
j._job_info()
j1 = Jobs('Ineuron', 678)
j1._job_info()

#Example 7
class Employee:

    def __init__(self, name, salary):
        logging.debug('We are initializing employee class')
        self._name = name
        self._salary = salary

    def _emp_info(self):
        logging.info('This method describe about the employee info')
        try:
            if type(self._name) == str:
                print(self._name + ' is working in Ineuron an datascience ')
            else:
                raise ValueError('value should be string')
        except Exception as e:
            logging.exception(e)

    def _emp_salary(self):
        logging.info('This method describe about the employee salary info')
        try:
            if type(self._salary) == int:
                print(self._name + ' salary is ' + str(self._salary))
            else:
                raise ValueError('value should be integer')
        except Exception as e:
            logging.exception(e)

    def emp_details(self):
        try:
            logging.info('This method describe about the employee details')
            self._emp_info()
            self._emp_salary()
        except Exception as e:
            logging.exception(e)

e = Employee('murali','45000')
e.emp_details()
e._emp_salary()

#Example 8
class Music_app:

    def __init__(self, appname, type_of_app):
        logging.debug('We are initializing the values for Music application')
        self._appname = appname
        self.type_of_app = type_of_app

    def _music_info(self):
        logging.info('music info describe about what kind of app')
        try:
            if type(self.type_of_app) == str and type(self._appname) == str:
                print(self._appname + ' is a '+ self.type_of_app + ' application we can listen music for '+ self.type_of_app)
            else:
                raise ValueError('Values should be string')
        except Exception as e:
            logging.exception(e)

    def music_app_details(self, pod):
        logging.info('music_app_details method explain about details of music')
        try:
            if type(pod) == str:
                self._music_info()
                print(self._appname + ' has contains '+ pod )
            else:
                raise ValueError('The value entered must be string')
        except Exception as e:
            logging.exception(e)
        finally:
            logging.info('Finally you can enjoy music')
            print('You can enjoy music')

m = Music_app('jio_savan','paid')
m._music_info()
m.music_app_details('podcast')
m1 = Music_app('Youtube','free')
m1.music_app_details('video')
m2 = Music_app('RED','free')
m2.type_of_app = 'combined'
m2.music_app_details('FM')

# Example 9
class No_of_course:

    def __init__(self):
        logging.debug('We just initialed number of courses class ')
        self._one_neuron = 400
        self.community = 55
        self._kids_neuron = 100

    def _one_ner(self):
        return self._one_neuron

    def comm(self):
        return self.community

    def _kid(self):
        return self._kids_neuron

    def no_of_cr(self, p):
        try:
            if (p == 'O' or p == 'o') and len(p) == 1:
                return 'The one neuron has '+ str(self._one_ner())+ ' courses'
            elif (p == 'C' or p == 'c') and len(p) == 1:
                return 'The community has ' + str(self.comm())+ ' courses'
            elif (p == 'K' or p == 'k') and len(p) == 1:
                return 'The kid neuron has ' + str(self._kid()) + ' courses'
            else:
                raise Exception('Please Enter any of O/C/K')
        except Exception as e:
            print(e)
            logging.exception(e)

n = No_of_course()
print(n._one_neuron)
print(n._kid())
n.no_of_cr(10)
print(n.no_of_cr('K'))
n.no_of_cr('MU')

# Example 10
class House:

    def __init__(self,type_of_home):
        logging.debug('we are initializing the House class')
        self._ty = type_of_home

    def house_type(self):
        logging.info('house_type describe about type of house')
        try:
            if type(self._ty) == str:
                print('There are so many types of houses now a days people prefer ' + self._ty)
            else:
                raise Exception('Value should be string')
        except Exception as e:
            logging.exception(e)

h = House('2-BHK')
h.house_type()
