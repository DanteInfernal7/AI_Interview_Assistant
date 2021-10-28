badWords = ["kinda", "hate", "perfectionist", "basically", "stuff", "dedicated", "motivated", "fired", "actually",
            "benefits", "nervous", "sorry", "money", "perks", "horrible", "terrible", "divorced", "pregnant", "sick",
            "vacation", "arse", "bloody", "bugger", "damn", "balls", "bitch", "bullshit", "dick", "fuck"]

def speechAnalyzer(userSpeech):
    word_set = set(badWords)
    phrase_set = set(userSpeech.lower().split())
    return word_set.intersection(phrase_set)