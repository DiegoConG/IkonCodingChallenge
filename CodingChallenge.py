import os
import ast 

def calculateOptimal():

    with open(os.getcwd()+'//challenge.in') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines] 

    for i in range(0,len(lines),3):

        capacity = int(lines[0+i])
        backgroundTasks = ast.literal_eval(lines[1+i])
        foregroundTasks = ast.literal_eval(lines[2+i])

        optimal = 0
        optimalProcesses = []

        for x in range(len(backgroundTasks)):
            temp = []
            for y in range(len(foregroundTasks)):

                consuption = backgroundTasks[x][1] + foregroundTasks[y][1] 

                if consuption <= capacity  and consuption >= optimal :
                    optimal = consuption

                    temp = backgroundTasks[x][0],foregroundTasks[y][0]
                    optimalProcesses.append(temp)

        print(optimalProcesses)
        writeOptimal(optimalProcesses)

def writeOptimal(procs):
    print("Procs: ")
    print(procs)
    with open(os.getcwd()+'//challenge.out', 'a') as out:
        out.write(str(procs).strip("[]") + '\n')


calculateOptimal()