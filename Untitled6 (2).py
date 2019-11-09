#!/usr/bin/env python
# coding: utf-8

# In[5]:


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
       
        


# In[ ]:




