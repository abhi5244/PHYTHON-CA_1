#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
class Student:
    dictStudents = dict()
    sortedDictStudents = dict()
    firstStudentDict = dict()
    def __init__(self, StudentId, CourseName):
        Student.StudentId = StudentId
        Student.CourseName = CourseName
    def Add(self):
        Student.dictStudents.update({Student.StudentId: Student.CourseName})
        Student.sortedDictStudents.update({Student.StudentId: Student.CourseName})
    def Retreive(self):
        SortedList = sorted(Student.sortedDictStudents)
        if (SortedList == []):
            return []
    else:
            Student.sortedDictStudents.clear()


# In[ ]:




