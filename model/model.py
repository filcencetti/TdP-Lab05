import model.studente as s
import model.corso as c
import model.registration as d
from database.registration_DAO import addstudent

class Model:
    def __init__(self):
        self.students = s.Student().list_students
        self.courses = c.Course().list_courses
        self.registrations = d.Registration()
        self.coursestudent = []

    def register_new_course(self):
        addstudent(self.registrations.new_matr,self.registrations.new_course)


