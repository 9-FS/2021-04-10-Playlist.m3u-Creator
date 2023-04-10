#Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import KFS.log
import logging
import os


@KFS.log.timeit
def main() -> None:
    DEST_PATH: str="./m3u/"                 #playlist file destination folder
    LIBRARY_PATH: str=""
    MUSIC_FILE_EXT=(".m4a", ".mp3", ".wav") #music file extensions, recognise these files as music
    playlist_content: str                   #playlist current
    playlist_names: list
    
    logging.info(f"Loading direct child directory names excluding \"{DEST_PATH}\" and \"./Log/\"...")
    playlist_names=[folder.name
                      for folder in os.scandir(".")
                      if folder.is_dir()==True and folder.name!="m3u" and folder.name!="Log"]   #get all playlist folders, exclude destination folder if exists already, exclude Log folder
    logging.info(f"\rLoaded direct child directory names excluding \"{DEST_PATH}\" and \"./Log/\".")
    logging.debug(playlist_names)
    logging.debug(f"Creating destination directory \"{DEST_PATH}\"...")
    os.makedirs(f"{DEST_PATH}", exist_ok=True)                                                  #create destination folder
    logging.debug(f"\rCreated destination directory \"{DEST_PATH}\".")
    
    logging.info("Creating playlist files...")
    for playlist_name in playlist_names:                                        #every playlist folder
        logging.info(f"Loading music files from \"{playlist_name}/\"...")
        playlist_content="\n".join([f"{os.path.join(LIBRARY_PATH, song.name)}"  #get every song in playlist folder, must be file and have music file extension, collapse list to string
                                    for song in os.scandir(f"./{playlist_name}")
                                    if song.is_file()==True and os.path.splitext(song.name)[1] in MUSIC_FILE_EXT])
        logging.info(f"Loaded music files from \"{playlist_name}/\".")
        logging.debug(playlist_content)
        
        logging.info(f"Saving playlist \"{DEST_PATH}{playlist_name}.m3u\"...")
        with open(f"{DEST_PATH}{playlist_name}.m3u", "wt", encoding="utf-8") as playlist_file:  #save playlist
            playlist_file.write(playlist_content)
        logging.info(f"\rSaved playlist \"{DEST_PATH}{playlist_name}.m3u\".")
    logging.info("Created playlist files.")
    
    return