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



        label1 = Tkinter.Label(self,text='Speed', anchor="center",fg="black")
        label1.grid(column=0,row=0,sticky='EW')


        self.slider1Variable = Tkinter.IntVar()
        slider1 = Tkinter.Scale(self, from_=1, to=2047, orient=Tkinter.HORIZONTAL, command=self.UpdateSlider1Value )
        slider1.grid(column=1,row=0,sticky='EW')
        #self.slider1Variable.set(100)
        slider1.set(1000)

        label1a = Tkinter.Label(self,text='Accel.', anchor="center",fg="black")
        label1a.grid(column=2,row=0,sticky='EW')


        self.slider1aVariable = Tkinter.IntVar()
        slider1a = Tkinter.Scale(self, from_=1, to=2047, orient=Tkinter.HORIZONTAL, command=self.UpdateSlider1aValue )
        slider1a.grid(column=3,row=0,sticky='EW')
        #self.slider1Variable.set(100)
        slider1a.set(1000)

        button1 = Tkinter.Button(self,text=u" Rel. Move ",width=10, command=self.RelativeMove)
        button1.grid(column=2,row=1)

        button2 = Tkinter.Button(self,text=u" Update ", width=10, command=self.GetPosition)
        button2.grid(column=2,row=2)

        button3 = Tkinter.Button(self,text=u" STOP ", width=10, command=self.StopWheel, fg="white", bg="red",bd=3)
        button3.grid(column=5,row=0)

        button4 = Tkinter.Button(self,text=u" Abs. Move ",width=10, command=self.AbsoluteMove)
        button4.grid(column=2,row=3)

        button5 = Tkinter.Button(self,text=u" Reset ",width=10, command=self.ResetPosition)
        button5.grid(column=3,row=2)

        button6 = Tkinter.Button(self,text=u" Get Par. ",width=10, command=self.GetAxisPar)
        button6.grid(column=3,row=5)

        button7 = Tkinter.Button(self,text=u" Get Par. ",width=10, command=self.GetGlobalPar)
        button7.grid(column=3,row=6)

        label2 = Tkinter.Label(self,text='Distance to move', anchor="e",fg="black")
        label2.grid(column=0,row=1,sticky='EW')



        self.entryVariable = Tkinter.IntVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=1,row=1,sticky='EW')
#        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(12800)

        label3 = Tkinter.Label(self,text='Current Position', anchor="e",fg="black")
        label3.grid(column=0,row=2,sticky='EW')

        self.label4Variable = Tkinter.IntVar()
        label4 = Tkinter.Label(self,textvariable=self.label4Variable,
                              anchor="w",fg="black")
        label4.grid(column=1,row=2,sticky='EW')
        self.label4Variable.set(stepper.gap(0,1))

        label5 = Tkinter.Label(self,text='Move to pos.', anchor="e",fg="black")
        label5.grid(column=0,row=3,sticky='EW')

        label6 = Tkinter.Label(self,text='12800 = 1 rev', anchor="center",fg="black")
        label6.grid(column=3,row=1,sticky='EW')

        emptylabel = Tkinter.Label(self,text=' ', anchor="center")
        emptylabel.grid(column=0,row=4,columnspan=4,sticky='EW')

        label7 = Tkinter.Label(self,text='Axis Par. (gap)', anchor="e",fg="black")
        label7.grid(column=0,row=5,sticky='EW')

        label8 = Tkinter.Label(self,text='Global Par. (ggp)', anchor="e",fg="black")
        label8.grid(column=0,row=6,sticky='EW')

        self.entry2Variable = Tkinter.IntVar()
        self.entry2 = Tkinter.Entry(self,textvariable=self.entry2Variable)
        self.entry2.grid(column=1,row=3,sticky='EW')
        #        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry2Variable.set(0)


        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=10,columnspan=4,sticky='EW')
        self.labelVariable.set(u"GUI by B. Leverington Aug. 2016")

        self.entry3Variable = Tkinter.IntVar()
        self.entry3 = Tkinter.Entry(self,textvariable=self.entry3Variable)
        self.entry3.grid(column=1,row=5,sticky='EW')
        #        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry3Variable.set(1)


        self.label9Variable = Tkinter.IntVar()
        label9 = Tkinter.Label(self,textvariable=self.label9Variable,
                      anchor="w",fg="black")
        label9.grid(column=2,row=5,sticky='W')
        self.label9Variable.set(0)

        self.entry4Variable = Tkinter.IntVar()
        self.entry4 = Tkinter.Entry(self,textvariable=self.entry4Variable)
        self.entry4.grid(column=1,row=6,sticky='EW')
        #        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry4Variable.set(1)

        self.label10Variable = Tkinter.IntVar()
        label10 = Tkinter.Label(self,textvariable=self.label10Variable,
              anchor="w",fg="black")
        label10.grid(column=2,row=6,sticky='W')
        self.label10Variable.set(0)

        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def UpdateSlider1Value(self,speed):
        self.slider1Variable.set(speed)

    def UpdateSlider1aValue(self,accel):
        self.slider1aVariable.set(accel)

    def RelativeMove(self):
        stepper.sap(0,4,self.slider1Variable.get()) #set the maximum speed
        stepper.sap(0,5,self.slider1aVariable.get()) #set the maximum acceleration
        stepper.mvp(0,"REL",self.entryVariable.get()) #move to relative coordinate

    def AbsoluteMove(self):
        stepper.sap(0,4,self.slider1Variable.get()) #set the maximum speed
        stepper.sap(0,5,self.slider1aVariable.get()) #set the maximum acceleration
        stepper.mvp(0,"ABS",self.entry2Variable.get()) #move to abs coordinate

    def GetPosition(self):
        self.label4Variable.set(stepper.gap(0,1)) # get current position

    def ResetPosition(self):
        stepper.sap(0,4,0) #set the maximum speed to zero
        stepper.sap(0,0,0) #set current position as zero
        stepper.sap(0,1,0) #set target position as zero
        stepper.mst(mn) # motor stop
        self.label4Variable.set(stepper.gap(0,1)) #get current position again

    def StopWheel(self):
        stepper.mst(mn) # motor stop

    def GetAxisPar(self):
        self.label9Variable.set(stepper.gap(0,self.entry3Variable.get())) # get current position

    def GetGlobalPar(self):
        self.label10Variable.set(stepper.ggp(0,self.entry4Variable.get())) # get current position


if __name__ == "__main__":
    stepper = TMCLDevice("COM3")
    mn = 0 # motor number
    app = simpleapp_tk(None)
    app.title('PyStepRocker GUI')
    app.mainloop()
