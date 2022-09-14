import os


# Define path
path = "files"
# stopwords = open("stop_words.txt","r")
# stop_words = stopwords.read()
# print(stop_words)
# colors = ["red", "green", "blue", "purple"]

for filename in os.listdir(path):
   with open(os.path.join(path, filename), 'r') as f: 
    f.seek(0)
    # content = f.read()
    # print(content)
    # line = 1
    # for word in f:
    #     if word == '\n':
    #         line += 1
    # print("Number of lines in file is: ", line)
    array = []
    array.append(f.read())
    print(array)
    # punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    # for ele in content:
    #     if ele in punc:
    #         content = content.replace(ele, " ")
    # # to maintain uniformity
    # content=content.lower()		
    # # print(content)	
    # for word in array:
    #     print(word)

        





