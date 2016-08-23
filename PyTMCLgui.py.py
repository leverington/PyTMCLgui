#!python.exe
# -*- coding: iso-8859-1 -*-
from TMCL import *
import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        label1 = Tkinter.Label(self,text='Speed', anchor="e",fg="black",bg="white")
        label1.grid(column=0,row=0,sticky='EW')


        self.slider1Variable = Tkinter.IntVar()
        slider1 = Tkinter.Scale(self, from_=1, to=2047, orient=Tkinter.HORIZONTAL, command=self.UpdateSlider1Value )
        slider1.grid(column=1,row=0,sticky='EW')
        self.slider1Variable.set(100)

        button1 = Tkinter.Button(self,text=u" Rel. Move ",width=10, command=self.RelativeMove)
        button1.grid(column=2,row=1)

        button2 = Tkinter.Button(self,text=u" Update ", width=10, command=self.GetPosition)
        button2.grid(column=2,row=2)

        button3 = Tkinter.Button(self,text=u" STOP ", width=10, command=self.StopWheel, fg="white", bg="red",bd=3)
        button3.grid(column=2,row=0)

        button4 = Tkinter.Button(self,text=u" Abs. Move ",width=10, command=self.AbsoluteMove)
        button4.grid(column=2,row=3)

        label2 = Tkinter.Label(self,text='Distance to move', anchor="e",fg="black",bg="white")
        label2.grid(column=0,row=1,sticky='EW')



        self.entryVariable = Tkinter.IntVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=1,row=1,sticky='EW')
#        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(12800)

        label3 = Tkinter.Label(self,text='Current Position', anchor="e",fg="black",bg="white")
        label3.grid(column=0,row=2,sticky='EW')

        self.label4Variable = Tkinter.IntVar()
        label4 = Tkinter.Label(self,textvariable=self.label4Variable,
                              anchor="w",fg="black",bg="white")
        label4.grid(column=1,row=2,sticky='EW')
        self.label4Variable.set(stepper.gap(0,1))

        label5 = Tkinter.Label(self,text='Move to pos.', anchor="e",fg="black",bg="white")
        label5.grid(column=0,row=3,sticky='EW')

        self.entry2Variable = Tkinter.IntVar()
        self.entry2 = Tkinter.Entry(self,textvariable=self.entry2Variable)
        self.entry2.grid(column=1,row=3,sticky='EW')
        #        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry2Variable.set(0)


        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=10,columnspan=3,sticky='EW')
        self.labelVariable.set(u"GUI by B. Leverington Aug. 2016")


        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def UpdateSlider1Value(self,speed):
        self.slider1Variable.set(speed)

    def OnButtonClick(self):
        self.labelVariable.set( self.entryVariable.get() )
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        movewheel(self)

#    def OnPressEnter(self,event):
#        self.labelVariable.set( self.entryVariable.get() )
#        self.entry.focus_set()
#        self.entry.selection_range(0, Tkinter.END)

    def RelativeMove(self):
        stepper.sap(0,4,self.slider1Variable.get())
        stepper.mvp(0,"REL",self.entryVariable.get())

    def AbsoluteMove(self):
        stepper.sap(0,4,self.slider1Variable.get())
        stepper.mvp(0,"ABS",self.entry2Variable.get())

    def GetPosition(self):
        self.label4Variable.set(stepper.gap(0,1))

    def StopWheel(self):
        stepper.mst(mn)



if __name__ == "__main__":
    stepper = TMCLDevice("COM3")
    mn = 0 # motor number
    app = simpleapp_tk(None)
    app.title('PyStepRocker GUI')
    app.mainloop()
