import sys
import logging
import inspect

# new constant
DEBUG2 = 5

# Create the logging
basicConfig = logging.basicConfig
logging.addLevelName(DEBUG2, "DEBUG2")

# Set logger
logger = logging.getLogger(__name__)

# Set handler
handler = logging.StreamHandler(stream=sys.stderr)
logger.addHandler(handler)


# Improve the name
def _get_name():
    upper_frame = inspect.currentframe().f_back.f_back
    module_frame = inspect.getmodule(upper_frame)
    module = (
        module_frame.__name__
        if module_frame
        else inspect.getmodule(upper_frame.f_back).__name__
    )
    module_function = upper_frame.f_code.co_name
    return f"{module}:{module_function}()"


# Custom debug with custom level
def debug2(message):
    function = inspect.stack()[0].function
    logger._log(
        DEBUG2, f"{function.upper()}:{_get_name()}: {message}", ()
    )  # The () is for the empty args


# Overwrite function
def debug1(message):
    function = inspect.stack()[0].function
    logger.debug(f"{function.upper()}:{_get_name()}: {message}")


# Overwrite function
def info(message):
    function = inspect.stack()[0].function
    logger.info(f"{function.upper()}:{_get_name()}: {message}")


# Overwrite function
def error(message):
    function = inspect.stack()[0].function
    logger.error(f"{function.upper()}:{_get_name()}: {message}")


# Overwrite function
def warning(message):
    function = inspect.stack()[0].function
    logger.warning(f"{function.upper()}:{_get_name()}: {message}")


# Overwrite function
def critical(message):
    function = inspect.stack()[0].function
    logger.critical(f"{function.upper()}:{_get_name()}: {message}")
