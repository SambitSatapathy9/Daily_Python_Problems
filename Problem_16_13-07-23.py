#Problem 16
# Write a python program to create a class called Student with attributes name and grades (a list of integers).
#Write a method to calculate the average grade of the student.

class Student(object):
  
    def __init__(self,name,grades):
        self.name    = name
        self.grades  = grades
        
    def average(self):
        if self.grades:
            return sum(self.grades)/ len(self.grades)
        else:
            return 0
          
student = Student('Sam',[95,91,94,87,85])
average_marks = student.average()
print(f"Average grade: {average_marks}")
