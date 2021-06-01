# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

fName = input("Enter your file name : ")
fhand = open(fName)
count = 0
for line in fhand :
    print(line.upper())