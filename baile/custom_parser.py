from pathlib import Path
import argparse

# Set default path for mocks
dir_in = Path(__file__).resolve().parent.parent / "tests" / "mocks"


# Customize parser
def customize_parser():
    parser_logging = argparse.ArgumentParser()
    parser_logging.add_argument(
        "--human",
        action="store_true",
        dest="human",
        default=True,
        help="Format the logs for humans",
    )
    parser_logging.add_argument(
        "--structured",
        action="store_false",
        dest="human",
        help="Format the logs as JSON",
    )  # app.py
    parser_logging.add_argument(
        "--n_tabs", type=int, help="Number of tabs, use it in app.py"
    )  # app.py
    parser_logging.add_argument(
        "--mock_path",
        type=str,
        default=dir_in,
        help="Directory of mock file/s, use it in app.py",
    )  # app.py
    parser_logging.add_argument(
        "--benchmark", action="store_true", help="Enable benchmarking, use it in app.py"
    )  # app.py
    parser_logging.add_argument(
        "--headless",
        action="store_true",
        dest="headless",
        default=True,
        help="Set headless as True, use it in app.py",
    )  # app.py
    parser_logging.add_argument(
        "--no_headless",
        action="store_false",
        dest="headless",
        help="Set headless as False, use it in app.py",
    )  # app.py
    return parser_logging
