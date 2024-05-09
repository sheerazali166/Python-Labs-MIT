#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:22:38 2024

@author: sheeraz
"""

from adding_another_class import UG
from more_classes_in_hierarchy import Grad

"""EXAMPLE: GRADEBOOK"""

class Grades(object):
    
    """A mapping from students to a list of grades"""
    def __init__(self):
       
        """Create empty grade book"""
        self.students = []   # list of Student objects
        self.grades = {}     # maps idNum -> list of grades

        self.isSorted = True  # true if self.students is sorted

        
    def addStudent(self, student):
        
        """Assumes: student is of type Student
           Add student to the grade book"""
           
        if student in self.students:
            raise ValueError('Duplicate student')
        
            
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
        
        
    """
       index into dict using IdNum;
       returns a list of grades 
    """

    def addGrade(self, student, grade):
        
        """
           Assumes: grade is a float
           Add grade to the list of grades for student """
           
        """
           add to list;
           mutating existing list
        
        """
        
        try:
            """index into dict using"""
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            """return a copy"""
            raise ValueError('Student not in grade book')
            
    
    def getGrades(self, student):
        """Return a list of grades for student"""
        try: # return copy of student's grades
            "index into dict; using idNum"
            return self.grades[student.getIdNum()][:]
        except KeyError:
            "return a copy"
            raise ValueError('Student not in grade book')
            
        
            
    """EXAMPLE: GRADEBOOK"""
            
    #def allStudents(self):
    """Return a list of the students in the grade book"""
        #if not self.isSorted:
            #self.students.sort()
            #self.isSorted = True
            
    """Return a copy"""
    """return copy of list of students"""        
            
        #return self.students[:]
  
    """EXAMPLE: GRADEBOOK"""
            
    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
            
     
         
        for s in self.students:
            
            yield s
        

    
  
    """
       USE GRADEBOOK WITHOUT
       KNOWING INTERNAL DETAILS
    """
    
    def gradeReport(course):
        """Assumes: course is of type grades"""
        report = []
        
        """use method to get data; preserves information hiding"""
        for s in course.allStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
                
            try:
                """return as string, with return between each student"""
                average = tot/numGrades
                report.append(str(s) + '\'s mean grade is ' + str(average))
            except ZeroDivisionError:
                report.append(str(s) + ' has no grades')
                
                            
        return '\n'.join(report)    
            
            
    
    
print('************\\\\\\\\\\\\\\\------???------\\\\\\\\\\\\\\\***************')
    
"""SETTING UP AN EXAMPLE"""


ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)

g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()

six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)

six00.addStudent(ug4)
six00.addStudent(ug3)


"""RUNNING AN EXAMPLE"""

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

avg = (100 + 25 + 95 + 85 + 75) / 5
print("Average: ", avg)

print(Grades.gradeReport(six00))


"""RUNNING AN EXAMPLE 2"""

print("********************||||||||||************************")

average = (90 + 45 + 80 + 75) / 4
print("Average: ", average)


six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print(Grades.gradeReport(six00))


"""
   USING EXAMPLE
   could list all students using  
"""

print("||||||||||||||||****************||||||||||||||||")

for s in six00.allStudents():
    print(s)
    
"""
     prints out the list of student names sorted by idNum
     why not just do
""" 

print("*********************")

for s in six00.students:
    print(s)
    
    
    
    
    
    
    
   
    






























    
                
            
    
    
           
           
           
           