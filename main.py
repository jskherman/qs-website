#!/usr/bin/env python3

"""
The main entrypoint for the NiceGUI-based application for my quantified self
project that analyzes and visualizes various datasets I have collected about
myself such as local weather, exercise, time-tracking, and many others.

Execute this simply by: `python main.py`.

Remember to set ui.run(reload=False) when pushing to production.
"""

# =============================================================================
# MARK: imports
# =============================================================================

# Standard library imports
import os
import logging

# import datetime as dt

# Third party imports
from dotenv import load_dotenv
from nicegui import ui, app

# Local imports
# import design as ds
import logging_config  # noqa: F401, pylint: disable=unused-import

# =============================================================================
# MARK: Preamble
# =============================================================================

# Load environment variables
load_dotenv()
ENV = os.environ["ENVI"].strip().lower()

# Setup logging
logger = logging.getLogger(__name__)


def startup_sequence() -> None:
    """
    This function contains the startup sequence for the application. It is
    called at the beginning of the main() function.
    """

    if ENV == "production":
        logger.info("Running in production mode.")
    else:
        logger.info("Running in development mode.")

    logger.info("Starting the application...")

    # Load the design system
    # ds.load_design_system()

    # Load the design
    # ds.load_design()

    # Load the standard components
    # ds.load_standard_components()

    # Load the page layout
    # ds.load_page_layout()

    # Load the application logic
    # ds.load_application_logic()

    logger.info("Application started.")


# =============================================================================
# MARK: main()
# =============================================================================
def main() -> None:
    """
    This is the main function. Need I say more?
    """

    # Run the startup sequence
    app.on_startup(startup_sequence)

    def notify_me():
        ui.notify("Hello, World!")

    ui.button("Click me!", on_click=notify_me)

    if ENV == "production":
        if (
            os.environ.get("NATIVE") is not None
            and os.environ.get("NATIVE").strip().lower() == "true"
        ):
            ui.run(reload=False, native=True, favicon="static/favicon.ico")
        else:
            ui.run(reload=False, favicon="static/favicon.ico")
    else:
        ui.run(favicon="static/favicon.ico")


if __name__ in {"__main__", "__mp_main__"}:
    main()
