import os
# Define path
path = "files"

for filename in os.listdir(path):
   with open(os.path.join(path, filename), 'r') as f: 
    content = (f.read())
    print(content)
