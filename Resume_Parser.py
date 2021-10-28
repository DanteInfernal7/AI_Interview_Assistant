import docx2txt as dct
badWords = ["getter", "synergy", "hard-worker", "hard-working", "thinker", "negotiable", "detail-oriented", "hardworker", "hardworking", "proactive", "thinker", "objective"]

def resumeAnalyzer(resumeFile):
    resume = dct.process(resumeFile)
    word_set = set(badWords)
    phrase_set = set(resume.lower().split())
    resumeWordCorrections = word_set.intersection(phrase_set)
    return resumeWordCorrections