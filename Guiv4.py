#!/usr/bin/python3
#Joshua Pierce, Michael Abdo, Arnav Nagpal

#padding for the text boxes need to be spaced (complete)
#debuging tool to tell user that there is an error with entry, what it is, how to fix it.(ie they put in letters, or same block twice)
#link widgets to variables


from tkinter import *
from tkinter import ttk
import re
root = Tk()
blocks = ["Block 1", "Block 2", "Block 3", "Block 4", "Block 5", "Block 6"]

Spinboxes = []
textEntries = []
finalCol = []
initialConfig = []

#variables for canvas use
CanvasRect = []

#reset grid and values function
def resetGrid():
    print('reset')
    for x in Spinboxes:
        x['state'] = 'normal'
        x.delete(0,"end")
        x.insert(0,0)
        x['state'] = 'readonly'
        print(x)
    textEntries.clear()

#run arm(send values to text file for asp)
def runArm():
    errhandle = 0
    
    for x in Spinboxes:
        temp = x.get()
        if int(temp) == 0:
            x['fg'] = "red"
            errhandle = -1
        else:
            x['fg'] = "black"
    for x in finalCol:
        if int(x.get()) == 0:
            x['fg'] = "red"
            errhandle = -1
        else:
            x['fg'] = "black"
            
    if errhandle == 0:
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
        
        tempArray.append(visited[temp])
        visited[temp] = visited[temp] + 1;
        
    
    #tempArray holds vertical position
    print("vertical position")
    for i in tempArray:
        print(i)
        
    # is the horizontal position
    print("horizontal position = ")
    for x in reversed(Spinboxes):
        temp = int(x.get())
        print(temp)

    

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
    file = open("final_sol.txt", "w")
    file.write("")
    file.close()
    print("blocks_ASP_prog.lp asp is beginning to find solution")
    os.system("clingo startingPosition.txt blocks_ASP_prog.lp >> final_sol.txt")
    os.system("rosrun pub publisher")

#canvas use, will appear in middle frame
def makeCanvasStart():

    #four arrays for the four columns
    cOne, cTwo, cThree, cFour = ([] for i in range(4))
    #the block numbers and their associated colors
    numberAndColor = [(6, "red"), (5, "green"), (4, "red"), (3, "yellow"), (2, "green"), (1, "blue")]

    baseYAxis = 200
    window = Toplevel(root)
    window.title("Block Setup")

    GraphInt = Canvas(window, width=600, height=200)
    GraphInt.grid(row = 0, column = 0, columnspan = 1)
    
    
    #Accessing the data from the input and place in CanvasRect arr
    for x in reversed(Spinboxes):
        CanvasRect.append(x.get())

    
    #Moving that data into seperate arrays cOne,cTwo, cThree, cFour. using in range 6, we start at the beginning of the array
    #the order of that array is 6 through to 1, representing each block. list numberAndColor keeps track of each block order
    #each block has a column on the board, represented by
    #the array value, 1-4. if the array is 0 then the block wont be placed, and the program moves to the next block. This
    #happens by reducing count by one each time wheather or not a block is placed.
    for i in range(6):
        x = CanvasRect.pop(0)
        y = numberAndColor.pop(0)
        if int(x) == 1:
            print(x)
            cOne.append(y)
        elif int(x) == 2:
            print(x)
            cTwo.append(y)
        elif int(x) == 3:
            print(x)
            cThree.append(y)
        elif int(x) == 4:
            print(x)
            cFour.append(y)
       
    
    print(cOne)
    print(cTwo)
    print(cThree)
    print(cFour)

    #from each of the array columns, write to canvas for block position, color and number
    
    if len(cOne) > 0:
        for i in range(len(cOne)):
            height = baseYAxis
            GraphInt.create_rectangle(30, heightEquation(baseYAxis, i), 60, heightEquation(baseYAxis, i) + 30, fill=cOne[i][1])
            GraphInt.create_text(40,heightEquation(baseYAxis, i) + 20,text=cOne[i][0])
    if len(cTwo) > 0:
        for i in range(len(cTwo)):
            GraphInt.create_rectangle(70, heightEquation(baseYAxis, i), 100, heightEquation(baseYAxis, i) + 30, fill=cTwo[i][1])
            GraphInt.create_text(80,heightEquation(baseYAxis, i) + 20,text=cTwo[i][0])
    if len(cThree) > 0:
        for i in range(len(cThree)):
            GraphInt.create_rectangle(110, heightEquation(baseYAxis, i), 140, heightEquation(baseYAxis, i) + 30, fill=cThree[i][1])
            GraphInt.create_text(120, heightEquation(baseYAxis, i) + 20,text=cThree[i][0])
    if len(cFour) > 0:
        for i in range(len(cFour)):
            GraphInt.create_rectangle(150, heightEquation(baseYAxis, i), 180, heightEquation(baseYAxis, i) + 30, fill=cFour[i][1])
            GraphInt.create_text(160,heightEquation(baseYAxis, i) + 20,text=cFour[i][0])
 
def heightEquation(height, offset):
    blockOff = 30 * offset
    spaceOff = 4 * offset
    return height - blockOff - spaceOff - 30
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

        self.middleFrame = ttk.Frame(Root)
        self.middleFrame.pack(fill = BOTH)
        self.middleFrame.config(relief = SOLID)

        
        #

        self.middleFrame.config(padding = (15,15))

        #Frame is directly under topframe by order of pack methods called
        self.botomFrame = ttk.Frame(Root)
        self.botomFrame.pack(fill = BOTH)
        self.botomFrame.config(relief = SOLID)

        #future reset and run buttons
        reset = ttk.Button(self.botomFrame, text = 'reset', command = resetGrid)
        reset.grid(row = 0, column = 0, columnspan = 1)

        run = ttk.Button(self.botomFrame, text = 'run', command = runArm)
        run.grid(row = 0, column = 2, columnspan = 1)
        

        #showSetup = ttk.Button(self.botomFrame, text = 'view setup', command = makeCanvasStart(Root))
        showSetup = ttk.Button(self.botomFrame, text = 'view setup', command = makeCanvasStart)
        showSetup.grid(row = 0, column = 4, columnspan = 1)
        self.botomFrame.config(padding = (30,50))

        

def main():
    
    app = alphaFrame(root)
    root.title("PhantomX GUI")


    root.mainloop()

if __name__ == "__main__": main()
