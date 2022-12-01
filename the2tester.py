import sys, subprocess, os, threading, time
cases = open("cases.txt")
answers = open("answers.txt")
temp = cases.read().splitlines()
temp2 = [*map(float, answers.read().splitlines())]
cases.close()
answers.close()
wrongs = []
diffs = []

#this questions should contain simple and some extreme cases but do not worry 'i hope', all are calculated by my brain (also my code too)so the answers should be right
#if you think there are some problems with the cases-answers or just want to ask something, just mail me at 'taylan.sahin@metu.edu.tr' 
#i hope you all (including me ofc) get 100 from the 'the'

#      We will not going to include the area of little triangle!
"""
HOW TO USE:
Copy your the2.py into the same folder
"""

def testing(inputxt, testedvalues):
    if os.path.isfile("the2.py"):
        area = subprocess.run(f"{sys.executable} the2.py", shell=1 ,input=inputxt, encoding="ascii", stdout=subprocess.PIPE).stdout
    else:
        raise FileNotFoundError("Please put the2.py into the same folder.")
    testedvalues.append(float(area)) #the2.py should return 2 UNROUNDED decimals as the pdf says


def grading(): #a simple check for cases and answers, nothing fancy here
    total = len(temp)
    grade = 0
    testedvalues = []
    for i in range(total):
        thread = threading.Thread(target=testing, args=[temp[i], testedvalues]) # Subprocess already spawns new processes, so multithreading is enough
        thread.start()
    while len(testedvalues) < total:
        time.sleep(0.01)
    for i in range(total):
        if abs(testedvalues[i] - temp2[i]) < 0.01:
            grade +=1
        else:
            diff = float(testedvalues[i]) - float(temp2[i])
            diff = "%.2f"%diff
            diffs.append(diff)
            wrongs.append(i+1)         

    print(f"{grade}/{total}")
    print(f"Wrong questions are: {wrongs}")
    print(f"Diffs from the answers in the same order: {diffs}")

grading() #runs the grading function which runs the testing function which returns a value that the grading function checks 'w'