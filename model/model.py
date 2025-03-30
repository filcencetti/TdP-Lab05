import model.studente as s
import model.corso as c


class Model:
    def __init__(self):
        self.students = s.Student().list_students
        self.courses = c.Course().list_courses

