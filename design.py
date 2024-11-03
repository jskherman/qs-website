"""
This module is for specifying the design system and design of the quantified
self application. The typography, colors, and other design elements are defined
here. Several standard components are also defined here, such as buttons,
cards, and forms. Styling is done with Tailwind CSS classes.

This is a separate module from main.py to keep the main module clean and focused
on the application logic.
"""

# =============================================================================
# MARK: imports
# =============================================================================
# Standard library imports
import os
import logging
from contextlib import contextmanager


# Third party imports
from dotenv import load_dotenv
from nicegui import ui

# Local imports
# import logging_config  # noqa: F401, pylint: disable=unused-import

# =============================================================================
# MARK: Preamble
# =============================================================================

load_dotenv()
ENV = os.environ.get("ENVI").strip().lower()

# Setup logging
logger = logging.getLogger(__name__)

# =============================================================================
# MARK: Design
# =============================================================================

color_palette = {
    "primary": "#006A8A",
    "secondary": "#08415C",
    "accent": "#cf3965",
    "positive": "#3fa63f",
    "negative": "#ee5f5b",
    "warning": "#FFBD00",
}


# =============================================================================
# MARK: Components
# =============================================================================


class message(ui.label):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.classes("text-h4 text-grey-8")


@contextmanager
def frame(page_title: str):
    """
    Custom page frame to share the same styling and behavior across all
    pages.
    """

    ui.colors(
        primary=color_palette["primary"],
        secondary=color_palette["secondary"],
        accent=color_palette["accent"],
        positive=color_palette["positive"],
        negative=color_palette["negative"],
        warning=color_palette["warning"],
    )

    yield


@contextmanager
def left_drawer():
    """
    Custom left_drawer frame
    """

    with ui.left_drawer() as drawer:
        yield


# =============================================================================
# MARK: main()
# =============================================================================
def main() -> None:
    """Main function for the design module."""

    logger.warning(
        "The design module was ran as a script. This is not the intended behavior."
    )


if __name__ == "__main__":
    main()
