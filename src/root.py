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
'''
import os

class root():
    import os
    def __init__(self, directory):
        self.original_directory = directory
        self.directory = directory
        self.curr = directory
        self.main_list = []
        self.dir_list = []
        self.file_list = []
        
    def get_list(self, directory, curr):
    # notes: this function requires two directory arguments (one as abspath
        files = self.os.listdir(directory)                  # list contents of current dir
       
        for f in files:

            file_with_path = self.os.path.join(directory, f) # append path for recursion
            
            if os.path.isdir(file_with_path):               # if it's a dir:
                
                if directory == self.original_directory: 
                    
                    self.main_list.append(f)
                    self.dir_list.append(f)
                    curr_d = f                              # for the second argument for recursion
                    
                else:
                    curr_d = self.os.path.join(curr, f)
                    self.main_list.append(curr_d)
                    self.dir_list.append(curr_d)
                    
                self.get_list(file_with_path,curr_d)        # recurse

            else:

                if directory == self.original_directory:
                    print ("Directory = my_dir")
                    print ("$$$$$$$$$$$$$")
                    print ("This is a file...")
                    self.main_list.append(f)
                    self.file_list.append(f)
                    print ("Appending ", f)
                else:
                    print ("Directory isn't root!")
                    curr_f = self.os.path.join(curr, f)
                    self.main_list.append(curr_f)
                    self.file_list.append(curr_f)
                    print ("Appending ", curr_f)

        return self.main_list, self.dir_list, self.file_list




