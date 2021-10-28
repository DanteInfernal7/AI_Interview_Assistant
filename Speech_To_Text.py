import speech_recognition as sr
def speechToText(name):
    r = sr.Recognizer()
    with sr.AudioFile(name+'.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            return text
        except:
            print('Couldn\'t process request')