class Student:

    def __init__(self, name, rollNumber, marks):
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollNumber)
        print("Marks:", self.marks)

    def calculateGrade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 35:
            return "D"
        else:
            return "Fail"

    def updateMarks(self, newMarks):
        self.marks = newMarks
        print("Marks updated successfully")


def searchStudent(students, rollNumber):

    for student in students:
        if student.rollNumber == rollNumber:
            return student

    return None


def findHighestMarks(students):

    highest = students[0]

    for student in students:
        if student.marks > highest.marks:
            highest = student

    return highest


def startprogram():

    student1 = Student("Karan", 101, 85)
    student2 = Student("Riya", 102, 92)
    student3 = Student("Ankitha", 103, 76)

    students = [student1, student2, student3]

    print("----- ALL STUDENTS -----")

    for student in students:
        student.display()
        print("Grade:", student.calculateGrade())
        print()

    print("----- SEARCH STUDENT -----")

    student = searchStudent(students, 102)

    if student is not None:
        student.display()
        print("Grade:", student.calculateGrade())
    else:
        print("Student not found")

    print()

    print("----- UPDATE MARKS -----")

    student = searchStudent(students, 101)

    if student is not None:
        student.updateMarks(95)
        student.display()

    print()

    print("----- HIGHEST MARKS -----")

    highest = findHighestMarks(students)

    highest.display()
    print("Grade:", highest.calculateGrade())


startprogram()