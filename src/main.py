# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
from KFSlog import KFSlog
import logging
import os


@KFSlog.timeit
def main(DEBUG: bool) -> None:
    DEST_PATH: str="./m3u/"                 # playlist file destination folder
    LIBRARY_PATH: str="C:\\Users\\Felix\\Dropbox\\Music\\Library\\"
    MUSIC_FILE_EXT=(".m4a", ".mp3", ".wav") # music file extensions, recognise these files as music
    playlist_content: str                   # playlist current
    playlist_names: list
    
    logging.info(f"Loading direct child directory names excluding \"{DEST_PATH}\" and \"./log/\"...")
    playlist_names=[entry
                    for entry in os.listdir(".")
                    if os.path.isdir(entry)==True and entry!="m3u" and entry!="log"]    # get all playlist folders, exclude destination folder if exists already, exclude Log folder
    logging.info(f"\rLoaded direct child directory names excluding \"{DEST_PATH}\" and \"./log/\".")
    logging.debug(playlist_names)
    logging.debug(f"Creating destination directory \"{DEST_PATH}\"...")
    os.makedirs(f"{DEST_PATH}", exist_ok=True)                                              # create destination folder
    logging.debug(f"\rCreated destination directory \"{DEST_PATH}\".")
    
    logging.info("Creating playlist files...")
    for playlist_name in playlist_names:                                # every playlist folder
        logging.info(f"Loading music files from \"{playlist_name}/\"...")
        playlist_content="\n".join([os.path.join(LIBRARY_PATH, song)    # get every song in playlist folder, must be file and have music file extension, collapse list to string
                                    for song in os.listdir(f"./{playlist_name}")
                                    if os.path.isfile(song)==True and os.path.splitext(song)[1] in MUSIC_FILE_EXT])
        logging.info(f"Loaded music files from \"{playlist_name}/\".")
        logging.debug(playlist_content)
        
        logging.info(f"Saving playlist \"{DEST_PATH}{playlist_name}.m3u\"...")
        with open(f"{DEST_PATH}{playlist_name}.m3u", "wt", encoding="utf-8") as playlist_file:  # save playlist
            playlist_file.write(playlist_content)
        logging.info(f"\rSaved playlist \"{DEST_PATH}{playlist_name}.m3u\".")
    logging.info("Created playlist files.")
    
    return