from pydub import AudioSegment
sound = AudioSegment.from_mp3(".mp3")
sound.export(".wav", format="wav")