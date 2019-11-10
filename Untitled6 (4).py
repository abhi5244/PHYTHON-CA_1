#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
class Student:
    dictStudents = dict()
    def __init__(self, StudentId, CourseName):
        Student.StudentId = StudentId
        Student.CourseName = CourseName
    def Add(self):
        Student.dictStudents.update({Student.StudentId: Student.CourseName})
        
    def Retreive(self):
        minStudentId = sys.maxsize
        for x in Student.dictStudents.keys():
             if (x < minStudentId):
                minStudentId = x
        del Student.dictStudents[minStudentId]
        return minStudentId

# admins process students in the order it was received

obj = studentprocessing()
obj1 = student(123456, "course b01")
obj.Add(obj1)
obj2 = student(123457, "course b02")
obj.Add(obj2)
obj3 = student(123458, "course b03")
obj.Add(obj3)
obj4 = student(123459, "course b04")
obj.add(obj4)
       
        


# In[ ]:




