""" class Add:
    x = 10
    y = 20
    def sqr(self,a):
        return a**2
s = Add()#object creating

class Student:
   name = 'Sateesh'
   Rollno = '181abc537'
   def display(self):
       print('hello {} number is {}'.format(Student.name,Student.Rollno))
class CsE:
    def __init__(self,name,section):
        self.name = name
        self.section = section
        print('hello',self.name,self.section)
    def m(self):
	    print('this is method')
name = input('enter name:')
section = input('enter section')
c = CsE(name,section)
c.m()
c.m()
c.m()

class Parent:
   money = 100000
   land = 10
  
class Child(Parent):
	study = 'B Tech'
	def properties(self):
		print('child properties')
c = Child()
print(c.money)
print(c.land)
print(c.study)
c.properties()"""
class Parent:
   money = 100000
   land = 10
  
class Child1(Parent):
	study = 'B Tech'
	def prop(self):
		print('child1 properties')
class Child2(Parent):
	study = 'Degree'
	def properties(self):
		print('child2 properties')
c1 = Child1()
print(c1.money)
print(c1.land)
print(c1.study)
c1.prop()
c2 = Child2()
print(c2.money)
print(c2.land)
print(c2.study)
c2.properties()
