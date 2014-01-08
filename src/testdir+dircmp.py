# This will run the main functions for:
#
# 1. Making lists of the directories - this is now in class "sync"
#     f1 = sync("C:\blah"), f1.get_list(f1.directory, f1.curr) etc.
# 2. Making lists of directories shared
# 3. Making lists of files shared
# 4. Comparing the lists for missing files/directories (i.e. not UPDATED files)
#
# To do:
#
# 1. Write checks for lists in beginning of functions (or classes)
# 2. Check modification dates on shared files/folders*
# 3. Check for uniques and shared stuff in class "sync"
#       (sync.files, sync.dirs, sync.copy ?)
# 4. Solve the general problem of uniques in subfolders (??)
# 5. Solve the import issue (see http://stackoverflow.com/questions/4142151/python-how-to-import-the-class-within-the-same-directory-or-sub-directory)
#
# Long term to do:
#
# 1. Current implementation is: all analysis -> copy
#       Could this become a loop of list > copy?
# 2. Can current unique file/dir be solved in one function, as a dict?
#

import os
import ntpath
import sync
from sync import sync

f1_main = []
f2_main = []

f1_name = "C:\Test1"
f2_name = "C:\Test2"


##def get_full_paths(directory, curr):
##
##    main_list = []
##    dir_list = []
##    file_list = []
##    my_dir = directory
##
##    def get_list(directory, curr):
####        global main_list # So that list isn't reset when it recurses.
##
##        files = os.listdir(directory)
##        print ("##################")
##        print (files)
##        print ("##################")
##
##        for f in files:
##            print ("This is the file with a path")
##            file_with_path = os.path.join(directory, f)
##            print (file_with_path)
##            print ("This is a file or dir")
##            print f
##
##            if os.path.isdir(file_with_path):
##                print ("%%%%%%%%%%%")
##                print ("This is a dir...")
##
##                if directory==my_dir:
##                    print ("Directory = my_dir")
##                    main_list.append(f)
##                    dir_list.append(f)
##                    print ("Appending ", f)
##                    print ("---------------------")
##                    curr_d = f
##                else:
##                    print ("Directory isn't sync!")
##                    curr_d = os.path.join(curr, f)
##                    main_list.append(curr_d)
##                    dir_list.append(curr_d)
##                    print ("Appending ", curr_d)
##
##                print ("Restarting!")
##                get_list(file_with_path,curr_d)
##
##            else:
##
##                if directory==my_dir:
##                    print ("Directory = my_dir")
##                    print ("$$$$$$$$$$$$$")
##                    print ("This is a file...")
##                    main_list.append(f)
##                    file_list.append(f)
##                    print ("Appending ", f)
##                else:
##                    print ("Directory isn't sync!")
##                    curr_f = os.path.join(curr, f)
##                    main_list.append(curr_f)
##                    file_list.append(curr_f)
##                    print ("Appending ", curr_f)
##
##        return main_list, dir_list, file_list
##
##
##    get_list(directory, curr)
##    return main_list, dir_list, file_list

def compare_folders(list_a, list_b):

    unique_dir_a = [f for f in list_a if f not in list_b]
    unique_dir_b = [f for f in list_b if f not in list_a]
    shared_dirs = [f for f in list_a if f in list_b]

    return (unique_dir_a, unique_dir_b, shared_dirs)

def compare_files(list_a, list_b):

    unique_files_a = [f for f in list_a if f not in list_b]
    unique_files_b = [f for f in list_b if f not in list_a]
    shared_files = [f for f in list_a if f in list_b]

    return (unique_files_a, unique_files_b, shared_files)

##def shared_update(shared_files):
##
##    shared_f1 = [os.path.join(f1_name, f) for f in shared_files]



from sync import sync


## Test ##
# Make lists
##f1_list, f1_dir_list, f1_file_list = get_full_paths(f1_name, f1_name)
##f2_list, f2_dir_list, f2_file_list = get_full_paths(f2_name, f2_name)
##d1_list = get_fulldirpaths(f1_name)
##d2_list = get_fulldirpaths(f2_name)
f1 = sync(f1_name)
f1.get_list(f1.curr, f1.curr)
f2 = sync(f2_name)
f2.get_list(f2.curr, f2.curr)
##
##
##
####
##### ??
##newf1_list = clean_files(f1_list)
##newf2_list = clean_files(f2_list)
##newd1_list = clean_folders(d1_list, f1_name)
##newd2_list = clean_folders(d2_list, f2_name)
##
### Make lists of shared and unique folders and files
##
##unique_f1, unique_f2, shared_files = compare_files(f1.file_list, f2.file_list)
##unique_d1, unique_d2, shared_dirs = compare_folders(f1.dir_list, f2.dir_list)
f1.syncopts(f2)
f2.syncopts(f1)

print (f1.shared_files)
print (f1.unique_files)
print (f2.unique_files)
f1.syncup(f2)
f2.syncup(f1)
