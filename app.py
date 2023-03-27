import api_functions as af
import log_functions as lf

logger = lf.log_init(__name__)


def main() -> None:
    agadmator_videos = af.extract_info("UCL5YbN5WLFD8dLIegT5QAbA")
    print(agadmator_videos.head())


if __name__ == "__main__":
    main()
