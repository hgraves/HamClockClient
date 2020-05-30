from tkinter import *

import socket
from urllib.request import urlretrieve
import configparser

import os
import requests
import xmltodict
from configparser import SafeConfigParser

import sys

dispVal = 1


class HamClockClient:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.lbl_value = Label(frame, text="Display")
        self.lbl_value.pack(side=LEFT)

        self.btn_toggle = Button(frame, text="On", command=self.toggleDisplay)
        self.btn_toggle.pack(side=RIGHT)

    def toggleDisplay(self):
        global dispVal
        if dispVal == 1:
            self.btn_toggle["text"] = "Off"
            dispVal = 0
            print("Off")
            queryString = 'http://192.168.47.211/set_display?off'
            thing = urlretrieve(queryString)
        else:
            self.btn_toggle["text"] = "On"
            dispVal = 1
            print("On")
            queryString = 'http://192.168.47.211/set_display?on'
            thing = urlretrieve(queryString)


root = Tk()
hmc = HamClockClient(root)
root.mainloop()




