#!/usr/bin/python3
#Joshua Pierce

#padding for the text boxes need to be spaced (complete)
#debuging tool to tell user that there is an error with entry, what it is, how to fix it.(ie they put in letters, or same block twice)
#link widgets to variables


from tkinter import *
from tkinter import ttk
import re

columns = ["column 1", "column 2", "column 3", "column 4"]

#reset grid and values function
def resetGrid():
    print('reset')

#run arm(send values to text file for asp)
def runArm():
    print('run arm')
    
class alphaFrame:
    
        
    def __init__(self, Root):
        #sets size of window on open
        Root.geometry('500x500')
        
        #Frame is set to use Pack method, to fill space across with a border
        self.topFrame = ttk.Frame(Root)
        self.topFrame.pack(fill = BOTH)
        self.topFrame.config(relief = SOLID)


        y = 0
        #Text input to take the input from user, each column relates to a physical column for the arm

        for z in range(6):
            for x in range(4):
                x = Text(self.topFrame, width = 10, height = 1)
                x.grid(row = z+1, column = y, columnspan = 1, padx = 10, pady = 10)
                y = y + 1
            y = 0
        y = 0

        #loop to place all the labels for the columns above the input
        for x in columns:
            label = ttk.Label(self.topFrame, text = x)
            label.grid(row = 0, column = y, columnspan = 1)
            y = y + 1
        
        
        
            
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
    root.mainloop()
if __name__ == "__main__": main()
