#!/usr/bin/env python
# coding: utf-8

# In[19]:


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
obj = Student(123457, "Course1")
obj.Add()
obj = Student(123456, "Course2")
obj.Add()
obj = Student(123459, "Course4")
obj.Add()
obj = Student(123458, "Course3")
obj.Add()

# Retreive will get the min student id and deletes it from the collection
print(obj.Retreive())
print(obj.dictStudents)
print(obj.sortedDictStudents)


# In[ ]:




