__author__ = 'NafizFarhan'

#import tkinter
#from tkinter import ttk

from tkinter import *
from tkinter import ttk
from serial import *


import threading
import time
import os

class GUI(Frame):
  def __init__(self,master):
    frame = Frame(master)
    frame.pack()
    # Serial Port Setting Related Variables 
    self.port = 'COM1'
    self.baudrate = 9600
    # Serial slogan prompt 
    self.lab1 = Label(frame,text = 'Serial Number')
    self.lab1.grid(row = 0,column = 0,sticky = W)
    # Serial Password Selection Dropdown Menu 
    self.boxValue = StringVar()
    self.boxChoice = ttk.Combobox(frame,textvariable = self.boxValue,state = 'readonly')
    self.boxChoice['value'] = ('COM1','COM2','COM3','COM4')
    self.boxChoice.current(0)
    self.boxChoice.bind('<<ComboboxSelected>>',self.Choice)
    self.boxChoice.grid(row = 1,column = 0,sticky = W)
    # Baud Rate Selection Tips 
    self.lab2 = Label(frame,text = 'Baudrate Set')
    self.lab2.grid(row = 2,column = 0,sticky = W)
    # Baud Rate Selection Dropdown Menu 
    self.boxValueBaudrate = IntVar()
    self.BaudrateChoice = ttk.Combobox(frame,textvariable = self.boxValueBaudrate,state = 'readonly')
    self.BaudrateChoice['value'] = (9600,115200)
    self.BaudrateChoice.current(0)
    self.BaudrateChoice.bind('<<ComboboxSelected>>',self.ChoiceBaudrate)
    self.BaudrateChoice.grid(row = 3,column = 0,sticky = W)
    # Output box prompt 
    self.lab3 = Label(frame,text = 'Message Show')
    self.lab3.grid(row = 0,column = 1,sticky = W)
    # Output Box 
    self.show = Text(frame,width = 40,height = 5,wrap = WORD)
    self.show.grid(row = 1,column = 1,rowspan = 4,sticky = W)
    # Input box prompt 
    self.lab4 = Label(frame,text = 'Input here,please!')
    self.lab4.grid(row = 5,column = 1,sticky = W)
    # Input Box 
    self.input = Entry(frame,width = 40)
    self.input.grid(row = 6,column = 1,rowspan = 4,sticky = W)
    # Input Button 
    self.button1 = Button(frame,text = "Input",command = self.Submit)
    self.button1.grid(row = 11,column = 1,sticky = E)
    # Serial Open Button 
    self.button2 = Button(frame,text = 'Open Serial',command = self.open)
    self.button2.grid(row = 7,column = 0,sticky = W)
    # Serial port close button 
    self.button3 = Button(frame,text = 'Close Serial',command = self.close)
    self.button3.grid(row = 10,column = 0,sticky = W)
    # Serial information prompt box 
    self.showSerial = Text(frame,width = 20,height = 2,wrap = WORD)
    self.showSerial.grid(row = 12,column = 0,sticky = W)
    # Serial Initialization Configuration 
    self.ser = Serial()
    self.ser.setPort(self.port)
    #self.ser.setBaudrate(self.baudrate)
    #self.ser.open()
    #print self.ser.isOpen()
    #print self.ser
  def Choice(self,event):
    context = self.boxValue.get()
    list = ["COM1",'COM2','COM3','COM4']
    if context in list:
      self.port = list.index(context)
      self.ser.setPort(self.port)
    print(self.port)
  def ChoiceBaudrate(self,event):
    self.baudrate = self.boxValueBaudrate.get()
    self.ser.setBaudrate(self.baudrate)
    print(self.baudrate)
  def Submit(self):
    context1 = self.input.get()
    n = self.ser.write(context1)
    output = self.ser.read(n)
    print(output)
    self.show.delete(0.0,END)
    self.show.insert(0.0,output)
  def open(self):
    self.ser.open()
    if self.ser.isOpen() == True:
      self.showSerial.delete(0.0,END)
      self.showSerial.insert(0.0,"Serial has been opend!")
  def close(self):
    self.ser.close()
    if self.ser.isOpen() == False:
      self.showSerial.delete(0.0,END)
      self.showSerial.insert(0.0,"Serial has been closed!")
root = Tk()
root.title("Serial GUI")
#root.geometry("3000x4000")
app = GUI(root)
root.mainloop()