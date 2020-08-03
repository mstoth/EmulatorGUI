import tkinter
import unittest
from EmulatorGui import EmulatorGui
from tkinter import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.g = EmulatorGui()

    def tearDown(self) -> None:
        self.g.get_canvas().delete("all")

    def test_gui(self):
        self.g.set_geometry("600x800")
        print(self.g.geometry())

    def test_emulator(self):
        e = self.g.emulator()

    def test_displays(self):
        root = self.g.display()
        root.geometry="600x800"

    def test_inst(self):
        s = self.g.em.inst
        self.g.inst = self.g.em.inst
        args = [1, int(s[0]), int(s[1]), int(s[2])]
        self.assertTrue(args == [1, 0, 0, 0])

    def test_items(self):
        self.assertTrue(type(self.g.get_canvas()) == tkinter.Canvas)
        self.assertTrue(type(self.g.getButtonFrame()) == tkinter.Frame)
        self.assertTrue(type(self.g.getIOFrame()) == tkinter.Frame)
        self.assertTrue(type(self.g.getIOFrame().inputEntry) == tkinter.Entry)
        self.assertTrue(type(self.g.getIOFrame().outputEntry) == tkinter.Entry)
        self.assertTrue(type(self.g.mem) == tkinter.Text)

    def test_load_program(self):
        self.g.fname.set("simpleNim.asm")
        self.g.loadProgram()
        s = self.g.em.get_dump()
        self.assertTrue(s.index('013') > 0)
        s2 = self.g.mem.get(1.0, "end")
        self.assertTrue(s2.index('013') > 0)


if __name__ == '__main__':
    unittest.main()
