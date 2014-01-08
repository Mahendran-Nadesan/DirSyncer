#-------------------------------------------------------------------------------
# Name:        syncgui
# Purpose:     tkinter gui for dirsync project
#
# Author:      Mahen
#
# Created:     24/12/2013
# Copyright:   (c) Mahen 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

## For help:
## http://stackoverflow.com/questions/17466561/python-tkinter-program-structure
## http://stackoverflow.com/questions/7300072/tkinter-inherit-from-frame-or-not
##
## Current issues (29/12):
## 1. How can I keep the size of the message frame the same (from when I click Browse and it changes dir_1)
## 2. How can I add arguments to callbacks, so that I can have a general browse callbacks, and feed different dir vars.
##
## To do (29/12):
## 1. Make error messages for when a button is pressed before its preceding button (pressing Sync before Browse)
## 2. OR (and I like this better), disable the side sync buttons until both dirs have been set. Which leads to:
## 3. How do I enable the buttons once self.dir_1 and self.dir_2 have non-default values?
## 4. Make sure the sync buttons (in row0 & 1) actually do syncing (as masters, for the "deleted file" problem.

# Imports
from Tkinter import *
import tkFileDialog
from sync import *

# Main GUI Class
class SyncGui(Frame):
    def __init__(self, title, master=None, padding="30 30 120 120"):
        Frame.__init__(self, master)
        self.master.title(title)
        self.colors = ['red', 'blue', 'green', 'yellow', 'white', 'black', 'red', 'purple']

        self.topframe = Frame(self.master, bg='red')
        self.topframe.grid(column=0, row=0)
        self.topframe.grid_rowconfigure(0, minsize=60)
##        self.topframe.grid_columnconfigure(0, minsize=150)
##        self.topframe.pack(side=TOP, expand=True, fill=BOTH)
        self.midframe = Frame(self.master, bg='blue')
        self.midframe.grid(column=0, row=1)
        self.midframe.grid_rowconfigure(0, minsize=60)
##        self.midframe.grid_columnconfigure(0, minsize=150)
##        self.midframe.pack(side=TOP, expand=True, fill=BOTH)
        self.botframe = Frame(self.master, bg='yellow')
        self.botframe.grid(column=0, row=2)
        self.botframe.grid_rowconfigure(0, minsize=60)
##        self.botframe.grid_columnconfigure(0, minsize=150)
##        self.botframe.pack(side=TOP, expand=True, fill=BOTH)


        self.frame_1 = Frame(self.topframe, bg=self.colors[0])
        self.frame_1.grid(column=0, row=0)
        self.frame_1.grid_columnconfigure(0, minsize=200)
##        self.frame_1.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame_2 = Frame(self.topframe, bg=self.colors[1])
        self.frame_2.grid(column=1, row=0)
        self.frame_2.grid_columnconfigure(0, minsize=100)

##        self.frame_2.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame_3 = Frame(self.topframe, bg=self.colors[2])
        self.frame_3.grid(column=2, row=0)
        self.frame_3.grid_columnconfigure(0, minsize=100)
##        self.frame_3.pack(side=LEFT, expand=True, fill=BOTH)

        self.frame_4 = Frame(self.midframe, bg=self.colors[4])
        self.frame_4.grid(column=0, row=0)
        self.frame_4.grid_columnconfigure(0, minsize=200)
##        self.frame_4.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame_5 = Frame(self.midframe, bg=self.colors[5])
        self.frame_5.grid(column=1, row=0)
        self.frame_5.grid_columnconfigure(0, minsize=100)
##        self.frame_5.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame_6 = Frame(self.midframe, bg=self.colors[6])
        self.frame_6.grid(column=2, row=0)
        self.frame_6.grid_columnconfigure(0, minsize=100)
##        self.frame_6.pack(side=LEFT, expand=True, fill=BOTH)

        self.frame_7 = Frame(self.botframe, bg=self.colors[7])
        self.frame_7.grid(column=0, row=0)
        self.frame_7.grid_columnconfigure(0, minsize=100)
##        self.frame_7.pack(side=LEFT, expand=True, fill=BOTH)
##        self.rightframe.grid(column=0, row=0, sticky=(N, W, E, S))
##        self.rightframe.columnconfigure(0, weight=1)


##        self.frame_7.grid_columnconfigure(0, weight=1)
        self.frame_8 = Frame(self.botframe, bg=self.colors[0])
        self.frame_8.grid(column=1, row=0)
        self.frame_8.grid_columnconfigure(0, minsize=200)
##        self.columnconfigure(0)
##        self.frame_8.grid_columnconfigure(0, weight=2)
##        self.frame_8.pack(side=LEFT, expand=True, fill=BOTH)


        self.dir_1 = StringVar(self)
        self.dir_2 = StringVar(self)
        self.dir_1.set("No Directory Specified")
        self.dir_2.set("No Directory Specified")
        self.dirs = [self.dir_1, self.dir_2]
        self.synclist = []
##        print self.dirs[0].get()
        self.entry_1 = Label(self.frame_1, textvariable=self.dir_1, width=20, relief=SUNKEN)
        self.entry_1.grid(column=0, row=0)
        self.entry_1.grid_columnconfigure(0, minsize=200)
        self.browse_1 = Button(self.frame_2, text="Browse", command=lambda directory=self.dir_1: self.browse_callback(directory))
##        self.browse_1 = Button(self.frame_2, text="Browse", command=lambda directory: self.browse_callback(directory), self.dir_1)


        self.browse_1.grid(column=0, row=0, ipadx=10, ipady=3)
##        self.syncobj_1 = sync
        self.sync_1 = Button(self.frame_3, text="Sync", command=self.sync_callback)
        self.sync_1.grid(column=0, row=0, ipadx=15, ipady=3)


        self.entry_2 = Label(self.frame_4, textvariable=self.dir_2, width=20, relief=SUNKEN)
        self.entry_2.grid(column=0, row=0)
        self.browse_2 = Button(self.frame_5, text="Browse", command=lambda directory=self.dir_2: self.browse_callback(directory))
        self.browse_2.grid(column=0, row=0, ipadx=10, ipady=3)
##        self.syncobj_2 = sync
        self.sync_2 = Button(self.frame_6, text="Sync", command=self.sync_callback)
        self.sync_2.grid(column=0, row=0, ipadx=15, ipady=3)

        self.checkbox = Checkbutton(self.frame_7, text="Log File")
        self.checkbox.grid(column=0, row=0)
        self.syncopts = Button(self.frame_7, text="Sync Options", command=self.syncopts_callback)
        self.syncopts.grid(column=1, row=0, ipadx=15, ipady=8)
        self.syncopts.grid_columnconfigure(1, minsize=100)
        self.sync_3 = Button(self.frame_8, text="Sync All", command=self.syncall_callback)
        self.sync_3.grid(column=0, row=0, ipadx=30, ipady=8)

    def browse_callback(self, directory):
        mydir = tkFileDialog.askdirectory(parent=self.topframe, initialdir="c:\\",title="Select a directory")
        directory.set(mydir)
        if directory.get()=='':
            directory.set("No Directory Specified")
        self.synclist.append(sync(directory.get()))

    def sync_callback(self):
##        syncobj = sync(directory.get())
##        syncobj.get_list(syncobj.curr, syncobj.curr)
        print self.synclist
        print type(self.synclist)
        for i in range(len(self.synclist)):
            print (self.synclist[i].curr)
            self.synclist[i].get_list(self.synclist[i].curr,self.synclist[i].curr)
            print (self.synclist[i].file_list)
##        return syncobj

    def syncopts_callback(self): # I don't like no arguments being passed.
##        syncobj_1.syncopts(syncobj_2)
##        syncobj_2.syncopts(syncobj_1)
        print "Stuff"
        self.synclist[0].syncopts(self.synclist[1])
        self.synclist[1].syncopts(self.synclist[0])
        print self.synclist[0].file_list
##        print syncobj1.curr

    def syncall_callback(self):
        self.synclist[0].syncup(self.synclist[1])
        self.synclist[1].syncup(self.synclist[0])
##    def browse1_callback(self):
##        mydir = tkFileDialog.askdirectory(parent=None, initialdir="c:\\",title="Select a directory")
##        self.dir_1.set(mydir)
##        print self.dir_1.get()
##
##    def browse2_callback(self):
##        mydir = tkFileDialog.askdirectory(parent=None, initialdir="c:\\",title="Select a directory")
##        self.dir_2.set(mydir)
##        print self.dir_2.get()
##        self.dir_1.set(my_dir)
##        print self.dir_1.get()


    def set_dirs(self, dirvar):
        try:
            dirvar.set(self.my_dir)
        except:
            dirvar.set("No Directory Specified")
        ##        directory.set(self.dir)
##        self.rowframes = ['top', 'mid', 'bot']
##        self.allframes=['topleft', 'topmid', 'topright', 'midleft', 'midmid', 'midright', 'botleft', 'botmid', 'botright']
##        self.entryframes = ['topleft', 'midleft']
##        self.buttonframes = ['topmid', 'topright', 'midmid', 'midright', 'botmid']
##        self.checkbuttonframes = ['botleft']

##        self.weightmatrix = [1, 3, 1, 3, 1, 3]
##        self.create_frames(self.master, self.allframes, self.rowframes, self.colors, self.weightmatrix)
##        self.create_entries(self.all_frames, self.entryframes)
##        self.create_buttons(self.all_frames, self.buttonframes)
##        self.create_checkbuttons(self.all_frames, self.checkbuttonframes)

##        self.entry1 = Entry(self.all_frames['topleft'])
##        self.entry1.grid(row=0, column=0)

##    def create_entries(self, masterframes, framelist):
##        self.entry_frames = {}
##        for i in range(len(framelist)):
##            self.entry_frames[framelist[i]] = Entry(masterframes[framelist[i]])
##            self.entry_frames[framelist[i]].grid(row=0, column=0)
##        return self.entry_frames
##
##    def create_checkbuttons(self, masterframes, framelist):
##        self.check_buttons = {}
##        self.check_buttons[framelist[0]] = Checkbutton(masterframes[framelist[0]], text="Log file")
##        self.check_buttons[framelist[0]].grid(row=0, column=0)
##
##    def create_buttons(self, masterframes, framelist):
##        self.smallbuttons = {}
##        self.mediumbuttons = {}
##        self.largebuttons = {}
##        for i in range(len(framelist)-1):
##            self.smallbuttons[framelist[i]] = Button(masterframes[framelist[i]], text="Browse")
####            self.smallbuttons[framelist[i]].grid(row=0, column=0, sticky=W)
##            self.smallbuttons[framelist[i]].pack(side=LEFT, fill=NONE, expand=False)
##            self.mediumbuttons[framelist[i]] = Button(masterframes[framelist[i]], text="Sync", padx=20, pady=5)
####            self.mediumbuttons[framelist[i]].grid(row=0, column=2, sticky=E)
##            self.mediumbuttons[framelist[i]].pack(fill=X)
##        self.largebuttons[framelist[-1]] = Button(masterframes[framelist[-1]], text="SyncAll", padx=30, pady=10)
####        self.largebuttons[framelist[-1]].grid(row=0, column=0)
##        return self.smallbuttons, self.mediumbuttons, self.largebuttons
##
##        self.leftframe = Frame(master, width=200, height=50, bg='red')
##        self.leftframe.pack(side='left', fill='both', expand=True)
####        self.leftframe.grid(column=0, row=0, sticky=(N, W, E, S))
####        self.leftframe.columnconfigure(0, weight=1)
####        self.leftframe.rowconfigure(0, weight=1)
##        self.rightframe = Frame(master, width=200, height=50, bg='blue')
##        self.rightframe.pack(side='right', fill='both', expand=True)

##    def create_frames(self, masterframe, framelist, rowlist, colorlist, weights):
##        self.all_frames = {}
##        self.all_rows = {}
##        for i in range(len(rowlist)):
##            self.all_rows[rowlist[i]] = Frame(masterframe, width=200, height=50, bg=colorlist[i])
##            self.all_rows[rowlist[i]].pack(side=TOP, fill=BOTH, expand=TRUE)
##            for j in range(3):
##                self.all_frames[framelist[(i*3+j)]] = Frame(self.all_rows[rowlist[i]])
##                self.all_frames[framelist[(i*3+j)]].pack(side=LEFT)
##        return self.all_frames, self.all_rows
'''
    def create_frames(self, masterframe, framelist, colorlist, weights):
        self.all_frames = {}
        for i in range(len(framelist)):
            self.all_frames[framelist[i]] = Frame(masterframe, width=200, height=50, bg=colorlist[i])
        for i in range(3):
            for j in range(2):
##                print (i*2+j)
##                self.all_frames[framelist[(i*2+j)]].grid(row=i, column=j, columnspan=weights[i*2+j])
                self.all_frames[framelist[(i*2+j)]].pack(anchor=NW, side=RIGHT, fill=BOTH, expand=1)
##                self.all_frames[framelist[(i*2+j)]].config(padx=10, pady=10)

##                self.all_frames[framelist[(i*2+j)]].config(height=150)
##                self.all_frames[framelist[(i*2+j)]].grid_columnconfigure(j, weight=weights[i*2+j])
                print weights[i*2+j]

        return self.all_frames
##        self.rightframe.grid(column=0, row=0, sticky=(N, W, E, S))
##        self.rightframe.columnconfigure(0, weight=1)
##        self.rightframe.rowconfigure(0, weight=1)
'''


     # Row 1 - Master Directory Stuff
##        self.grid(column=0, row=0, sticky=(N, W, E, S))
##        self.grid_columnconfigure(0, weight=3, pad=10)
##        #self.grid_rowconfigure(0, weight=3, pad=10, minsize=150)
##        #self.grid_rowconfigure(1, weight=3, minsize=150)
##        self.grid_columnconfigure(1, weight=3, minsize=150)
##        self.grid_columnconfigure(2, weight=3, minsize=150)
        #self.grid_rowconfigure(2, weight=3, minsize=150)

##        self.dir_entry1 = Entry(self.leftframe)
##        self.dir_entry1.grid(row=0, column=1, sticky=E)
##        self.dir_entry1.grid_configure(ipadx=3)
##        newbut = self.buttons(self.rightframe, 5, 'W', 0, 1)

##        self.dir_entry2 = Entry(self.leftframe)
##        self.dir_entry2.grid(row=2, column=1, sticky=E)

##    def buttons(self, root, sizen, stickyn, rown, columnn):
##        new = Button()
##        new.grid(row=rown, column=columnn, sticky=stickyn)

##    def entries(self):


##    for row in range(4):
##        self.grid_rowconfigure(row, minsize=5)
##        for col in range(4):
##            self.grid_columnconfigure(col, minsize=5)

##    self.master.title(title)



##        self.dir_button1 = Button()
##        self.dir_button1.grid(row=1, column=2)


##        self.dir_button2 = Button()
##        self.dir_button2.grid(row=3, column=2)
##        self.dir_button2.grid_configure(ipadx=6)



##
##
##
##
##
###def main():
## #   pass
##
##if __name__ == '__main__':
app = SyncGui("SyncGui")
app.mainloop()

##from Tkinter import *
##
##class Application(Frame):
##    def __init__(self, title, master=None):
##        Frame.__init__(self, master)
##        self.grid()
##        self.master.title(title)
##
##        self.label = Label(self, text='Hello')
##        self.label.grid(row=0, column=0)
##
##app = Application('Sample App')
##app.mainloop()