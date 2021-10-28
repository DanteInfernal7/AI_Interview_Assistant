import speech_recognition as sr
def speechToText(audioFile):
    r = sr.Recognizer()
    with sr.AudioFile('Recording.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            return text
        except:
            print('Couldn\'t process request')