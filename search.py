import os


# Define path
path = "files"
stopwords = open("stop_words.txt","r")
stop_words = stopwords.read()


for filename in os.listdir(path):
   with open(os.path.join(path, filename), 'r') as f: 
    content = f.read()
    # print(content)
    f.seek(0)
    array = []
    array.append(f.readline())
    # print(array)
    line = 1
    for word in f:
        if word == '\n':
            line += 1
    # print("Number of lines in file is: ", line)
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in content:
        if ele in punc:
            content = content.replace(ele, " ")
    content = content.lower()
    from nltk.tokenize import word_tokenize
    for i in range(1):
        # this will convert
        # the word into tokens
        text_tokens = word_tokenize(content)
        # print(text_tokens)
    
    tokens_without_sw = [
        word for word in text_tokens if not word in stop_words]
    
    # print(tokens_without_sw)
    dict = {}

    for i in range(line):
        check = array[i].lower()
        for item in tokens_without_sw:

            if item in check:
                if item not in dict:
                    dict[item] = []

                if item in dict:
                    dict[item].append(i+1)

    print(dict)



    	
    





