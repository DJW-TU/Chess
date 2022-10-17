# Chess

This project presents a short script using a google API to match chess openings with videos from the youtube channel agadmator. This is then utizlized to create a google sheet file, where the videos can be searched by the opening. Agadmator is a popular chess youtuber who analyzes chess matches accross popular chess tournaments. He publishes roughly one video per day and his analyzes are sharp and fun to watch. Agadmator posts the move order of each match in the video description among other information of the match. The extraction happens in three steps. 

1. All descriptions from the videos from agadmator are loaded.
2. The move order description of each video is extracted and matched against the opening database.
3. The file is saved as a csv. 

The chess openings which were used were retraced from https://github.com/tomgp/chess-canvas/blob/master/pgn/chess_openings.csv.
After the extraction the created csv is uploaded into a google sheet and a short query is written in order to utilize the sheet as a search tool. The final search tool can be found here - use the search function in cells D4 & D5 to find a specific opening:

https://docs.google.com/spreadsheets/d/1P_0yk1MQiWjT4Qhp1MrkD_bYtRFPTGJrUsvtJXpTX-Q/edit?usp=sharing