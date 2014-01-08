# Proposed class for files
'''
Written 11/11/2013
    - __init__, .get_list

Modified 13/11/2013:

    - removed print statements

To do:

    - Perhaps use abspath so that .getlist only needs one argument
    - Change class to "sync"
    - Add method ".syncto(x)" where x is a sync object
    - Add checks - for lists, for dirlists
    - Add method to print info when instance of class is called
'''
import os
import shutil

class sync(object):

    def __init__(self, directory):
##        import os
        self.original_directory = directory
        self.directory = directory
        self.curr = directory
        self.main_list = []
        self.dir_list = []
        self.file_list = []

    def get_list(self, directory, curr):
##        import os
    # notes: this function requires two directory arguments (one as abspath, one as current dir in loop)
        files = os.listdir(directory)                  # list contents of current dir

        for f in files:

            file_with_path = os.path.join(directory, f) # append path for recursion

            if os.path.isdir(file_with_path):               # if it's a dir:

                if directory == self.original_directory:    # if the root dir is the initial argument to the class

                    self.main_list.append(f)
                    self.dir_list.append(f)
                    curr_d = f                              # for the second argument for recursion

                else:

                    curr_d = os.path.join(curr, f)
                    self.main_list.append(curr_d)
                    self.dir_list.append(curr_d)

                self.get_list(file_with_path,curr_d)        # recurse

            else:                                           # if it's just a file

                if directory == self.original_directory:    # if the root dir is the initial argument for the class

                    self.main_list.append(f)
                    self.file_list.append(f)

                else:

                    curr_f = os.path.join(curr, f)
                    self.main_list.append(curr_f)
                    self.file_list.append(curr_f)

        return self.main_list, self.dir_list, self.file_list

    def syncopts(self, syncobj): # for now, takes a sync object (i.e.: x = sync(dir), y = sync(dir2), x.syncopts(y)
        # check if arg is sync obj; make unique and date.mod lists; copy
        self.unique_dirs = [f for f in self.dir_list if f not in syncobj.dir_list]          # makes a relative path list of unique dirs for dir_a
        self.unique_files = [f for f in self.file_list if f not in syncobj.file_list]       # makes a relative path list of unique files for dir_a
        self.shared_files = [os.path.join(self.directory, i) for i in (f for f in self.file_list if f in syncobj.file_list)]        # makes an absolute path list of shared files for dir_a
        syncobj.shared_files = [os.path.join(syncobj.directory, i) for i in (f for f in syncobj.file_list if f in self.file_list)]  # makes an absolute path list of shared files for dir_b

        # two options: make a list with mod dates, then subtract them (so that list can be >>>), or do it in one step.
        # option 2 follows.

        self.mod_dates = [os.path.getmtime(i) - os.path.getmtime(j) for i, j in zip(self.shared_files, syncobj.shared_files)] # if t1 - t2 > 0, it's newer

        return self.unique_dirs, self.unique_files, self.shared_files, syncobj.shared_files, self.mod_dates

    def syncup(self, syncobj):

        for j in self.mod_dates:

            if j > 0:

                shutil.copy2(self.shared_files[self.mod_dates.index(j)], syncobj.shared_files[self.mod_dates.index(j)]) # copy most recent versions of shared files

        [os.makedirs(os.path.join(syncobj.original_directory, i)) for i in self.unique_dirs]                            # copy unique directories
        [shutil.copy2(os.path.join(self.original_directory, i), os.path.join(syncobj.original_directory, i)) for i in self.unique_files]                           # copy unique files



##        [os.makedirs(i, 0755) for i in (os.path.join(syncobj.original_directory, f) for f in self.shared_files if (j > 0 for j in self.mod_dates))]






