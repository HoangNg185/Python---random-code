def spacebreak():
    for i in range(2):
        print(' ')
class A:
    def __init__(self,A1,A2):
        self.A1=A1
        self.A2=A2
    def __str__(self):
        return 'A class Self'
    def my_self_function(self):
        print(f'Hello this is my created self_function {self.A1}')
p1=A('AA1  ','AA2')
print(p1.A1)
print(p1)

p1.my_self_function()
class B:
    def __init__(randomsilly_selfname, B1, B2):
        randomsilly_selfname.B1=B1
        randomsilly_selfname.B2=B2
    def __str__(self):
        return 'random B class'
    def myself_B_function(sedaslkjdslf):
        print(f'class B is {sedaslkjdslf.B2}')
p2=B('first of B','second of B')
p2.myself_B_function()
spacebreak()

class class_A1(A):
    def my_self_function_2(self):
        print(f'kjsadlkjdas')
p11=class_A1('Liam','Nguyen')
p11.my_self_function()
