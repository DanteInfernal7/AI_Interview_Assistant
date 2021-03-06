from AudioVideoSplitter import splitAudio
from Speech_Parser import speechAnalyzer
from Emotion_Recognition import emotionRecog
from Resume_Parser import resumeAnalyzer
name = 'name'
videoFile = 'video file location'
resumeFile = 'resume location'
splitAudio(name, videoFile)
speechWordCorrections = speechAnalyzer('\\audio\\'+name+'.wav')
emotionRecog(name, videoFile)
resumeWordCorrections, correctedResume = resumeAnalyzer(resumeFile)
