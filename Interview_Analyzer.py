from AudioVideoSplitter import splitAudio
from Speech_Parser import speechAnalyzer
from Emotion_Recognition import emotionRecog
name = 'name'
videoFile = 'video file location'
splitAudio(name, videoFile)
speechWordCorrections = speechAnalyzer('\\audio\\'+name+'.wav')
emotionRecog(name, videoFile)