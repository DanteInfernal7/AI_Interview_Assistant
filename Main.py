from AudioVideoSplitter import splitAudio
from Speech_Parser import speechAnalyzer
from Emotion_Recognition import emotionRecog
from Resume_Parser import resumeAnalyzer
name = 'name'
audioFile = 'audio file location'
videoFile = 'video file location'
resumeFile = 'resume location'
splitAudio(name, audioFile)
speechWordCorrections = speechAnalyzer('\\audio\\'+name+'.wav')
emotionRecog(name, videoFile)
resumeWordCorrections, correctedResume = resumeAnalyzer(resumeFile)




