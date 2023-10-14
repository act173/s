from flet import *
from flet_route import path, Routing
from index import IndexPage

def main(app_page: Page):

    theme = Theme()
    theme.page_transitions.macos = PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.ios = PageTransitionTheme.FADE_UPWARDS
    app_page.theme = theme

    app_routes = [
        path(url = "/", clear=True, view=IndexPage().view)
    ]

    Routing(page = app_page, app_routes = app_routes)
    app_page.go(app_page.route)


app(target=main, view = WEB_BROWSER)