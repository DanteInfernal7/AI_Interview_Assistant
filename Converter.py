from pydub import AudioSegment
sound = AudioSegment.from_mp3("Recording.mp3")
sound.export("Recording.wav", format="wav")