import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('siddhi.wav') as source:
    audio_text = r.listen(source)

    try:

        text = r.recognize_google(audio_text)
        print(text)

    except:
        print('Couldn\' process request')