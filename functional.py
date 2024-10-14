from functools import reduce

sentences = [
    "Der Fuchs hat die Gans gestohlen",
    "Heute war nichts sinnvolles im Fernsehen zu sehen",
    "Ich bin müde nach der Mittagspause"
]

# Definiere die Mindestlänge
min_length = 4

# Sätze in Listen von Wörtern umwandeln
splitted = list(map(lambda sentence: sentence.split(), sentences))

# Filtern von Wörtern, die länger als min_length sind
filtered_words = list(map(lambda words: list(filter(lambda word: len(word) > min_length, words)), splitted))

# Anzahl der Wörter zählen, die das Kriterium erfüllen
word_counts = list(map(len, filtered_words))

# Die Gesamtanzahl der Wörter summieren
total_count = reduce(lambda x, y: x + y, word_counts)

# Ausgabe
print("Anzahl der Wörter, die länger als", min_length, "Zeichen sind:", total_count)
