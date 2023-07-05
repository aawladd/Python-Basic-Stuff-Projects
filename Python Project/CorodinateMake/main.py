import os

# filename = input("Enter the filename: ")
infile = open("Points.txt", "r")
lines = infile.readlines()

outfile = open("OutputPoints.txt", "w")

for i in lines:
    xcod = ""
    ycod = ""

    det = 0
    for j in i:
        if j == ",":
            det = 1
            continue
        if j == "\\":
            det = 2
            break

        if det == 0:
            xcod = xcod + j
        elif det == 1:
            ycod = ycod + j
        else:
            break

    outfile.write(f"{{x: {xcod} , y: {ycod[0:-1]} }},")
    outfile.write("\n")
