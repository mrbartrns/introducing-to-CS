from people import *

# people부터 시작하여 다시 짜보기
#sort use __eq__
class Grades(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True
    
    def addStudent(self, student):
        if student in self.students:
            raise ValueError("Duplicate Student")
        self.students.append(student)
        self.grades[student.getIdNum()] = [] #score is in the list
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError("Student NOT in grade book")

    def getGrade(self, student):
        try:
            return self.grades[student.getIdNum()][:] #copy the list
        except KeyError:
            raise ValueError("Student NOT in grade book")

    def allStudents(self):
        if not self.isSorted:
            self.students.sort() # sort by id
            self.isSorted = True
        return self.students[:] # return copy of list of students
    
def gradeReport(course):
    """course: type of Grades"""
    report = []
    for s in course.allSudents(): # expected result: [a, b, c]
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s): # expected result: {s: [a, b, c]}
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(f"{s} 's mean grade is {average}")
        except ZeroDivisionError:
            report.append(f"{s} has no grades")
    return '\n'.join(report)