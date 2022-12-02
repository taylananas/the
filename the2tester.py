from asyncio import threads
import sys, subprocess, os, threading, time
cases = open("cases.txt")
answers = open("answers.txt")
temp = cases.read().splitlines()
temp2 = [*map(float, answers.read().splitlines())]
cases.close()
answers.close()
wrongs = []

#this questions should contain simple and some extreme cases but do not worry 'i hope', all are calculated by my brain (also my code too)so the answers should be right
#if you think there are some problems with the cases-answers or just want to ask something, just mail me at 'taylan.sahin@metu.edu.tr' 

"""
HOW TO USE:
Copy your the2.py into the same folder
"""

def testing(inputxt, testedvalues, i):
    if os.path.isfile("the2.py"):
        area = subprocess.run(f'"{sys.executable}" the2.py', shell=1, input=inputxt, encoding="ascii", stdout=subprocess.PIPE).stdout
    else:
        raise FileNotFoundError("Please put the2.py into the same folder.")
    testedvalues[i] = float(area)

def grading(): #a simple check for cases and answers, nothing fancy here, maybe something thanks to @Lojcs
    total = len(temp)
    grade = 0
    testedvalues = [*range(total)]
    threads = []
    for i in range(total):
        thread = threading.Thread(target=testing, args=[temp[i], testedvalues, i]) # Subprocess already spawns new processes, so multithreading is enough
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    for i in range(total):
        if abs(testedvalues[i] - temp2[i]) < 0.01:
            grade +=1
        else:
            diff = float(testedvalues[i]) - float(temp2[i])
            diff = "%.2f"%diff
            wrongs.append([i+1,diff])         

    print(f"{grade}/{total}")
    if wrongs:
        print(f"Wrong questions, diffs are: {wrongs}")

grading() #runs the grading function which runs the testing function which returns a value that the grading function checks 'w'