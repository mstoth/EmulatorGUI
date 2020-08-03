from tkinter import *
from cardiacgui import CardiacDisplay
from testEmulator import Emulator
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)  # expand frame to fill window


class EmulatorGui():

    def __init__(self,master=None):
        self.root = master
        self.app = Window(self.root)
        self.root.wm_title("CARDIAC")
        self.root.geometry("600x800")
        self.em = Emulator()
        self.cd = CardiacDisplay()
        self.cardiacCanvas = Canvas(self.root, width=500, height=500)
        cardiacImage = self.cd.get_image(1, 2, 3, 4)
        renderedImage = ImageTk.PhotoImage(cardiacImage.resize((500, 500), Image.ANTIALIAS))
        self.cardiacCanvas.create_image(20, 20, anchor=NW, image=renderedImage)
        self.cardiacCanvas.image = renderedImage
        self.cardiacCanvas.pack()
        self.buttonFrame = Frame(self.root, width=500, height=200)
        button = Button(self.buttonFrame, text="View", padx=5, command=self.updateDisplay)
        button.pack(side=LEFT, padx=5)
        button2 = Button(self.buttonFrame, text="Reset", padx=5, command=self.reset)
        button2.pack(side=LEFT, padx=5)
        button3 = Button(self.buttonFrame, text="Step", padx=5, command=self.step)
        button3.pack(side=LEFT, padx=5)
        button4 = Button(self.buttonFrame, text="Load Program", padx=5, command=self.loadProgram)
        button4.pack(side=LEFT, padx=5)
        self.fname = StringVar()
        self.fileName = Entry(self.buttonFrame, width=14, textvariable=self.fname)
        self.fileName.pack(side=LEFT)
        button5 = Button(self.buttonFrame, text="Load Input", padx=5, command=self.loadInput)
        button5.pack(side=LEFT, padx=5)
        self.iname = StringVar()
        self.ifileName = Entry(self.buttonFrame, width=14, textvariable=self.iname)
        self.ifileName.pack(side=LEFT)
        self.buttonFrame.pack()
        self.ioFrame = Frame(self.root, width=500, height=200)
        self.input_stream = StringVar()
        self.input_stream.set(value=str(self.em.input_stream))
        # self.em.input_stream = self.input_stream.get().split(",")
        self.ioFrame.inputEntry = Entry(self.ioFrame, width=40, textvariable=self.input_stream)
        self.ioFrame.inputEntry.pack(side=LEFT, padx=10)
        self.output_stream = StringVar()
        self.output_stream.set(str(self.em.output_stream))
        self.ioFrame.outputEntry = Entry(self.ioFrame, width=40, textvariable=self.output_stream)
        self.ioFrame.outputEntry.pack(side=LEFT)
        self.ioFrame.pack()
        self.regFrame = Frame(self.root, width=500, height=200, pady=10)

        acc = StringVar()
        acc.set("Acc: ")
        self.regFrame.accLabel = Label(self.regFrame, textvariable=acc)
        self.regFrame.accLabel.pack(side=LEFT)

        self.acce = StringVar()
        self.regFrame.accEntry = Entry(self.regFrame, width=10, textvariable=self.acce)
        self.regFrame.accEntry.pack(side=LEFT)

        inst = StringVar()
        inst.set("Inst: ")
        self.regFrame.instLabel = Label(self.regFrame, textvariable=inst)
        self.regFrame.instLabel.pack(side=LEFT)

        self.inste = StringVar()
        self.regFrame.instEntry = Entry(self.regFrame, width=10, textvariable=self.inste)
        self.regFrame.instEntry.pack(side=LEFT)

        pc = StringVar()
        pc.set("PC: ")
        self.regFrame.pcLabel = Label(self.regFrame, textvariable=pc)
        self.regFrame.pcLabel.pack(side=LEFT)

        self.pce = StringVar()
        self.regFrame.pcEntry = Entry(self.regFrame, width=10, textvariable=self.pce)
        self.regFrame.pcEntry.pack(side=LEFT)

        self.regFrame.sendButton = Button(self.regFrame, padx=10, text="Send", command=self.send)
        self.regFrame.sendButton.pack(side=LEFT, padx=10)
        self.regFrame.retrieveButton = Button(self.regFrame, padx=10, text="Retrieve", command=self.retrieve)
        self.regFrame.retrieveButton.pack(side=LEFT, padx=10)
        self.regFrame.pack()
        self.mem = Text(self.root, width=300, height=500, padx=120)
        self.mem.delete(1.0, "end")
        s = self.em.get_dump()
        self.mem.insert(1.0, s)
        self.mem.pack()

    def updateDisplay(self):
        self.inputListPointer = self.em.istream
        self.inste.set(self.em.inst)
        self.pce.set(str(self.em.pc))
        self.input_stream.set(str(self.em.input_stream))
        self.output_stream.set(str(self.em.output_stream))
        self.acce.set(str(self.em.acc))
        s = self.em.inst
        args = [1, int(s[0]), int(s[1]), int(s[2])]
        load = self.cd.get_image(int(args[0]), int(args[1]), int(args[2]), int(args[3]))
        render = ImageTk.PhotoImage(load.resize((500, 500), Image.ANTIALIAS))
        self.get_canvas().create_image(20, 20, anchor=NW, image=render)
        self.get_canvas().image = render
        s = self.em.get_dump()
        self.mem.delete(1.0, "end")
        self.mem.insert(1.0, s)

    def send(self):
        self.em.acc = self.acce.get()
        self.em.inst = self.inste.get()
        self.em.pc = int(self.pce.get())
        self.updateDisplay()

    def retrieve(self):
        self.acce.set(str(self.em.acc))
        self.inste.set(self.em.inst)
        self.pce.set(str(self.em.pc))
        self.updateDisplay()

    def reset(self):
        self.em.reset()
        self.updateDisplay()

    def loadProgram(self):
        if len(self.fname.get()) > 0:
            self.em.loadProgram(self.fname.get())
        self.updateDisplay()

    def loadInput(self):
        if len(self.iname.get()) > 0:
            self.em.loadInput(self.iname.get())
        self.updateDisplay()

    def step(self):
        self.em.step(1)
        self.updateDisplay()

    def set_geometry(self, g):
        self.root.geometry = g

    def geometry(self):
        return self.root.geometry

    def emulator(self):
        return self.em

    def display(self):
        return self.root

    def get_canvas(self) -> Canvas:
        return self.cardiacCanvas

    def getButtonFrame(self) -> Frame:
        return self.buttonFrame

    def getIOFrame(self):
        return self.ioFrame


if __name__ == "__main__":
    root = Toplevel()
    g=EmulatorGui(root)
    mainloop()
