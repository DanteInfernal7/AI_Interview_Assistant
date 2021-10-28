import moviepy.editor
def splitAudio(name, file):
    video = moviepy.editor.VideoFileClip(file)
    audio = video.audio
    audio.write_audiofile('\\audio\\'+name+'.wav')
