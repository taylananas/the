cases = open("cases.txt")
answers = open("answers.txt")
temp = cases.read().splitlines()
temp2 = answers.read().splitlines()
wrongs = []

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
    yourinputvariable = inputxt

    area = "Your answer"
    #print(area) do not do this
    return area


def grading():
    total = len(temp)
    grade = 0
    for i in range(total):
        if testing(temp[i]) == temp2[i]:
            grade +=1
        else:
            wrongs.append(i+1)
    
    print(f"{grade}/{total}")
    print(f"Wrong questions are: {wrongs}")

grading()

