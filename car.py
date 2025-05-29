class Car:
    wheel=4             
    def __init__(self,name,year,color):
        self._name=name
        self.__year=year   
        self.color=color    
    def _viewcar(self):#getter
        print(self.name,self.year)
    def update(self,xd):#setter
        self.name=xd

    


c1=Car('hundai',2004,'red')

c1.viewcar()




#instance method
#accesors           #getters
#mutators           #setters


#class method
#static method



# a=7
# b=10
# a,b=7,10
# class Point:

#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
 
#     def reset(self):
#         self.move(0,0)
#         print(self.x,self.y)

#     def move(self,c,d):
#         self.x=c
#         self.y=d
#         print(self.x,self.y)

#     def xm(self,xx):
#         self.x=xx
# p1=Point(1,2)

# print(p1.x)
# p1.move(3,4)
# p1.xm(7)



# def a():
#     def b():
#         return 'hari'
#     b()
# c1=Car('porshe')
# # c2=Car('city')
# # c1.namez()
# # c1.update('jojojo')
# # c1.namez()
# c1.sumz()

# class A:
#     def __init__(self):
#         print('hello')
#     def task1():
#         print('task1')

# class B(A):
#     def __init__(self):
#         print('hai')
#     def task2():
#         print('task2')

# class C(B):
#     def __init__(self):
#         print('ola')
#     def task3():
#         print('task3')                

# c=C()

# class Emplooyee:

#     def __init__(self):
#        self.lap=self.Laptop()
        
#     class Laptop:
#         def __init__(self):
#             self.brand='dell'


# e=Emplooyee()
# print(e.lap.brand)


# class Person1:

#     def __init__(self):
#         print('person1')

#     def run(self):
#         print('person one is running')
    

# class Person2():

#     def __init__(self):
      
#         print('person2')
      

#     def eat(self):
#         print('person 2 is eating')
      

#     def walk(self):
#         print('person 2 is walking')  

                  


# class Person3(Person2,Person1):
   
#     def __init__(self):
      
#         super().__init__()
      
    
#     def learning(self): #stub
#         print('Person3 is learning')

#     def writing(self):
#         print("Person 3 is Writing")

#     def sleep(self):
#         print('person3 is sleeping')       



# p3=Person3()

# class Student:

#     def __init__(self,name,year,lnm):
#         self.name = name
#         self.year=year
#         self.l1=self.Laptop(lnm)


#     class Laptop:

#         def __init__(self,lname):
#             self.lapname=lname

# s1=Student('hari',2019,'dell')

# print(s1.l1.lapname)