import os
from string import punctuation
from nltk.tokenize import word_tokenize


# Define path
file_path = "files"

#reading the files
for file in os.listdir(file_path):
       with open(os.path.join(file_path, file), 'r') as open_file: 
            content = open_file.read()
            open_file.seek(0)
            new_array = []
            new_array.append(open_file.readline())
            line = 1
            for new_line in open_file:
                if new_line == '\n':
                    line += 1
            punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
            for element in content:
                if element in punctuation:
                    content = content.replace(element, " ")
            content = content.lower()
            import nltk
            nltk.download('punkt')

            from nltk.tokenize import word_tokenize
            stopwords = open("stop_words.txt","r")
            stop_words = stopwords.read()
            for i in range(1):
                word_tokens = word_tokenize(content)

            tokens_without_stopwords = [
                word for word in word_tokens if not word in stop_words]
            # print(tokens_without_stopwords)

            word_dict = {}

            for i in range(line):
                check = new_array[i].lower()
                for item in tokens_without_stopwords:
                    if item in check:
                        if item not in word_dict:
                            word_dict[item] = []
                        elif item in word_dict:
                            word_dict[item].append(i+1)

            print(word_dict)





        