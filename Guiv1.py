#!/usr/bin/python3
#Joshua Pierce, Michael Abdo, Arnav Nagpal

#padding for the text boxes need to be spaced (complete)
#debuging tool to tell user that there is an error with entry, what it is, how to fix it.(ie they put in letters, or same block twice)
#link widgets to variables


from tkinter import *
from tkinter import ttk
import re

blocks = ["Block 1", "Block 2", "Block 3", "Block 4", "Block 5", "Block 6"]

Spinboxes = []
textEntries = []
finalCol = []

initialConfig = []
#reset grid and values function
def resetGrid():
    print('reset')
    for x in Spinboxes:
        x.delete(0,"end")
        x.insert(0,0)
        print(x)
    textEntries.clear()

#run arm(send values to text file for asp)
def runArm():
    
    print('run arm')
    for x in Spinboxes:
        temp = x.get()
        print(temp)
    sortFunc()
    textEntries.clear()

#function to sort the input into locations the asp program can use
def sortFunc():
    for x in reversed(Spinboxes):
        Spinboxes
        initialConfig.append(x.get())

    tempArray = []
    visited = [1, 1, 1, 1]
    i = 0

    for x in reversed(Spinboxes):
        temp = int(x.get())
        temp = temp - 1
        #print("Temp = ")
        #print(temp)

        tempArray.append(visited[temp])
        visited[temp] = visited[temp] + 1;
        #print("TempArray2 = ")
        #for i in tempArray:
            #print(i)
    
    #tempArray holds vertical position
    print("vertical position")
    for i in tempArray:
        print(i)
        
    # is the horizontal position
    print("horizontal position = ")
    for x in reversed(Spinboxes):
        temp = int(x.get())
        print(temp)

    #for y in tempArry (Y Axis)
    #for x in revered(Spinboxes) - (Xaxis)

    #sends the following to print and a text file for reading by asp, i for block, r for y(reversed)
    i = 1
    r = 5
    strTotal = ""
    for x in Spinboxes:
        strLine = "initCellHasBlock("+ str(tempArray[r]) +","+ x.get() + ","+ str(i) + ")."
        strTotal = strTotal + strLine + "\n"
        print(strLine)
        i = i + 1
        r = r - 1
    for x in (finalCol):
        temp = int(x.get())
        print(temp)
        strTotal = strTotal + "goalPlatform(" + str(temp) + ")." + "\n" 

    #the file handling, open to startingPosition.txt with write priveliges, write strTotal, close for asp use
    file = open("startingPosition.txt", "w")
    file.write(strTotal)
    file.close()
    import os
    file = open("initial_config.txt", "w")
    file.write("")
    file.close()
    os.system("clingo startingPosition.txt blocks_ASP_prog.lp >> initial_config.txt")
    os.system("rosrun pub publisher")
    
class alphaFrame:

    def __init__(self, Root):
        #sets size of window on open
        Root.geometry('1300x500')

        #Frame is set to use Pack method, to fill space across with a border
        self.topFrame = ttk.Frame(Root)
        self.topFrame.pack(fill = BOTH)
        self.topFrame.config(relief = SOLID)


        y = 0
        #Text input to take the input from user, each column relates to a physical column for the arm

        for z in range(1):
            label = ttk.Label(self.topFrame, text = "Platforms")
            label.grid(row = 2, column = 0, columnspan = 1)

            for x in range(6):
                #x = Text(self.topFrame, width = 10, height = 1)
                #x.grid(row = z+1, column = y, columnspan = 1, padx = 10, pady = 10)
                w = Spinbox(self.topFrame, from_= 0, to = 4, state = 'readonly')
                if x < 3:
                    w.grid(row = z+2, column = x+1, columnspan = 1, padx = 10, pady = 10)
                else:
                    w.grid(row = z+4, column = y+1, columnspan = 1, padx = 10, pady = 10)
                    y = y + 1
                Spinboxes.append(w)
            y = 0
        y = 0
        z = 0
        #loop to place all the labels for the columns above the input
        for x in blocks:
            label = ttk.Label(self.topFrame, text = x)
            if y < 3:
                label.grid(row = 1, column = y+1, columnspan = 1)
            #elif y == 3:
                #label.grid(row = 3, column = y+1-y, columnspan = 1)
            else:
                label.grid(row = 3, column = z+1, columnspan = 1)
                z = z + 1
            y = y + 1
            
        label2 = ttk.Label(self.topFrame, text = "Final Column")
        label2.grid(row = 6, column = 0, columnspan = 1)
        
        finalColumn = Spinbox(self.topFrame, from_= 0, to = 4)
        finalColumn.grid(row = 6, column = 1, columnspan = 1)
        
        finalCol.append(finalColumn)
        
        #Padding prevents frame from collapsing around button, err known on mac
        self.topFrame.config(padding = (30,50))

        #Frame defined as buffer for future dev, for visuals or other features (err messages), ignore or delete

        #self.middleFrame = ttk.Frame(Root)
        #self.middleFrame.pack(fill = BOTH)
        #self.middleFrame.config(relief = SOLID)


        #

        #Frame is directly under topframe by order of pack methods called
        self.botomFrame = ttk.Frame(Root)
        self.botomFrame.pack(fill = BOTH)
        self.botomFrame.config(relief = SOLID)

        #future reset and run buttons
        reset = ttk.Button(self.botomFrame, text = 'reset', command = resetGrid)
        reset.grid(row = 0, column = 0, columnspan = 1)

        run = ttk.Button(self.botomFrame, text = 'run', command = runArm)
        run.grid(row = 0, column = 2, columnspan = 1)
        self.botomFrame.config(padding = (30,50))

        

def main():
    root = Tk()
    app = alphaFrame(root)
    root.title("PhantomX GUI")


    root.mainloop()

if __name__ == "__main__": main()
