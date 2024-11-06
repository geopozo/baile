from time import process_time
from pathlib import Path
import sys
import json
import argparse
import asyncio
import logging
import baile

# Extract jsons of mocks
dir_in = Path(__file__).resolve().parent / "mocks"
results_dir = Path(__file__).resolve().parent / "images"

parser = argparse.ArgumentParser()
parser.add_argument("--n_tabs", type=int, help="Number of tabs")
parser.add_argument(
    "--mock_path", type=str, default=dir_in, help="Directory of mock file/s"
)
parser.add_argument("--benchmark", action="store_true", help="Enable benchmarking")
parser.add_argument(
    "--headless",
    action="store_true",
    dest="headless",
    default=True,
    help="Set headless as True",
)
parser.add_argument(
    "--no_headless", action="store_false", dest="headless", help="Set headless as False"
)
args = parser.parse_args()
arg_dict = vars(args)

# Improve the defaults
if arg_dict["benchmark"] and not arg_dict["n_tabs"]:
    arg_dict["n_tabs"] = 1
elif not arg_dict["benchmark"] and not arg_dict["n_tabs"]:
    arg_dict["n_tabs"] = 4

# Get logger and set handler
logging.StreamHandler(stream=sys.stderr)
relative_path = Path(__file__).relative_to(Path.cwd())
logger = logging.getLogger(str(relative_path))

# Function to process the images
async def process_images():
    try:
        await baile.create_image(
            path_figs=arg_dict["mock_path"],
            path=str(results_dir),
            debug=True,
            num_tabs=arg_dict["n_tabs"],
            headless=arg_dict["headless"],
        )
        return "Successful"
    except Exception as e:
        logger.error("No to image".center(30, "%"))
        logger.error(e)
        logger.error("***")
        return e


# Run the loop
if __name__ == "__main__":
    if arg_dict["benchmark"]:
        # Set the dictionary
        results = {
            "execution_time": None,
            "unit": "seconds",
            "mock_path": arg_dict["mock_path"],
        }

        t1_start = process_time()  # Start timing

        # Measure the execution of process_images
        result_message = asyncio.run(process_images())

        t2_stop = process_time()  # Stop timing
        results["execution_time"] = t2_stop - t1_start
        if result_message == "Successful":
            results["result"] = result_message
        else:
            results["error"] = result_message

        # Convert results to JSON and print
        logger.setLevel(logging.DEBUG)
        logger.info("Benchmark".center(30, "*"))
        logger.info(json.dumps(results, indent=4))
    else:
        asyncio.run(process_images())
