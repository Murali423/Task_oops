# Examples for Class and objects

import logging
logging.basicConfig(filename='class.log', level=logging.DEBUG,
                    format='[%(levelname)s]: %(asctime)s: %(name)s: %(message)s')

# Example 1
class Ineuron:

    def __init__(self):
        logging.debug('We entered into init method to initialize values,Welcome to iNeuron')
        print('Hi Welcome to iNeuron')

    def who_get_courese(self):
        try:
            logging.info('This is method which tells about who can avail the course')
            print('Any student/Any professional can avail course')
        except Exception as e:
            logging.error(e)

    def speciality_of_courses(self):
        try:
            logging.info('We entered into function which tells about speciality of iNeuron')
            print('The Speciality of iNeuron courses are all are affordable courses')
        except Exception as e:
            logging.error(e)

i = Ineuron()    # iNeuron object creation
i.who_get_courese()
i.speciality_of_courses()

#Example 2

class Ineuron_platform:

    def __init__(self):
        logging.debug('We have entered into iNeuron platform class')
        print('Welcome to iNeuron platform')


    def no_of_platform(self):
        try:
            logging.info('We Entered into numbers of platform method')
            print('iNeuron has mainly two platforms, 1.One Neuron 2.Kids Neuron')
        except Exception as e:
            logging.error(e)

    def price_for_platfrom(self):
        try:
            logging.info('we entered into price of each platform')
            print('One Neuron costs about 11500 and Kids Neuron cost about 7000')
        except Exception as e:
            logging.error(e)

    def courses_offered(self):
        try:
            logging.info('we entered into numbers of course offered in iNeuron platform')
            print('400+ course in the One neuron platform and 200 course in kids Neuron platform')
        except Exception as e:\
            logging.error(e)

p = Ineuron_platform() #ineuron platform object createion
p.no_of_platform()
p.price_for_platfrom()
p.courses_offered()

#Examples 3
class Ineuron_class:

    def __init__(self):
        logging.debug("We just initiated the ineuron_classes claas")
        print('Welcome to iNeuron Classes')

    def class_type(self, type_of_cls):
        try:
            logging.debug('This method describes about the type of class in iNeuron')
            if type(type_of_cls) == str:
                if type_of_cls == 'Community' or type_of_cls == 'community':
                    print('In Ineuron we have '+type_of_cls+' it is for free')
                elif type_of_cls == 'Live' or type_of_cls == 'live':
                    print('In Ineuron we have '+type_of_cls+' it costs depends on what you want to take')
                else:
                    raise Exception('The value entered is wrong please add live/community')
            else:
                raise Exception('Entered value is not a string please enter string')

        except Exception as e:
            print('we has self-phased courses to get those we need to purchase One/kids Neuron platform ')
            logging.exception(e)

c = Ineuron_class()
c.class_type(6)
c.class_type('live')
c.class_type('COMMUNITY')

#Example 4
class Ineuron_students:

    def __init__(self):
        logging.debug('We just initialed ineuron_students class')
        print('Welcome to iNeuron Students')
    def achiever(self):
        logging.info('The achiever function has called')
        print('The achivers are who has successfully transistion to new job')
    def hall_of_fame(self):
        logging.info('The achiever function has called')
        print('The students who got good score and giving interviews on wall of fame')
    def learner(self):
        logging.info('The achiever function has called')
        print('The students who joined to course and learning')
    def type_of_stud(self,student):
        try:
            if type(student) == str:
                if student == 'acheiver' or student == 'ACHIEVER':
                   self.achiver()
                elif student == 'hall' or student == 'HALL':
                    self.hall_of_fame()
                else:
                    self.learner()
            else:
                raise Exception('Please Enter valid student input')
        except Exception as e:
            print('please enter either achiever/hall')
            logging.exception(e)

st = Ineuron_students()
st.learner()
st.achiever()
st.type_of_stud(6)
st.type_of_stud('hall')
st.type_of_stud('ACHIVER')
st.type_of_stud('murali')

#Example 5
class No_of_course:

    def __init__(self):
        logging.debug('We just initialed number of courses class ')
        self.one_neuron = 400
        self.community = 55
        self.kids_neuron = 100

    def one_ner(self):
        return self.one_neuron

    def comm(self):
        return self.community

    def kid(self):
        return self.kids_neuron

    def no_of_cr(self, p):
        try:
            if (p == 'O' or p == 'o') and len(p) == 1:
                return 'The one neuron has '+ str(self.one_ner())+ ' courses'
            elif (p == 'C' or p == 'c') and len(p) == 1:
                return 'The community has ' + str(self.comm())+ ' courses'
            elif (p == 'K' or p == 'k') and len(p) == 1:
                return 'The kid neuron has ' + str(self.kid()) + ' courses'
            else:
                raise Exception('Please Enter any of O/C/K')
        except Exception as e:
            print(e)
            logging.exception(e)

n = No_of_course()
print(n.one_neuron)
print(n.kid())
n.no_of_cr(10)
print(n.no_of_cr('K'))
n.no_of_cr('MU')

#Example 6
class Ineuron_Affliate:

    def __init__(self):
        logging.debug("We just initiated iNeuron Affliate")
        print('Ineuron Affliatae has started')

    def affliate_info(self):
        return 'The who purchase either one neuron/kids neuron can affliate to others'

    def use_of_affliate(self):
        return 'As a strudent you can also earn money by affliating others'

    def create_affliate(self,program):
        return 'Affliation link for '+program+ ' is htttps://course.ineuron.afflication'+program

    def refer_affliate(self, program, name):
        try:
            logging.debug('This method describes about the refering of affliate')
            if len(program) == 0 or len(name) == 0:
                raise ValueError('The value of program/name is null')
            if type(program) == str and type(name) == str:
                return 'This is '+self.create_affliate(program)+' for your friend '+ name
            else:
                raise Exception('The given values are not string please enter string only.')
        except Exception as e:
            logging.exception(e)

    def affliate_earning(self):
        logging.debug('This method describes about the earning of affliate')
        print(self.affliate_info())
        print(self.use_of_affliate())
        print("You have earned 10% who ever purchase any of program")

a = Ineuron_Affliate()
print(a.affliate_info())
print(a.refer_affliate('FSDS', 'kiran'))
print(a.refer_affliate(78,909))
print(a.affliate_earning())

#Example 7
class Ineuron_blog:

    def __init__(self):
        logging.debug('we initialized the Ineuron Blog class')
        print('Welcome to Ineuron-blog')

    def thank_blog(self):
        logging.info('This method describe about thank you blog')
        print('Here in iNeuron we have Thanking blog, in which people who got offers can give thank note')

    def info_blog(self):
        logging.info('This method describe about information blog')
        print('iNeuron has information blogs which gives idea of each topic which though in the class and clear understing of concept')

    def type_of_blog(self, t):
        try:
            logging.debug('This method describe about which type of blogs present in iNeuron')
            if type(t) == str:
                if t == 'i' or t == 'I':
                    self.info_blog()
                elif t == 't' or t == 'T':
                    self.thank_blog()
                else:
                    raise Exception('Please enter either t/i')
            else:
                raise Exception('Entered is not a string please add string or character')
        except Exception as e:
            print(e)
            logging.exception(e)

b = Ineuron_blog()
b.info_blog()
b.type_of_blog(89)
b.type_of_blog('T')



#Example 8
class Ineuron_jobs:

    def __init__(self):
        logging.debug('We Initiated Ineuron Jobs class')
        print('Welcome to Ineuron job class')

    def who_can_apply_job(self):
        logging.info('who_can_apply_job method can describe about who can apply for job in ineuron jobs class')
        print('The one who has part of Job Guarantee Program and who completed 40% or above assignment can apply')

    def which_jobs_can_apply(self):
        logging.info('which_jobs_can_apply method describe about which jobs he can apply')
        print('Student who met criteria in respective program can apply for jobs having different levels')

    def how_to_apply(self):
        logging.info('which_jobs_can_apply method describe about how to apply jobs')
        print('Student once they met criteria can schedule Resume discussion and can apply for job')

    def other_job_info(self):
        logging.info('which_jobs_can_apply method describe about how to apply jobs')
        print('Student who completed course in one neuron can come for resume discussion and apply for job')

    def jobs(self):
        try:
            logging.info('jobs method explains about process and how to apply for job')
            self.who_can_apply_job()
            self.who_can_apply_job()
            self.how_to_apply()
            self.other_job_info()
        except Exception as e:
            print(e)
            logging.exception(e)

j = Ineuron_jobs()
j.other_job_info()
j.jobs()

#Example 9
class Ineuron_intern:

    def __init__(self):
        logging.debug('We Initiated Ineuron Internship class')
        print('Welcome to Ineuron Internship class')

    def apply_intern(self):
        logging.info('apply_intern method describe about how to apply for internship')
        print('Any student who purchased any course can apply for any type of internship with iNeuron')

    def how_to_apply_intern(self):
        logging.info('how_to_apply_intern method describe about how to apply for internship')
        print(""" First we need to  register the internship program and select domain we need to work 
                  and build a team  work on project.""")

    def adv(self):
        logging.info('adv method describe about advantages of internship')
        print('Real time project idea, Free project,connection with team, project delivery')

    def intern(self):
        try:
            logging.info("intern will describe about process of internship")
            self.apply_intern()
            self.how_to_apply_intern()
            self.adv()
        except Exception as e:
            print(e)
            logging.exception(e)

i = Ineuron_intern()
i.intern()


#Example 10
class Ineuron_hackthon:

    def __init__(self):
        logging.debug('We Initiated Ineuron category courses ')
        print('Welcome to Ineuron category courses')

    def hackton(self):
        logging.info('This method describe about ineuron hackton')
        print('Any one can apply for hackton in Ineuron')

    def winner_prize(self):
        logging.info('This method describe about prize for hackton winner ')
        print('Hackton 1st prize is 2 lakh, 2nd prize 1 lakh , 3rd prize 50k ')

    def hack_info(self):
        try:
            logging.info('This is method describe about hackton info')
            self.hackton()
            self.winner_prize()
        except Exception as e:
            logging.exception(e)

h = Ineuron_hackthon()
h.winner_prize()
h.hack_info()