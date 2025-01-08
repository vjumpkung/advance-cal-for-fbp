import sys
import platform
import logging

MIN_PYTHON_VERSION = (3, 10, 0)
MAX_PYTHON_VERSION = (3, 13, 0)

# Get Python information

# Print Python information


def check_python_version():
    """
    Check if the current Python version is within the acceptable range.
    Returns:
        bool: True if the current Python version is valid, False otherwise.
    """
    logging.debug("Checking Python version...")
    try:
        current_version = sys.version_info
        logging.info(f"Python version is {sys.version}")

        if not (MIN_PYTHON_VERSION <= current_version < MAX_PYTHON_VERSION):
            logging.error(
                f"The current version of python ({sys.version}) is not supported."
            )
            logging.error("The Python version must be >= 3.10.9 and < 3.13.0.")
            return False
        return True
    except Exception as e:
        logging.error(f"Failed to verify Python version. Error: {e}")
        return False
