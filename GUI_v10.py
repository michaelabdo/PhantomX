

from tkinter import *
from tkinter import ttk
import re
root = Tk()
blocks = ["Block 1", "Block 2", "Block 3", "Block 4", "Block 5", "Block 6"]
labels = []
labelCol = []

Spinboxes = []
textEntries = []
finalCol = []
initialConfig = []

#to make the arm run code, make 1 when Canvas needs to run the solution
isRunArm = 0

#variables for canvas use
CanvasRect = []


#reset grid and values function
def resetGrid():
    for x in Spinboxes:
        x['state'] = 'normal'
        x.delete(0,"end")
        x.insert(0,0)
        x['state'] = 'readonly'
        x['fg'] = "black"

    for x in finalCol:
        x['state'] = 'normal'
        x.delete(0,"end")
        x.insert(0,0)
        x['state'] = 'readonly'
        x['fg'] = "black"

    err = labelCol[1]
    err['text'] = ''
    textEntries.clear()


def InitRunArm():

    runArm(0)

#run arm (send values to text file for asp), wont send if error,
#will change colour of text regarding error or no error
def runArm(isRunArm):
    
    errhandle = 0
    count = 0
    errString = "ERROR: Please change the following input(s) with values between 1 and 4: \n\n"
    for x in Spinboxes:
        temp = x.get()
        if int(temp) == 0:
            x['fg'] = "red"
            y = labels[count]
            errString = errString + "\t" + y['text'] + "\n"
            errhandle = -1
            
        else:
            x['fg'] = "black"
            y = labels[count]
        count = count + 1

    for x in finalCol:
        if int(x.get()) == 0:
            x['fg'] = "red"
            y = labelCol[0]
            errString = errString + "\t" + y['text'] + "\n"
            errhandle = -1
            
        else:
            x['fg'] = "black"
            y = labelCol[0]

    err = labelCol[1]
    if errhandle == 0:
        err['text'] = "Clingo: ASP program solving solution."
        if isRunArm == 0:
            err['text'] = err['text'] + "\nC++ program writing solution movments to arm..."
        else:
            err['text'] = err['text'] + "\nGUI program is generating visuals..."
        sortFunc(isRunArm)
    else:
        err['text'] = errString
    textEntries.clear()

#function to sort the input into locations the asp program can use
def sortFunc(isRunArm):
    
    
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
    outputmsg = labelCol[1]
    if isRunArm == 0:
        os.system("rosrun pub publisher")
        outputmsg['text'] = outputmsg['text'] + "\npublisher c++ code has finished"
    else:
        CanvasSolution()
        outputmsg['text'] =  outputmsg['text'] + "\nVisuals complete."


#run runArm() and sortfunc() from run arm without sending
def IsCanvSolPossible():
    runArm(1)
    

def CanvasSolution():
    
    
    window = Toplevel(root)
    window.title("Block Solution")
    window.geometry('600x600')
    
    scr = ttk.Scrollbar(window, orient=VERTICAL)
    MainCanvas = Canvas(window,scrollregion=(0, 0, 1000, 5000), yscrollcommand=scr.set)
    MainFrame = Frame(MainCanvas, background="lightgrey")
    scr['command'] = MainCanvas.yview
    
    MainCanvas.grid(column=0, row=0, sticky=(N,W,E,S))
    scr.grid(column=1, row=0, sticky=(N,S))
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    MainCanvas.create_window((0,0),window=MainFrame,anchor='nw')
    
    
    
    
    movesArr = []
    itemArr= []
    i = 6
    levOne = 0
    levTwo = 0
    levThree = 0
    levFour = 0

    #a loop to create a reference to where the blocks are currently positioned,
    #that reference will be updated for future positions
    for x in reversed(Spinboxes):
        CanvasRect.append(x.get())

        if int(x.get()) == 1:
            levOne = levOne + 1
            itemArr.append([i,int(x.get()), levOne])
            
        elif int(x.get()) == 2:
            levOne = levTwo + 1
            itemArr.append([i,int(x.get()), levTwo])
            
        elif int(x.get()) == 3:
            levThree = levThree + 1
            itemArr.append([i,int(x.get()), levThree])
            
        elif int(x.get()) == 4:
            levFour = levFour + 1
            itemArr.append([i,int(x.get()), levFour])
        i = i - 1
        

    #read from the generated solution, then split the solution into its steps, then sort the solution
    
    file = open("final_sol.txt", "r")
    movesArrRaw = file.read().split()
    file.close()
    i = 0
    
    
    for i in range(len(movesArrRaw)):
        
        if movesArrRaw[i].startswith("(", 12, 13):
            x = movesArrRaw[i].strip("moveCellCell() ").split(",")
            for j in range(len(x)):
                x[j] = int(x[j])
            movesArr.append( x )
            
   
    movesArr.sort()


    #make the inital canvas and use initial input 
    labelText = "Starting Position: "
    label = ttk.Label(MainFrame, text = labelText)
    label.grid(row = 0, column = 0, columnspan = 1)
    graphInt = Canvas(MainFrame, width=400, height=200)
    graphInt.grid(row = 0, column = 1, columnspan = 1, padx=(5,5), pady=(5,5))
    makeCanvasStart(graphInt)
    
    CanvasRect.clear()

    #through all the generated steps, all func to calc the new position,create a canvas,
    #call func to draw the position of blocks
    for i in range(len(movesArr)):
        
        newPosition(movesArr[i], itemArr)
        text = "Arm decision "
        labelText = text + str(i) + ":"
        label = ttk.Label(MainFrame, text = labelText)
        label.grid(row = i +1, column = 0, columnspan = 1)
        graphInt = Canvas(MainFrame, width=400, height=200)
        graphInt.grid(row = i + 1, column = 1, columnspan = 1, padx=(5,5), pady=(5,5))
        makeCanvasStart(graphInt)
        CanvasRect.clear()
        
    #this function keeps track of the positions of the blocks and then writes over a list
def newPosition(armMov, currentPosB):

    #armMov has 5 values, one is irrelivent as it refers to the arm position
    #two are block position before for height and column, and the other two
    #are the next placements of the blocks.
    #each block is from an array of where all the blocks are height and column,
    #it compares where each block should be and for the next movments original position
    #then it moves the blocks into the list CanvasRect in order to be drawn in the next canvas
    for block in currentPosB:
        if block[2] == armMov[1] and block[1] == armMov[2]:
            block[2] = armMov[3]
            block[1] = armMov[4]
            break
            
    for block in currentPosB:
        CanvasRect.append(block[1])
    

    #defines the visual for the inital set up of the arm
def CanvasSetup():
    window = Toplevel(root)
    window.title("Block Setup")

    for x in reversed(Spinboxes):
        CanvasRect.append(x.get())
    
    graphInt = Canvas(window, width=400, height=200)
    graphInt.grid(row = 0, column = 1, columnspan = 1)
    makeCanvasStart(graphInt)
    CanvasRect.clear()
    

#canvas use, will appear in seperate window
def makeCanvasStart(GraphInt):

    #four arrays for the four columns
    cOne, cTwo, cThree, cFour = ([] for i in range(4))
    
    #the block numbers and their associated colors
    numberAndColor = [(6, "red"), (5, "green"), (4, "red"), (3, "yellow"), (2, "green"), (1, "blue")]

    baseYAxis = 200
   
    
    #Moving that data into seperate arrays cOne,cTwo, cThree, cFour. using in range 6, we start at the beginning of the array
    #the order of that array is 6 through to 1, representing each block. list numberAndColor keeps track of each block order
    #each block has a column on the board, represented by
    #the array value, 1-4. if the array is 0 then the block wont be placed, and the program moves to the next block. This
    #happens by reducing count by one each time wheather or not a block is placed.

    for i in range(len(CanvasRect)):
    
        x = CanvasRect[i]
        y  = numberAndColor[i]
        
        if int(x) == 1:
            cOne.append(y)
        elif int(x) == 2:
            cTwo.append(y)
        elif int(x) == 3:
            cThree.append(y)
        elif int(x) == 4:
            cFour.append(y)
    

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
 

#defines the offsets in height when placing virtual blocks
def heightEquation(height, offset):
    blockOff = 30 * offset
    spaceOff = 4 * offset
    return height - blockOff - spaceOff - 30


#defines the view of the GUI, contains three frames, one
class alphaFrame:

    def __init__(self, Root):
        #sets size of window on open
        Root.geometry('750x600')

        #Frame is set to use Pack method, to fill space across with a border
        self.topFrame = ttk.Frame(Root)
        self.topFrame.pack(fill = BOTH)
        self.topFrame.config(relief = SOLID)



        #Text input to take the input from user, each column relates to a physical column for the arm
        y = 0
        for z in range(1):
            label = ttk.Label(self.topFrame, text = "Platforms")
            label.grid(row = 2, column = 0, columnspan = 1)

            for x in range(6):
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

            else:
                label.grid(row = 3, column = z+1, columnspan = 1)
                z = z + 1
            labels.append(label)
            y = y + 1

        #user selects the placement of the final column
        label2 = ttk.Label(self.topFrame, text = "Final Column")
        label2.grid(row = 6, column = 0, columnspan = 1)
        labelCol.append(label2)

        finalColumn = Spinbox(self.topFrame, from_= 0, to = 4, state = 'readonly')
        finalColumn.grid(row = 6, column = 1, columnspan = 1, pady=40)

        finalCol.append(finalColumn)

        #Padding prevents frame from collapsing around button
        self.topFrame.config(padding = (30,50))



        #Frame will show err messages
        self.middleFrame = ttk.Frame(Root)
        self.middleFrame.pack(fill = BOTH)
        self.middleFrame.config(relief = SOLID)
        label3 = ttk.Label(self.middleFrame, text = "")
        label3.grid(row = 0, column = 0, columnspan = 1)
        labelCol.append(label3)


        self.middleFrame.config(padding = (15,15))

        #Frame is directly under topframe by order of pack methods called
        self.botomFrame = ttk.Frame(Root)
        self.botomFrame.pack(fill = BOTH)
        self.botomFrame.config(relief = SOLID)

        #reset, run and display setup buttons
        reset = ttk.Button(self.botomFrame, text = 'reset', command = resetGrid)
        reset.grid(row = 0, column = 0, columnspan = 1, padx = 15)

        run = ttk.Button(self.botomFrame, text = 'run', command = InitRunArm)
        run.grid(row = 0, column = 2, columnspan = 1, padx = 15)



        showSetup = ttk.Button(self.botomFrame, text = 'view setup', command = CanvasSetup)
        showSetup.grid(row = 0, column = 4, columnspan = 1, padx = 15)

        visSol = ttk.Button(self.botomFrame, text = 'view generated solution', command = IsCanvSolPossible)
        visSol.grid(row = 0, column = 6, columnspan = 1, padx = 15)
        
        self.botomFrame.config(padding = (30,50))



def main():

    app = alphaFrame(root)
    root.title("PhantomX GUI")


    root.mainloop()

if __name__ == "__main__": main()
