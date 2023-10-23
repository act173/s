from flet import *
from flet_route import Params, Basket

class DetailsPage:
    def __init__(self):
        pass
    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Gathery Details"
        body = Column()

        body.controls.append((TextButton("Go Home", on_click = lambda _ : page.go("/"))))
        page.update()

        return View("/details", controls = [body])
