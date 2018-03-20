from tkinter import *
from tkinter import ttk
import time
import malespeaker


def query_gui(k):
    root = Tk()
    t = StringVar()
    content = ttk.Frame(root, padding=(3, 3, 12, 12))
    frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=500, height=600)
    namelbl2 = ttk.Label(frame, text=k)
    namelbl = ttk.Label(content, text="Please write your query")
    name = ttk.Entry(content, textvariable=t)

    ok = ttk.Button(content, text="Record")
    cancel = ttk.Button(content, text="OK")

    content.grid(column=0, row=0, sticky=(N, S, E, W))
    frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    namelbl2.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
    name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

    ok.grid(column=3, row=3)
    cancel.grid(column=4, row=3)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    content.columnconfigure(0, weight=3)
    content.columnconfigure(1, weight=3)
    content.columnconfigure(2, weight=3)
    content.columnconfigure(3, weight=1)
    content.columnconfigure(4, weight=1)
    content.rowconfigure(1, weight=1)
    # print('current value is %s' % name.get())

    # print(k)
    root.after(6000, lambda: root.destroy())
    root.mainloop()


if __name__ == '__main__':
    query_gui("name.get()\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t")