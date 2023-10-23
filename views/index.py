from flet import *
from flet_route import Params, Basket

class IndexPage:
    def __init__(self):
        pass
    def view(self, page: Page, params: Params, basket: Basket):
        page.title = "Gathery"
        body = Column()

        body.controls.append((TextButton("Go to Details", on_click = lambda _ : page.go("/details"))))
        page.update()

        return View("/", controls = [body])
