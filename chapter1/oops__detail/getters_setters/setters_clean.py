'''
setters = set the values of the attribute

they protect the attribute by providing an indirect way to access them and modify them 

We can make the attributes non-public and still provide a way to work with them indirectly.
'''

'''

setters naming convention:

set_+<attribute>

calling a setter 
<object>.set_<attribute>(new_name)

for eg:
set_name , set_address , set_color
'''

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def set_grade(self, new_grade):
        if isinstance(new_grade, int):
            self.grade = new_grade 
        else:
            print("please enter a valid grade")


student = Student("safal", 6)

print(f"Student's name was {student.name} and has grade {student.grade}")

student.set_grade(9)

print(f"Student's name was {student.name} and has new grade {student.grade}")
