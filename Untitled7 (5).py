#!/usr/bin/env python
# coding: utf-8

# In[10]:


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
        del Student.sortedDictStudents[FirstStudentID]
        return Student.firstStudentDict
    
    
    
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




