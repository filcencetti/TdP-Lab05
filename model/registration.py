from database import registration_DAO

class Registration:
    def __init__(self):
        self.new_matr = None
        self.new_course = None
        self.list_registrations = registration_DAO.addregistration()
        pass

