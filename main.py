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
import asyncio
import logging

# import datetime as dt

# Third party imports
import schedule
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

    # Schedule the jobs
    # ...

    logger.info("Application started.")


async def run_jobs() -> None:
    """
    Asynchronous function that schedules and runs jobs based on a predefined schedule.

    This function calculates the number of seconds until the next job is scheduled to run,
    sleeps for that amount of time, and then runs the pending job. It continues this process
    until there are no more jobs scheduled.
    """
    # Get the number of seconds until the next job
    seconds = schedule.idle_seconds()

    # Run the job scheduler
    while seconds is not None:
        # If there are seconds to wait
        if seconds > 0:
            # Sleep exactly the right amount of time to the next job
            await asyncio.sleep(seconds)
        schedule.run_pending()
        seconds = schedule.idle_seconds()

    # # Way: Run the job scheduler continuously
    # while True:
    #     schedule.run_pending()
    #     await asyncio.sleep(0.1)


# =============================================================================
# MARK: main()
# =============================================================================
def main() -> None:
    """
    This is the main function. Need I say more?
    """

    # Run the startup sequence
    app.on_startup(startup_sequence)
    app.on_startup(run_jobs)

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
