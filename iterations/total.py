# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
sum = 0
while True :
    x = input("Enter a number : ")
    if x=="done" :
        break
    try :
        num = int(x)
    except : 
        print("Invalid Number")
        continue

    count = count + 1
    sum = num + sum
print(f'count : {count}, sum : {sum}, average : {sum/count}')
# count = count +1
# # sum = x + sum
# print(f'count : {count}, sum : {sum}, average : {sum/count}')