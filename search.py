import os
import re


# Define path
path = "files"
stopwords = open("stop_words.txt", "r")
stop_words = stopwords.read()

file = {}
for filename in os.listdir(path):
    # print(filename)
    pattern = re.compile('[\W_]+')
    # print(pattern)
    file[filename] = open(os.path.join(path, filename), 'r').read().lower()
    file[filename] = pattern.sub(' ', file[filename])
    from nltk.tokenize import word_tokenize
    from nltk.tokenize.treebank import TreebankWordDetokenizer as Detok
    detokenizer = Detok()
    for i in range(1):
        # this will convert the word into tokens
        text_tokens = word_tokenize(file[filename])
        # print(text_tokens)

    tokens_without_sw = [
        word for word in text_tokens if word not in stop_words]
    file[filename] = detokenizer.detokenize(tokens_without_sw)
    # print(file[filename])
    re.sub(r'[\W_]+', '', file[filename])
    file[filename] = file[filename].split()
    # print(file[filename])

    fileIndex = {}
    for index, word in enumerate(file[filename]):
        if word in fileIndex.keys():
            fileIndex[word].append(index)
        else:
            fileIndex[word] = [index]
    print(fileIndex)

    