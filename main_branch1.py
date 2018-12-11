# Tapering it by making a copy of main.py file in branch1
# Aim: to implement the whole logic using classes

from tkinter import *
from web_crawler import *


class UtiliyFunctions(object):
    def __init__(self):
        pass

    def sendUrl(self, event):
        url = entry.get()
        extract(url)

    def clearEntry(self, event):
        entry.delete(0, 'end')

    def motion(self, event):  # https://stackoverflow.com/a/22925718
        x, y = event.x, event.y
        return str(str(x) + ", " + str(y))

    def doNothing(self):
        print("It does nothing, we'll implement it later!")


class PlotFrame(object):
    def __init__(self, root):
        # creating a utility object to use it for the whole class
        self.util = UtiliyFunctions()
        # ---- Top Frame------
        topFrame = Frame(root)
        topFrame.pack(side=TOP)

        myLabel_1 = Label(topFrame, text="Youtube Play List Title Extractor", fg='black')
        myLabel_1.config(font=("Helvetica 16 bold italic", 30))
        myLabel_1.pack()

        # ---- Middle Frame------
        middleFrame = Frame(root)
        middleFrame.pack(side=TOP)

        myLabel_2 = Label(middleFrame, text="Paste URL: ", fg='black')
        myLabel_2.grid(row=0, sticky=E)

        global entry
        entry = Entry(middleFrame, text="Paste Url: ", width=80)
        entry.grid(row=0, column=1)
        entry.focus_set()

        myButton = Button(middleFrame, text="Extract", height=5, width=20)
        myButton.bind("<Button-1>", self.util.sendUrl)
        myButton.grid(row=1, column=1)

        clearTextButton = Button(middleFrame, text="Clear")
        clearTextButton.bind("<Button-1>", self.util.clearEntry)
        clearTextButton.grid(row=1, column=2)

        # ---- Status Bar & Menu ------
        self.create_menu(root)
        self.create_statusBar(root)

    def create_statusBar(self, root):
        # statusBar = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        currentMousePosition = "Waiting for the url..."
        statusBar = Label(root, text=currentMousePosition, bd=1, relief=SUNKEN, anchor=W)
        statusBar.pack(side=BOTTOM, fill=X)

    def create_menu(self, root):
        menu = Menu(root)
        # we should configure the menu
        root.config(menu=menu)

        subMenu = Menu(menu)

        # drop down functionality is called 'cascading' in tkinter
        menu.add_cascade(label="File", menu=subMenu)

        # adding items to subMenu and giving functionality to it
        subMenu.add_command(label="New Project...", command=self.util.doNothing)
        subMenu.add_command(label="New...", command=self.util.doNothing)

        # a line to separate the items in the menu
        subMenu.add_separator()

        subMenu.add_command(label="Exit", command=self.util.doNothing)

        # creating an other menu item

        editMenu = Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label="Redo", command=self.util.doNothing)


class MyWindow(object):
    def __init__(self, root):
        root.title("Youtube playlist title's extractor")
        root.geometry("800x200")
        PlotFrame(root)


def main():
    print("Youtube PlayList Title Extractor!\nYou've 2 modes:\n1.GUI Mode\n2.CommandLine Mode")
    choice = int(input("Your option(1 or 2): "))
    if choice == 1:
        root = Tk()
        app = MyWindow(root)
        root.mainloop()
    else:
        print("\nI'll make it work later!\nThanks for using!\n")


if __name__ == '__main__':
    main()