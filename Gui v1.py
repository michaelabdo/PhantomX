#!/usr/bin/python3
#Joshua Pierce

from tkinter import *
from tkinter import ttk

class alphaFrame:

    def __init__(self, Root):
        Root.geometry('600x400')

        self.topFrame = ttk.Frame(Root)
        self.topFrame.pack(fill = BOTH)
        self.topFrame.config(relief = SOLID)
        
        reset = ttk.Button(self.topFrame, text = 'reset')
        reset.grid(row = 0, column = 0, columnspan = 1)
        self.topFrame.config(padding = (30,50))

        #
        
        #self.middleFrame = ttk.Frame(Root)
        #self.middleFrame.pack(fill = BOTH)
        #self.middleFrame.config(relief = SOLID)
        
        #reset = ttk.Button(self.middleFrame, text = 'reset')
        #reset.grid(row = 0, column = 0, columnspan = 1)
        #self.middleFrame.config(padding = (30,50))

        #
        self.botomFrame = ttk.Frame(Root)
        self.botomFrame.pack(fill = BOTH)
        
        
       
        self.botomFrame.config(relief = SOLID)
        
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
