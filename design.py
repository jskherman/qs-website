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

# Third party imports
from dotenv import load_dotenv
from nicegui import ui

# Local imports
import logging_config  # noqa: F401, pylint: disable=unused-import

# =============================================================================
# MARK: Preamble
# =============================================================================

load_dotenv()
ENV = os.environ.get("ENVI").strip().lower()

# Setup logging
logger = logging.getLogger(__name__)


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
