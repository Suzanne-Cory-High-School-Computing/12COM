# This is the code in Practice booklet 3 OOP in python
# The comments below explain how inheritance works (see comments on Parent class)

class Parent: # we declare a new class called "Parent"
    def __init__(self,a): # constructor is automatically called every time we create a new object of class Parent
        self.a = a # class Parent has a variable called a; each object created belonging to this class will have its own variable a
    
    def method1(self):
        return self.a*2 # class Parent has a method called method1 which is whatever a is declared as, doubled
    
    def method2(self):
        return self.a+'!!!' # class Parent also has a method called method2 which is whatever a is declared as, followed by !!!
    
class Child(Parent): # class Child is declared to be another class which inherits from class Parent
    def __init__(self,a,b): # constructor is automatically called every time we create a new object of class Child
        self.a = a # class Child has a variable called a; each object created belonging to this class will have its own variable a
        self.b = b # class Child has a variable called b; each object created belonging to this class will have its own variable b

    def method1(self):
        return self.a*7 # class Child has a method called method1 which is whatever a is declared as, multiplied 7 times
    
    def method3(self):
        return self.a + self.b # class Child has a method called method2 which is whatever a is declared as, concatenated with whatever b is declared as
    
    # notice that class Child has no method called method2!
    
p = Parent('hi')
c = Child('hi','bye')

print('Parent method 1: ', p.method1()) # refers to method1 in the parent class
print('Parent method 2: ', p.method2()) # refers to method2 in the parent class
print()
print('Child method 1: ', c.method1()) # refers to method1 in Child class ("overrides" parent class method1)
print('Child method 2: ', c.method2()) # refers to method2 in Parent class because Child class did not declare its own method2 (inheritance)
print('Child method 3: ', c.method3()) # refers to method3 in Child class ("overrides" parent class method3)
