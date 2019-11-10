#!/usr/bin/env python
# coding: utf-8

# In[8]:


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
        for stuID in SortedList:
                Student.sortedDictStudents.update({stuID: Student.dictStudents[stuID]})
        FirstStudentID = SortedList[0]            
        Student.firstStudentDict.clear()
        Student.firstStudentDict.update({FirstStudentID: Student.dictStudents[FirstStudentID]})
        return Student.firstStudentDict


# In[ ]:




