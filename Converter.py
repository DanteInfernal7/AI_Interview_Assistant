from pydub import AudioSegment
sound = AudioSegment.from_mp3("siddhi.mp3")
sound.export("siddhi.wav", format="wav")