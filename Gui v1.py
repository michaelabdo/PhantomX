#!/usr/bin/python3
#Joshua Pierce

from tkinter import *
from tkinter import ttk
columns = ["column1", "column2", "column3", "column4"]
class alphaFrame:
    
    def __init__(self, Root):
        #sets size of window on open
        Root.geometry('600x400')
        
        #Frame is set to use Pack method, to fill space across with a border
        self.topFrame = ttk.Frame(Root)
        self.topFrame.pack(fill = BOTH)
        self.topFrame.config(relief = SOLID)
        
        #Text input to take the input from user, each column relates to a physical column for the arm
        
        y = 0
        for x in columns:
            x = Text(self.topFrame, width = 10, height = 1)
            x.grid(row = 0, column = y, columnspan = 1)
            y = y + 1
            
        
        
        #Padding prevents frame from collapsing around button, err known on mac
        self.topFrame.config(padding = (30,50))

        #Frame defined as buffer for future dev, for visuals or other features, ignore or delete
        
        #self.middleFrame = ttk.Frame(Root)
        #self.middleFrame.pack(fill = BOTH)
        #self.middleFrame.config(relief = SOLID)
        
        #reset = ttk.Button(self.middleFrame, text = 'reset')
        #reset.grid(row = 0, column = 0, columnspan = 1)
        #self.middleFrame.config(padding = (30,50))

        #
        
        #Frame is directly under topframe by order of pack methods called
        self.botomFrame = ttk.Frame(Root)
        self.botomFrame.pack(fill = BOTH)
        self.botomFrame.config(relief = SOLID)
        
        #future reset and run buttons
        reset = ttk.Button(self.botomFrame, text = 'reset')
        reset.grid(row = 0, column = 0, columnspan = 1)
        
        run = ttk.Button(self.botomFrame, text = 'run')
        run.grid(row = 0, column = 2, columnspan = 1)
        self.botomFrame.config(padding = (30,50))


def main():
    root = Tk()
    app = alphaFrame(root)
    root.mainloop()
if __name__ == "__main__": main()
