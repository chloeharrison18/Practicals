unique_words = {"a": 0, "collection": 0, "fun": 0, "is": 0, "it": 0, "nice": 0, "of": 0, "thing": 0, "this": 0, "words": 0}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1
words = list(unique_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {} {}".format(word, max_length, unique_words[word]))
