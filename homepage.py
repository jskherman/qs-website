from nicegui import ui
from design import frame

from menu import create_menu


def create() -> None:
    @ui.page("/")
    def page_home():

        create_menu("Home Page")

        with frame("Home Page"):
            # message("Home Page")
            ui.label("This page is defined in a function.")
            ui.button(
                color="primary",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="secondary",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="accent",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="positive",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="negative",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="warning",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )
            ui.button(
                color="info",
                text="Click me!",
                on_click=lambda: ui.notify("Hello, World!"),
            )

        # ui.left_drawer().add_slot(ui.link("Home", "/"))
