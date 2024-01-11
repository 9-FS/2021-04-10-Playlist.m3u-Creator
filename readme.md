---
Topic: "Playlist.m3u Creator"
Author: "구FS"
---
<link href="./doc_templates/md_style.css" rel="stylesheet"></link>
<body>

# <p style="text-align: center">`Playlist.m3u` Creator</p>
<br>
<br>

- [1. General](#1-general)

## 1. General

Creates `{playlist name}.m3u` playlist files based on the working directory's children. Playlist names are the child directory's names and content are the music files they contain. The results are by default saved in `./m3u/`. This can be changed with the `dest_path` setting.

By default files with the following file extension are recognised as music files:
- `.m4a`
- `.mp3`
- `.wav`

This can be changed with the `music_file_ext` setting.

You may set `library path` if you you want any path prefix the music file entries. This may be useful if you want to use absolute paths in the playlist file.

You can exclude directories from being processed by adding them to the `exclude_paths` setting.

</body>