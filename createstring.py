"""
You can use this script to create a input string like THE2
After running the script, simply enter the coordinates in
clockwise order one by one
for example:

24, -12, 10, -16, 14, -14, 24, -10 (write one then press enter)

this will return you the string

[(24,-12), (10,-16), (14,-14), (24,-10)]
"""


def areaformatter():
    vexs = []
    for i in range(8):
        vexs.append(input())

    string = f"[({vexs[0]},{vexs[1]}), ({vexs[2]},{vexs[3]}), ({vexs[4]},{vexs[5]}), ({vexs[6]},{vexs[7]})]"
    print(string)
    return string

areaformatter()