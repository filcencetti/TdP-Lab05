import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_registered(self):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        self.val = True
        course_name = self._view.txt_course_name.value
        if course_name is None or course_name == "":
            self._view.create_alert("Inserire il corso!")
            self._view._page.update()
            self.val = False
            return

    def handle_matr(self):
        self.val = True
        if self._view._matr.value is None or self._view._matr.value == "":
            self._view.create_alert("Inserire la matricola!")
            self._view.update_page()
            self.val = False
            return

    def printstudents(self):
        self.handle_registered()
        self._view.txt_result.controls = []
        for registration in self._model.registrations.list_registrations:
            if self._view.txt_course_name.value == registration["codins"]:
                for student in self._model.students:
                    if student["matricola"] == registration["matricola"]:
                        self._view.txt_result.controls.append(
                                ft.Text(f"{student["cognome"]},{student["nome"]}, ({student["matricola"]})"))
                        self._model.coursestudent.append(student)
        if self._view.txt_course_name.value != "" and self._view.txt_course_name.value is not None:
            self._view.txt_result.controls.insert(0, ft.Text(f"Ci sono {len(self._view.txt_result.controls)} iscritti al corso:"))
            self._view._page.update()
            return

    def addcourses(self):
        for course in self._model.courses:
            self._view.txt_course_name.options.append(ft.dropdown.Option(text=f"{course["nome"]} ({course["codins"]})",key=course["codins"]))

    def searchstudent(self):
        self.handle_registered()
        if self._view._matr.value is None or self._view._matr.value == "":
            self._view.create_alert("Inserire la matricola!")
            self._view.update_page()


        for registration in self._model.registrations.list_registrations:
            if self._view.txt_course_name.value == registration["codins"]:
                for student in self._model.students:
                    if student["matricola"] == registration["matricola"]:
                        self._model.coursestudent.append(student)
        for student in self._model.coursestudent:
            if str(student["matricola"]) == self._view._matr.value:
                self._view._name.value = student["nome"]
                self._view._name.disabled = True
                self._view._surname.value = student["cognome"]
                self._view._surname.disabled = True
        self._view.update_page()

    def searchcourses(self):
        self._view.txt_result.controls = []
        for registration in self._model.registrations.list_registrations:
            if self._view._matr.value == str(registration["matricola"]):
                for course in self._model.courses:
                    if course["codins"] == registration["codins"]:
                        self._view.txt_result.controls.append(
                            ft.Text(f"{course["nome"]} ({course["codins"]})"))

        self._view.txt_result.controls.insert(0, ft.Text(
                    f"Risultano {len(self._view.txt_result.controls)} corsi:"))
        self._view._page.update()
        return

    def register(self):
        self.val = True
        self.handle_registered()
        self.handle_matr()
        print(self.val)
        if self.val:
            self._model.registrations.new_matr = self._view._matr.value
            self._model.registrations.new_course = self._view.txt_course_name.value
            self._model.register_new_course()
