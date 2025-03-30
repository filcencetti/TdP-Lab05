from database import studente_DAO


class Student:
    def __init__(self):
        self.list_students = studente_DAO.addstudent()
        pass

