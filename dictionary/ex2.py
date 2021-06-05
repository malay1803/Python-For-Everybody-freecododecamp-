# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

fName = input("Enter your file name: ")

try:
    doc = open(fName)
except:
    print("Invalid File Name")
    quit()

dic = {}
l = []
for line in doc: 
    if line.startswith("From"):
        words = line.split(" ")
        try:
            l.append(words[2])
        except:
            continue

for day in l:
    dic[day] = dic.get(day,0) + 1
print(dic)
