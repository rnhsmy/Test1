# Converts video file's into an audio file

import moviepy.editor as mp
video = mp.VideoFileClip("#")
video.audio.write_audiofile("#")
