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
from nicegui import ui

# Local imports
# import design as ds
import logging_config

# =============================================================================
# MARK: Preamble
# =============================================================================

# Load environment variables
load_dotenv()
ENV = os.environ.get("ENVIRONMENT").strip().lower()

# Setup logging
logger = logging.getLogger(__name__)


# =============================================================================
# MARK: main()
# =============================================================================
def main() -> None:
    """
    This is the main function. Need I say more?
    """

    if os.environ.get("ENVIRONMENT").strip().lower() == "production":
        logger.info("Running in production mode.")
        # ui.run(reload=False)
    else:
        logger.info("Running in development mode.")
        # ui.run()


if __name__ == "__main__":
    main()
