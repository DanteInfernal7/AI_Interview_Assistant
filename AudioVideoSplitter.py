import moviepy.editor

video = moviepy.editor.VideoFileClip(r"C:\Users\hwala\Downloads\Rohan.mp4")

audio = video.audio

audio.write_audiofile('rohan.wav')