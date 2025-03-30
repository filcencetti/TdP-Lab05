from database import corso_DAO


class Course:
    def __init__(self):
        self.list_courses = corso_DAO.addcourses()