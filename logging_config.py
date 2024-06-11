"""
Module to configure logging for the application as JSON logs via the
`pythonjsonlogger` library.

The configuration is defined in a dictionary and passed to
`logging.config.dictConfig()`. The configuration is set up to log to both
stdout and a file named `app.log`. The log level is set to `INFO` in production
and `DEBUG` in development.
"""

# Standard library imports
import os
import re
import logging
import logging.config
import datetime as dt
from functools import reduce

# Third party imports
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv

# Preamble
load_dotenv()


class SensitiveDataFilter(logging.Filter):
    """
    A logging filter that redacts sensitive data from log messages using
    regular expressions defined in a file named `regex.txt`. The filter is
    applied to both the stdout and file handlers.

    Based on https://betterstack.com/community/guides/logging/python/python-logging-best-practices/.
    """

    def __init__(self, patterns_file="regex.txt"):
        """
        Initialize the filter with a list of compiled regular expressions.
        """
        super().__init__()
        self.regex_patterns = self.load_patterns(patterns_file)

    def load_patterns(self, file_path):
        """
        Load regular expressions from a file and compile them.
        """

        patterns = []
        with open(file_path, "r") as file:
            for line in file:
                # Remove comments and strip whitespace
                pattern = line.split("#")[0].strip()
                if pattern:
                    patterns.append(re.compile(pattern))
        return patterns

    def filter(self, record):
        # Format the log message with the arguments if they exist
        if record.args:
            record.msg = record.msg % record.args
            record.args = ()

        # Modify the log record to mask sensitive data
        record.msg = self.mask_sensitive_data(record.msg)
        return True

    def mask_sensitive_data(self, message):
        """
        Mask sensitive data in the log message using the compiled regular
        expressions.
        """
        # Redact all data that matches the given patterns
        return reduce(
            lambda msg, p: p.sub("[REDACTED]", msg), self.regex_patterns, message
        )


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "sensitive_data_filter": {
            "()": SensitiveDataFilter,
        }
    },
    "formatters": {
        "json": {
            "format": "%(asctime)s %(name)s %(threadName)s %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        },
        "simple": {
            "format": "%(asctime)s -- %(name)s -- %(threadName)s -- %(levelname)s -- %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            "class": "logging.Formatter",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "simple",
            "filters": ["sensitive_data_filter"],
        },
        "app": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/app.log",
            "when": "midnight",
            "backupCount": 30,
            "utc": True,
            "formatter": "json",
            "filters": ["sensitive_data_filter"],
        },
    },
    "loggers": {
        "": {
            "handlers": ["stdout", "app"],
            "level": (
                "INFO"
                if os.environ.get("ENVIRONMENT").strip().lower() == "production"
                else "DEBUG"
            ),
        }
    },
}

logging.config.dictConfig(LOGGING)


# Example usage
if __name__ == "__main__":
    logger = logging.getLogger("logging_config")

    logger.warning(
        "This message contains a credit card number: %s.",
        "1234 5678 9101 1121",
    )
