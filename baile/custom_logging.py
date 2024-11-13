import sys
import json
import time
import logging
import inspect
from .custom_parser import customize_parser

# new constant
DEBUG2 = 5

# Create the logging
basicConfig = logging.basicConfig
logging.addLevelName(DEBUG2, "DEBUG2")

# Set logger
logger = logging.getLogger(__name__)

# Create handler
handler = logging.StreamHandler(stream=sys.stderr)

# parser
parser = customize_parser()

# Get the Format
arg_logging = vars(parser.parse_args())

# Create Formatter
if arg_logging["human"]:
    formatter = logging.Formatter("%(asctime)s - %(message)s")  # TODO

# Customize logger
if arg_logging["human"]:
    handler.setFormatter(formatter)
logger.addHandler(handler)


# Improve the name
def _get_name():
    level = inspect.currentframe().f_back.f_code.co_name
    upper_frame = inspect.currentframe().f_back.f_back
    module_frame = inspect.getmodule(upper_frame) or inspect.getmodule(
        upper_frame.f_back
    )
    package = module_frame.__package__
    file = module_frame.__name__
    module_function = (
        upper_frame.f_code.co_name if hasattr(upper_frame, "f_code") else None
    )
    if arg_logging["human"]:
        if module_frame:
            return f"{level.upper()} - {package}:{file}:{module_function}()"
        return f"{level.upper()} - {package}:{file}"
    else:
        return level.upper(), package, file, module_function


# This print the structured format
def print_structured(message, tag, level, package, file, module_function):
    log = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "level": level,
        "package": package,
        "file": file,
        "module_function": module_function,
        "message": message,
        "tag": tag,
    }
    print(json.dumps(log, indent=4))


# Custom debug with custom level
def debug2(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.log(DEBUG2, f"{_get_name()}: {message} ({tag})")
    else:
        logger.log(DEBUG2, f"{_get_name()}: {message}")


# Wrap function
def debug1(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.debug(f"{_get_name()}: {message} ({tag})")
    else:
        logger.debug(f"{_get_name()}: {message}")


# Wrap function
def info(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.info(f"{_get_name()}: {message} ({tag})")
    else:
        logger.info(f"{_get_name()}: {message}")


# Wrap function
def warning(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.warning(f"{_get_name()}: {message} ({tag})")
    else:
        logger.warning(f"{_get_name()}: {message}")


# Wrap function
def error(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.error(f"{_get_name()}: {message} ({tag})")
    else:
        logger.error(f"{_get_name()}: {message}")


# Wrap function
def critical(message, tag=None):
    if not arg_logging["human"]:
        level, package, file, module_function = _get_name()
        print_structured(message, tag, level, package, file, module_function)
        return
    if tag:
        logger.critical(f"{_get_name()}: {message} ({tag})")
    else:
        logger.critical(f"{_get_name()}: {message}")
