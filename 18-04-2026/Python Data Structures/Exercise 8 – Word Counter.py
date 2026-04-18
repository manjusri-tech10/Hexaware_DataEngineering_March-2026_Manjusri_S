#1
sentence = "python is easy and python is powerful"
words = sentence.split()
word_count = {}

#2
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)