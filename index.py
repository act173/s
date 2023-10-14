from flet import *
from flet_route import Params, Basket
import sqlite3


class IndexPage:

    user = []

    def __init__(self):
        pass

    def view(self, page: Page, params: Params, basket: Basket):


        page.title = "Assamble"

        app_view = View("/")

        div = Divider()
        page.vertical_alignment = "center"
        page.horizontal_alignment = "center"

        bar = AppBar(title = Text("     "))
        app_view.controls.append(bar)

        text = Row(controls=[Text("Assamble", size=30, weight= FontWeight.W_500)],
                   alignment=MainAxisAlignment.CENTER)
        text_under = Row(controls=[
            Text("Система школи №173 \nдля організації шкільних заходів", text_align = TextAlign.CENTER, color=colors.GREY)],
                         alignment=MainAxisAlignment.CENTER)

        but = Row([TextButton("Login", width=180)], alignment=MainAxisAlignment.CENTER)
        bar = AppBar(title=Text("   "))

        con = Container(height = 10)



        login = TextField(label="Username", border=InputBorder.UNDERLINE)
        pwd = TextField(label="Password", password=True, can_reveal_password=True, border=InputBorder.UNDERLINE)
        login_button = Row([FilledTonalButton("Увійти в систему")], alignment = MainAxisAlignment.CENTER)


        form = Container(Column([text, text_under, div, login, pwd, con, login_button]),
                         padding = 50)


        app_view.controls.append(form)

        return app_view

user = IndexPage().user