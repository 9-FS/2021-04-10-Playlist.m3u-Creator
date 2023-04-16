---
Topic: "Playlist.m3u Creator"
Author: "구FS"
---
<link href="./src/KFS/md_style.css" rel="stylesheet"></link>
<div id="global">

# <p style="text-align: center">`Playlist.m3u` Creator</p>
<br>
<br>

- [1. General](#1-general)

## 1. General

Creates `{playlist name}.m3u` playlist files based of the direct child directories. Playlist names are the child directory's names and content are the music files they contain. The results are saved in `./m3u`.  
By default files with the following file extension are recognised as music files:
- `.m4a`
- `.mp3`
- `.wav`

You may set `LIBRARY_PATH` if you you want any path prefixes in the playlist file.

</div>