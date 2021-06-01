# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F

def computegrade(score):
    if score>0.9 :
        print("A")
    elif score<0.9 and score>0.8 :
        print("B")
    elif score<0.8 and score>0.7 :
        print("C")
    elif score<0.7 and score>0.6 :
        print("D")
    else :
        print("F")
x = float(input("Enter score : "))
computegrade(x)