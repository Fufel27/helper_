import re, math, string, requests
from collections import Counter

TEXT = requests.get('http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml').text

def tokens(text):
    return re.findall(r'[а-я]+', text.lower())

words = tokens(TEXT)
counts =Counter(words)

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def splits(word):
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]
def known(words):
    return {w for w in words if w in counts}
def edits0(word):
    return {word}
def edits1(word):
    pairs = splits(word)
    deletes = [a+b[1:] for (a, b) in pairs if b]
    transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]
    replaces = [a + c + b[1:] for (a, b) in pairs for c in alphabet if b]
    inserts = [a + c + b for (a, b) in pairs for c in alphabet]
    return set(deletes + transposes + replaces + inserts)
def edits2(word):
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}
def correct(word):
    candidates = (known(edits0(word)) or known(edits1(word)) or known(edits2(word)) or [word])
    return max(candidates, key=counts.get)

