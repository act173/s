from flet import *
from views.index import IndexPage
from flet_route import path, Routing
from views.details import DetailsPage

def main(page: Page):

    routes = [
        path("/", view = IndexPage().view, clear = True),
        path("/details", view=DetailsPage().view, clear=True)
    ]
    Routing(page= page, app_routes = routes)
    page.go(page.route)

app(main, view = WEB_BROWSER)