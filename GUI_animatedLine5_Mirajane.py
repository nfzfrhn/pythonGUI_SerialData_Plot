import tkinter
#import tkinter as tk       #If we do this, then we can write tk.W instead of tkinter.W
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class MainSerial:
    def __init__(self):
        
        #Initialize Form
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Serial Communication Receiver")
        self.mainwin.geometry('1200x800')        

        # Grid layout for the input frame
        self.mainwin.rowconfigure(0, weight=1)
        self.mainwin.rowconfigure(0, weight=1)
        self.mainwin.rowconfigure(0, weight=2)
        self.mainwin.rowconfigure(0, weight=2)

        frame1 = ttk.Frame(self.mainwin)
        frame2 = ttk.Frame(self.mainwin)
        frame3 = ttk.Frame(self.mainwin)
        frame4 = ttk.Frame(self.mainwin)

        ## Frame1 is the top row
        frame1.columnconfigure(0,weight=1)
        frame1.columnconfigure(0,weight=1)
        frame1.columnconfigure(0,weight=1)
        frame1.columnconfigure(0,weight=1)
        # Select Port Number
        ttk.Label(frame1, text='Select Port Number:').grid(column=0, row=0, sticky=tkinter.W, padx=5)
        portNumber = ttk.Entry(frame1, width=10)
        portNumber.focus()
        portNumber.grid(column=1, row=0, sticky=tkinter.W)   
        # Connect Button
        connectButton = ttk.Button(frame1, text='Connect')
        connectButton.grid(column=2,row=0, stick=tkinter.E,padx=30)
        ttk.Label(frame1, text='Status:').grid(column=3, row=0, sticky=tkinter.W)
        status = ttk.Label(frame1, text='Disconnected').grid(column=4, row=0, sticky=tkinter.W, padx=5)

        ## Frame2 is the second row
        frame2.columnconfigure(0,weight=1)
        frame2.columnconfigure(0,weight=1)
        frame2.columnconfigure(0,weight=1)
        frame2.columnconfigure(0,weight=1)
        frame2.columnconfigure(0,weight=1)
        # Scan button
        ttk.Button(frame2, text='Scan').grid(column=0,row=0, sticky=tkinter.W, padx=10)        
        # Select LPF setting
        ttk.Label(frame2, text='Select LPF setting:').grid(column=1, row=0, sticky=tkinter.W)
        ttk.Entry(frame2, width=10).grid(column=2, row=0, sticky=tkinter.W)
        # Select X,Y,Z Offset
        ttk.Label(frame2, text='Select X-Offset:').grid(column=3, row=0, sticky=tkinter.W)
        ttk.Entry(frame2, width=10).grid(column=4, row=0, sticky=tkinter.W)        
        ttk.Label(frame2, text='Select Y-Offset:').grid(column=3, row=1, sticky=tkinter.W)
        ttk.Entry(frame2, width=10).grid(column=4, row=1, sticky=tkinter.W)
        ttk.Label(frame2, text='Select Z-Offset:').grid(column=3, row=2, sticky=tkinter.W)
        ttk.Entry(frame2, width=10).grid(column=4, row=2, sticky=tkinter.W)

        frame1.grid(column=0,row=0)
        frame2.grid(column=0,row=1)
        frame3.grid(column=0,row=2)
        frame4.grid(column=0,row=3)

    def show(self):
        self.mainwin.mainloop()

    #def callback_buttonClicked(args):
        #ghgh


if __name__ == "__main__":
	my_ser1 = MainSerial()
	my_ser1.show()