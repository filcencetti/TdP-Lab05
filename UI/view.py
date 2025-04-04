import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_course_name = None
        self.txt_result = None
        self.txt_container = None
        self._matr = None
        self._name = None
        self._surname = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_course_name = ft.Dropdown(
            label="Corso",
            width=500,
            hint_text="Selezionare un corso")

        self._controller.addcourses()

        self.btn_SearchRegistered = ft.ElevatedButton(text="Cerca iscritti",on_click=lambda e: self._controller.printstudents())
        row1 = ft.Row([self.txt_course_name, self.btn_SearchRegistered], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.update()

        # row2
        self._matr = ft.TextField(label="matricola",
                                  width=300)
        self._name = ft.TextField(label="nome",
                                  width=300)
        self._surname = ft.TextField(label="cognome",
                                     width=300)
        row2 = ft.Row(controls=[self._matr, self._name, self._surname])
        self._page.controls.append(row2)
        self._page.update()

        # row3
        self._btnSearchStudent = ft.ElevatedButton(text="Cerca studente",on_click=lambda e: self._controller.searchstudent())
        self._btnSearchCourse = ft.ElevatedButton(text="Cerca corsi",on_click=lambda e: self._controller.searchcourses())
        self._btnRegister = ft.ElevatedButton(text="Iscriviti",on_click=lambda e: self._controller.register())
        row3 = ft.Row(controls=[self._btnSearchStudent, self._btnSearchCourse, self._btnRegister],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self._page.update()

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()