# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
import json
from KFSconfig import KFSconfig
from KFSlog import KFSlog
import logging
import os


@KFSlog.timeit
def main(DEBUG: bool) -> None:
    playlist_content: str                           # playlist current
    playlist_names: list                            # playlist names
    settings: dict[str, str]                        # settings
    SETTINGS_DEFAULT: str=json.dumps({              # settings default
        "dest_path": "./m3u/",                      # playlist file destination folder
        "exclude_paths": ["./config/", "./log/"],   # don't create playlist files from these paths
        "library_path": "",                         # library path absolute to prepend to every song name in playlist file
        "music_file_ext": [".m4a", ".mp3", ".wav"], # music file extensions, recognise these files as music
    }, indent=4)


    try:
        settings=json.loads(KFSconfig.load_config("./config/settings.json",  SETTINGS_DEFAULT)) # load settings
    except FileNotFoundError:
        return
    
    
    logging.info(f"Loading direct child directory names excluding \"{settings['dest_path']}\" and \"{settings['exclude_paths']}\"...")
    playlist_names=[entry                                   # get all playlist directory names, exclude destination directory and excluded directories
                    for entry in os.listdir(".")
                    if     os.path.isdir(entry)==True
                       and entry!=settings["dest_path"].lstrip(".").strip("/")
                       and entry not in [exclude_path.lstrip(".").strip("/") for exclude_path in settings["exclude_paths"]]]
    logging.info(f"\rLoaded direct child directory names excluding \"{settings['dest_path']}\" and \"{settings['exclude_paths']}\".")
    logging.debug(playlist_names)
    logging.debug(f"Creating destination directory \"{settings['dest_path']}\"...")
    os.makedirs(f"{settings['dest_path']}", exist_ok=True)  # create destination folder
    logging.debug(f"\rCreated destination directory \"{settings['dest_path']}\".")
    
    logging.info("Creating playlist files...")          
    for playlist_name in playlist_names:                                            # every playlist folder
        logging.info(f"Loading music files from \"{playlist_name}/\"...")
        playlist_content="\n".join([os.path.join(settings["library_path"], song)    # get every song in playlist folder, must be file and have music file extension, collapse list to string
                                    for song in os.listdir(f"./{playlist_name}/")
                                    if os.path.isfile(f"./{playlist_name}/{song}")==True and os.path.splitext(song)[1] in settings["music_file_ext"]])
        logging.info(f"Loaded music files from \"{playlist_name}/\".")
        logging.debug(playlist_content)
        
        logging.info(f"Saving playlist \"{settings['dest_path']}{playlist_name}.m3u\"...")
        with open(f"{settings['dest_path']}{playlist_name}.m3u", "wt", encoding="utf-8") as playlist_file:  # save playlist
            playlist_file.write(playlist_content)
        logging.info(f"\rSaved playlist \"{settings['dest_path']}{playlist_name}.m3u\".")
    logging.info("Created playlist files.")
    
    return