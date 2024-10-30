import asyncio
from pathlib import Path

import baile

# Extract jsons of mocks
dir_in = Path(__file__).resolve().parent / "mocks"
results_dir = Path(__file__).resolve().parent / "images"


# Loop to generate images of the jsons
async def process_images():
    try:
        # Process to generete images of the json
        await baile.to_image(
            path_figs=dir_in, path=str(results_dir), num_tabs=4, debug=True
        )
    except Exception as e:
        print("No to image".center(30,"%"))
        print(e)
        print("***")


# Run the loop
asyncio.run(process_images())
