from typing import Optional

from nicegui import ui, app

import svg


def create_menu(page_title: str, menu: Optional[ui.left_drawer] = None) -> None:

    pages = {
        "Home": "/",
        "About": "/about",
    }

    dark_mode = ui.dark_mode(
        value=app.storage.browser.get("dark_mode"),
        on_change=lambda e: ui.run_javascript(
            f"""
        fetch('/dark_mode', {{
            method: 'POST',
            headers: {{'Content-Type': 'application/json'}},
            body: JSON.stringify({{value: {e.value}}}),
        }});
    """
        ),
    )

    with ui.header().classes(
        "items-center row duration-200 p-0 px-4 no-wrap"
    ) as header:

        if menu:
            ui.button(on_click=menu.toggle, icon="menu").props(
                "flat color=white round"
            ).classes("lg:hidden")

        ui.label("howis.jskherman.com").classes("text-md")
        ui.space()
        ui.label(page_title).classes("font-bold text-xl")
        ui.space()

        for page, url in pages.items():
            ui.link(page, url).classes(
                "p-2 text-white hover:text-white hover:bg-opacity-25 no-underline"
            )

        with ui.element().classes("max-[420px]:hidden").tooltip("Change theme"):
            ui.button(
                icon="dark_mode", on_click=lambda: dark_mode.set_value(None)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", value=True
            )
            ui.button(
                icon="light_mode", on_click=lambda: dark_mode.set_value(True)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", value=False
            )
            ui.button(
                icon="brightness_auto", on_click=lambda: dark_mode.set_value(False)
            ).props("flat fab-mini color=white").bind_visibility_from(
                dark_mode, "value", lambda mode: mode is None
            )

        with ui.link(target="https://github.com/zauberzeug/nicegui/").classes(
            "max-[365px]:hidden"
        ).tooltip("GitHub"):
            svg.github().classes("fill-white scale-125 m-1")

    # with ui.footer(value=False) as footer:
    #     ui.label("Footer")

    # with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    #     ui.button(on_click=footer.toggle, icon="contact_support").props("fab")
