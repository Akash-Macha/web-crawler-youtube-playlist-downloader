# Tapering it by making a copy of main.py file in branch1
# Aim: to implement the whole logic using classes

from tkinter import *
from web_crawler import *
from latest_web_crawler import *
from tkinter.filedialog import *
from tkinter import filedialog
from tkinter import ttk



class PlotFrame(object):
    def __init__(self, root=None):
        # creating a utility object to use it for the whole class
        # self.util = UtiliyFunctions()
        # ---- Top Frame------
        topFrame = Frame(root)
        topFrame.pack(side=TOP)

        myLabel_1 = Label(topFrame, text="Youtube Play List Title Extractor", fg='black')
        myLabel_1.config(font=("Helvetica 16 bold italic", 30))
        myLabel_1.grid(row=0)

        # ---- Middle Frame------
        middleFrame = Frame(root)
        middleFrame.pack(side=TOP)

        myLabel_2 = Label(middleFrame, text="Paste URL: ", fg='black')
        myLabel_2.grid(row=1, sticky=E)

        styleEntry = ttk.Style()
        styleEntry.configure("TEntry",
                             padding=5)
        self.entry = ttk.Entry(middleFrame, width=80)
        self.entry.grid(row=1, column=1)
        self.entry.focus_set()

        # --------- crating check button ---------

        self.checkButtonStatus = IntVar()
        self.checkButtonStatus.set(1)
        checkButton = Checkbutton(middleFrame,
                                  text="make a text file with those titles? ",
                                  variable=self.checkButtonStatus,
                                  ).grid(row=2, column=1, pady=10)  # sticky=N
        # print("creating check button:  ", self.checkButtonStatus.get())

        self.checkButtonDownloadPlayListStatus = IntVar()
        self.checkButtonDownloadPlayListStatus.set(1)
        checkButtonDownloadPlayList = Checkbutton(middleFrame,
                                  text="Download the complete Playlist? ",
                                  variable=self.checkButtonDownloadPlayListStatus,
                                  ).grid(row=3, column=1, pady=10)  # sticky=N

        # ------- creating and styling the extract button -----------
        style = ttk.Style()
        style.configure("TButton",
                        foreground="black",
                        font="Arial 15 bold",
                        padding=20)

        extractButton = ttk.Button(middleFrame,
                                   text="Extract",
                                   command=self.sendUrl)  # command will take a function, which will be invoked onclick!
        extractButton.grid(row=4, column=1, pady=15)


        # extractButton = Button(middleFrame, text="Extract", height=4, width=20)
        # extractButton.bind("<Button-1>", self.sendUrl)
        ''' extractButton.bind("<Button-1>", self.setStatusBarToProcessing) '''
        # extractButton.grid(row=3, column=1, pady=30)


        clearTextButton = Button(middleFrame, text="Clear", fg='green')
        clearTextButton.bind("<Button-1>", self.clearEntry)
        clearTextButton.grid(row=3, column=2, sticky=W, padx=1)


        # ---- Status Bar & Menu ------
        self.create_menu(root)
        self.create_statusBar(root)
        # self.create_innerView(root)

    # def create_innerView(self, root):


    def setStatusToEnterCorrectUrl(self):
        self.currentStatus.set("Enter correct Url please!")

    def sendUrl(self):
        self.currentStatus.set("Processing...")
        url = self.entry.get()

        path = filedialog.askdirectory()

        try:
            titles = download_playlist_and_get_video_titles(url, path)
        except requests.exceptions.MissingSchema:  # exception raised for bad url
            self.currentStatus.set("Invalid or Empty Url, Please enter the correct url...")
            self.clearEntry()
            return
        # print(self.checkButtonStatus)
        if self.checkButtonStatus.get() == 1:
            self.file_save(titles, url)

        # if self.checkButtonDownloadPlayListStatus.get() == 1:
        #     pass
        #     path = filedialog.askdirectory()
        #     downloadCompletePlayList(url, path)

        self.currentStatus.set("Task Completed! Waiting for new Url!")

    def file_save(self, titles, url):
        """get a filename and save the text in the editor widget """
        # default extension is optional, here we'll add .txt if missing
        fout = asksaveasfile(mode='w', defaultextension='.txt')
        text2save = self.gatherRequiredInfo(titles, url)

        fout.write(text2save)
        fout.close()

    def gatherRequiredInfo(self, titles, url):
        return "Url: " + url + "\n\n" + "\n".join(titles)


    def clearEntry(self, event=None):
        self.entry.delete(0, 'end')

    # def motion(self, event):  # https://stackoverflow.com/a/22925718
    #     x, y = event.x, event.y
    #     self.currentStatus.set("Mouse is at: " + str(str(x) + ", " + str(y)))

    def doNothing(self):
        print("It does nothing, we'll implement it later!")

    def setStatusBarToProcessing(self, event):
        pass

    def returnCurrentMousePosition(self, event=None):
        return str(str(event.x) + ", " + str(event.y))

    def create_statusBar(self, root):
        self.currentStatus = StringVar()
        self.currentStatus.set("Waiting for url...")
        # root.bind("<Motion>", self.motion)

        statusBar = Label(root, textvariable=self.currentStatus, bd=1, relief=SUNKEN, anchor=W)
        statusBar.bind("<Motion>", self.returnCurrentMousePosition)
        statusBar.pack(side=BOTTOM, fill=X)

    def create_menu(self, root):
        menu = Menu(root)
        # we should configure the menu
        root.config(menu=menu)

        subMenu = Menu(menu)

        # drop down functionality is called 'cascading' in tkinter
        menu.add_cascade(label="File", menu=subMenu)

        # adding items to subMenu and giving functionality to it
        subMenu.add_command(label="New Project...", command=self.doNothing)
        subMenu.add_command(label="New...", command=self.doNothing)

        # a line to separate the items in the menu
        subMenu.add_separator()

        subMenu.add_command(label="Exit", command=root.quit)

        # creating an other menu item

        editMenu = Menu(menu)
        menu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label="Redo", command=self.doNothing)

        helpMenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpMenu)
        helpMenu.add_command(label="About", command=self.doNothing)

# class LowerFrame(object):
#     def __init__(self, root):
#         lowerFrame = Frame(root)
#         lowerFrame.pack(side=BOTTOM)




class MyWindow(object):
    def __init__(self, root):
        root.title("Youtube playlist title's extractor")
        root.geometry("800x300")
        PlotFrame(root)

        # LowerFrame(root)


def main():
    root = Tk()
    app = MyWindow(root)
    root.mainloop()
    # print("Youtube PlayList Title Extractor!\nYou've 2 modes:\n1.GUI Mode\n2.CommandLine Mode")
    # choice = int(input("Your option(1 or 2): "))
    # if choice == 1:
    #     root = Tk()
    #     app = MyWindow(root)
    #     root.mainloop()
    # else:
    #     print("\nI'll make it work later!\nThanks for using!\n")


if __name__ == '__main__':
    main()
