#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
class Student:
    dictStudents = dict()
    def __init__(self, StudentId, CourseName):
        Student.StudentId = StudentId
        Student.CourseName = CourseName
    def Add(self):
        Student.dictStudents.update(Student.StudentId: Student.CourseName)


# In[ ]:




