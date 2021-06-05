# Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5

# Enter a file name: mbox.txt
# zqian@umich.edu 195

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

# for maximum number of messages

bigCount = None
bigWord = None

for word, value in dic.items():
    if bigCount is None or bigCount<value:
        bigCount = value
        bigWord = word
print(f'Most occured word: {bigWord}, {bigCount}')
