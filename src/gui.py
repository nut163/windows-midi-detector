```python
import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MIDI Controller Monitor")
        self.tree = ttk.Treeview(self.root, columns=('Key', 'Knob', 'Velocity'))
        self.tree.heading('#0', text='Event')
        self.tree.heading('#1', text='Key')
        self.tree.heading('#2', text='Knob')
        self.tree.heading('#3', text='Velocity')
        self.tree.pack()

    def display_midi(self, midi_info):
        for event in midi_info:
            self.tree.insert('', 'end', text=event['event'], values=(event['key'], event['knob'], event['velocity']))

    def run(self):
        self.root.mainloop()
```
This code creates a GUI using tkinter that displays MIDI events in a table. The `display_midi` function takes a list of MIDI events and adds them to the table. The `run` function starts the GUI.