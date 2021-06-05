# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fName = input("Enter your file name: ")
doc = open(fName)

dic = {}

for line in doc:
    words = line.split()
    if len(words)<2 or words[0]!="From":
        continue
    else:
        dic[words[1]] = dic.get(words[1],0) + 1
print(dic)