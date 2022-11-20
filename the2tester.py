cases = open("cases.txt")
answers = open("answers.txt")
temp = cases.read().splitlines()
temp2 = answers.read().splitlines()
wrongs = []

#there are 16 cases for now, its 4.30am and i want to commit suicide but i will add new ones later
#this cases should contain simple cases and some extreme cases but all are calculated by my brain (also my code too) so the answers should be right
#if you think there is some problems with the cases-answers just mail me taylan.sahin@metu.edu.tr

"""

HOW TO USE:
COPY YOUR CODE INTO THE def testing() area
erase any unnecessary print's like you are uploading it to odtuclass

WRITE "inputxt" in the input statement's right side
for example if your code is like:

inputvalues = input()

CHANGE THIS AS:
inputvalues = inputxt

and instead of printing the answer, return it

for example:

finalanswer = areaofthegreenzone
print(finalanswer)

INSTEAD OF PRINT, WRITE:
return finalanswer

"""
def testing(inputxt):
    yourinputvariable = inputxt #yourinputvariable = input() instead of input write inputxt

    area = "Your answer" #not have to be a string but must be a number with 2 UNROUNDED decimals as the pdf says
    #print(area) do not do this
    return area #do this instead


def grading(): #a simple check for cases and answers, nothing fancy here
    total = len(temp)
    grade = 0
    for i in range(total):
        if testing(temp[i]) == temp2[i]:
            grade +=1
        else:
            wrongs.append(i+1)
    
    print(f"{grade}/{total}")
    print(f"Wrong questions are: {wrongs}")

grading() #runs the grading function which runs the testing function which returns a value that the grading function checks 'w'

