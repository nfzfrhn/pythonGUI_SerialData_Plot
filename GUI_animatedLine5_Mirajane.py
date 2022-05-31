from doctest import master
from secrets import choice
import tkinter
#import tkinter as tk       #If we do this, then we can write tk.W instead of tkinter.W
from tkinter import StringVar, ttk

import matplotlib
matplotlib.use('TkAgg')

from serial import *
import serial.tools.list_ports

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class MainSerial:
    def __init__(self):
        
        #Initialize Form
        self.mainwin = tkinter.Tk()
        self.mainwin.title("Serial Communication Receiver")
        self.mainwin.geometry('1200x800')    

        # Initialize Serial Port
        self.ser = Serial()  
        self.ser.baudrate = 115200
        self.ser.port='COM12'      

        # Grid layout for the input frame
        self.mainwin.rowconfigure(0, weight=1)
        #self.mainwin.rowconfigure(0, weight=1)
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
        self.boxValue = StringVar()
        self.boxChoice = ttk.Combobox(frame1,textvariable=self.boxValue,state='readonly')
        self.boxChoice['value'] = [comport.device for comport in serial.tools.list_ports.comports()]
        self.boxChoice.current()
        self.boxChoice.bind('<<ComboboxSelected>>',self.ChoicePort)
        self.boxChoice.grid(column=1,row=0,sticky=tkinter.W)
        ttk.Label(frame1,text='Select BaudRate:').grid(column=0,row=1, sticky=tkinter.W, padx=5)
        self.boxValueBaudrate = [9600,115200]
        self.BaudrateChoice = ttk.Combobox(frame1,state = 'readonly')
        self.BaudrateChoice['value'] = (9600,115200)
        self.BaudrateChoice.current(0)
        self.BaudrateChoice.bind('<<ComboboxSelected>>',self.ChoiceBaudrate)
        self.BaudrateChoice.grid(column=1,row=1, sticky = tkinter.W)
        scanButton = ttk.Button(frame1, text='Scan',command=self.callback_buttonScanClicked)
        scanButton.grid(column=2,row=1, sticky=tkinter.E, padx=30)
        #portNumber = ttk.Entry(frame1, width=10)
        #portNumber.focus()
        #portNumber.grid(column=1, row=0, sticky=tkinter.W)   
        # Connect Button
        connectButton = ttk.Button(frame1, text='Connect', command=self.callback_buttonConnectClicked)
        connectButton.grid(column=2,row=0, stick=tkinter.E,padx=30)
        ttk.Label(frame1, text='Status:').grid(column=3, row=0, sticky=tkinter.W)
        status = ttk.Label(frame1, text='Disconnected').grid(column=4, row=0, sticky=tkinter.W, padx=5)

        ## Frame3 
        figure = Figure(figsize=(6,4), dpi=100)
        axes = figure.add_subplot(111)
        # Create FigureCanvasTkAgg object
        canvas = FigureCanvasTkAgg(figure, master=frame3)

        # Create the toolbar
        #NavigationToolbar2Tk(canvas, self)

        canvas.get_tk_widget().grid(column=0,row=0)

        frame1.grid(column=0,row=0)
        frame2.grid(column=0,row=1)
        frame3.grid(column=0,row=2)
        frame4.grid(column=0,row=3)

    def ChoicePort(self, event):
        context = self.boxValue.get()
        list = [comport.device for comport in serial.tools.list_ports.comports()]
        if context in list:
            self.port = list.index(context)
            self.ser.setPort(self.port)
        print("This is context"+context)
        print("This is port"+self.port)

    def ChoiceBaudrate(self,event):
        self.baudrate = self.boxValueBaudrate.get()
        self.ser.setBaudrate(self.baudrate)
        print(self.baudrate)        

    def callback_buttonConnectClicked(self):
        if self.ser.isOpen():
            self.ser.close()        
        self.ser.open()
        serialString =""
        self.ser.write("CNN\r\n".encode())
        serialString = self.ser.readline()
        self.ser.flushInput()
        #ser_bytes = self.ser.readline() 
        ser_bytes = self.ser.read(self.ser.inWaiting)       
        #decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))        
        if self.ser.isOpen():
            print("Success!")
            print(ser_bytes)

    def callback_buttonScanClicked(self):
        if self.ser.isOpen():
            self.ser.close()
            print("Port closed!")

    def show(self):
        self.mainwin.mainloop()




if __name__ == "__main__":
	my_ser1 = MainSerial()
	my_ser1.show()