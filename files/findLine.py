# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

#X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

fName = input("Enter your file name : ")
try:
    fHand = open(fName)
except:
    print("Invalid file name")
    quit()
sum = 0
count=0
for line in fHand :
    if line.startswith("X-DSPAM-Confidence:") :
        rmNewLine = line.strip()                                #to remove /n from the end of each line
        pos = rmNewLine.find(":")                             #to find the position of : in a line
        num = float(rmNewLine[pos+1:])                  #to select convert the string into number
        sum = sum + num                                         #to find sum of the numbers
        count = count +1                                          #to count the number of lines
print(f'Average spam confidence: {sum/count}')   #to print the output