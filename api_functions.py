# importing libraries
import os
import pandas as pd
from googleapiclient.discovery import build
import log_functions as lf

# API Key generated from the Youtube API console
api_key = os.getenv("API_K")  # (https://developers.google.com/youtube/v3/getting-started)
# Establishing connection with the YouTube API key
youtube = build("youtube", "v3", developerKey=api_key)

logger = lf.log_init(__name__)


@lf.timeit
def youtube_playlist_data(id: str):
    logger.info("-- Start Download --")
    token = None
    # Using the API's list function to retrive the channel data
    y_data = youtube.channels().list(id=id, part="contentDetails").execute()
    # Retrieving the "uploads" playlist Id from the channel
    youtube_playlist_id = y_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    video_data = []
    # The while loop which continues until the items are present in the playlist
    while 1:
        y_playlist_data = (
            youtube.playlistItems()
            .list(
                playlistId=youtube_playlist_id,
                part="snippet",
                maxResults=50,
                pageToken=token,
            )
            .execute()
        )  # Retrieving the playlist items snippet with a max result of 50 in each iteration
        video_data = video_data + y_playlist_data["items"]
        # Update the token so as to get the next data
        token = y_playlist_data.get("nextPageToken")
        # If there is no token break the loop
        if token is None:
            break
    # Return the final collected data
    logger.info("-- End Download --")
    return video_data


@lf.timeit
def extract_info(playlist_id: str) -> dict:
    logger.info("-- Start Data Extraction --")
    # Here we pass the channel id of which the data needs to be retrieved
    y_video_data = youtube_playlist_data(playlist_id)
    # Initializing the title variable
    title = []
    # Initializing the description variable
    description = []
    # Initializing the video_id
    video_id = []
    # Initializing the thumbnail_default variable
    thumbnail_default = []
    # Initializing the thumbnail_standard variable
    thumbnail_standard = []
    # iterating through videos data one by one
    for data in y_video_data:
        # Retrieving and appending the video title
        title.append(data["snippet"]["title"])
        # Retrieving and appending the description
        description.append(data["snippet"]["description"])
        # Retrieving and appending the video_id
        video_id.append("https://www.youtube.com/watch?v=" + data["snippet"]["resourceId"]["videoId"])
        # Check whether the thumbnail attribute is present
        if "thumbnails" in data["snippet"].keys():
            if "default" in data["snippet"]["thumbnails"].keys():
                # If thumbnail default present append the data
                thumbnail_default.append(data["snippet"]["thumbnails"]["default"]["url"])
            else:
                # If thumbnail default not present append 'Null'
                thumbnail_default.append("Null")
            if "standard" in data["snippet"]["thumbnails"].keys():
                # If thumbnail standard present append the data
                thumbnail_standard.append(data["snippet"]["thumbnails"]["standard"]["url"])
            else:
                # If thumbnail standard not present append 'Null'
                thumbnail_standard.append("Null")
        else:
            thumbnail_default.append("Null")
            thumbnail_standard.append("Null")
    final_data = {
        "video_title": title,
        "video_id": video_id,
        "Description": description,
        "thumbnail_default": thumbnail_default,
        "thumbnail_standard": thumbnail_standard,
    }  # Merge the data to form the final dataset
    logger.info("-- End Data Extraction --")
    return pd.DataFrame(final_data)
