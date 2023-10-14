from flet import *

def main(page: Page):
    page.add(Text("Hllo"))
    page.update()

app(main, view = WEB_BROWSER)
