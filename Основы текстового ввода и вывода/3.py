# BEGIN
from collections import Counter


def count_words(filepath):
    data = open(filepath).read()
    punctuation = [',', '.', '?', '!', ':']
    words = []
    for word in data.split():
        word = word.lower()
        for p in punctuation:
            if word.endswith(p):
                word = word[:-1]
        words.append(word)
    return Counter(words)
# END
