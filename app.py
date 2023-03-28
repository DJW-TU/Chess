import api_functions as af
import log_functions as lf
import os
import pandas as pd
import dotenv

logger = lf.log_init(__name__)
LOADED = os.getenv("LOADED") == "True"
DATA_PATH = os.getenv("DATA_PATH")
dotenv_file = dotenv.find_dotenv()


def main() -> None:
    if not LOADED:
        logger.info("Data has not been loaded yet")
        agadmator_videos = af.extract_info("UCL5YbN5WLFD8dLIegT5QAbA")
        agadmator_videos.to_csv(DATA_PATH + "/agadmator_videos.csv", sep="\t", index=False)
        os.environ["LOADED"] = "True"
        dotenv.set_key(dotenv_file, "LOADED", os.environ["Loaded"])
    else:
        logger.info("Data has been loaded already")
        agadmator_videos = pd.read_csv(DATA_PATH + "/agadmator_videos.csv")

    print(agadmator_videos.head())


if __name__ == "__main__":
    main()
