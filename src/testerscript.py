import sys
import os
## Check 2.7 and 3.3 compatibility


## List making stuff
'''
def get_paths(directory):

    file_paths = []
    dir_paths = []
    
##    for root, directories, files in os.walk(directory):
##        filenames = [os.path.join(root, filename) for filename in files]
##        with open("C:\JSP\pathlist_files1.txt", 'wb') as newtxt:
##            newtxt.writelines((filetext) + "\n" for filetext in filenames)
##        file_paths.append(filenames)
##To get (full-path) immediate sub-directories in a directory:
##
##def SubDirPath (d):
##    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])
##To get the latest (newest) sub-directory:
##
##def LatestDirectory (d):
##    return max(SubDirPath(d), key=os.path.getmtime)



    allfiles = [os.path.join(root,f) for root,dirs,files in os.walk(directory) for f in files]
    alldirs = [os.path.join(root,d) for root, dirs, files in os.walk(directory) for d in dirs]

##    # alternative for alldirs:
##    import os
##    def get_immediate_subdirectories(dir):
##      return [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]
    
##    with open("C:\JSP\pathlist_files1.txt", 'wb') as txt:
##        txt.writelines((filetext) + "\n" for filetext in allfiles)
##
##    with open("C:\JSP\pathlist_dirs1.txt", 'wb') as txt2:
##        txt2.writelines((dirtext) + "\n" for dirtext in alldirs)
##        txt.write[filenames(i) for i in filenames]
##    newtxt.close()
##    txt2.close()
##    txt.close()

##        dirnames = [os.path.join(root, dirname) for dirname in directories]
##        dir_paths.append(dirnames)

    return file_paths
##    return dir_paths
'''
'''
def get_paths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.
all_files = [] 
for root, directories, files in os.walk(directory):
    filenames = [os.path.join(root, filename) for filename in files]
    all_files.extend(filenames)
'''

##def get_paths(directory):
##    all_dirs = []
##    rvar = [] dvar = [] fvar = []
##    for r, d, f in os.walk(directory):
##        rvar.append



## Recursion stuff
'''def collect_folders(start, depth=-1)
    """ negative depths means unlimited recursion """
    folder_ids = []

    # recursive function that collects all the ids in `acc`
    def recurse(current, depth):
        folder_ids.append(current.id)
        if depth != 0:
            for folder in getChildFolders(current.id):
                # recursive call for each subfolder
                recurse(folder, depth-1)

    recurse(start, depth) # starts the recursion
    return folder_ids'''


main_list = []

##sets = {}
##i = 0
def get_dir_paths(directory):
    # So, this works alright, but doesn't put lists of subfolders inside the list
    # of its main folder (which I want because?? - will this help with
    # comparisons? Other things to do - 1. make yield work; 2. put this in a
    # class.
    # Ignore that, new edits:
    # I need to remove my_dir, so that things are appended as "subf" "subf/file"
    # etc.
    global main_list, my_dir
##    root_dir = os.path.abspath(directory) # do I need this?
    
    files_in_dir = os.listdir(directory)
    print ('################')
    print (files_in_dir)
    print ('################')
    
    for files in files_in_dir:
        if directory == my_dir:
            file_path = files
            print ("It's root!")
            print (file_path)
            print ("End...")
            main_list.append(file_path)
            full_file_path = os.path.join(directory, files)
            print (full_file_path)
            if os.path.isdir(full_file_path):
                print ("Into loop...")
##            for subfiles in get_dir_paths(file_path):
##                yield file_path
                #new_file_path = os.path.split(file_path)[1]
##                main_list.append(new_file_path)
##            yield file_path
                print (file_path)
                print ("Restarting...")
                get_dir_paths(full_file_path)
##          
            
        else:
            file_path = files
            new_file_path = os.path.split(file_path)[1]
            file_path = os.path.join(directory, files)
            print ("It ain't root")
            print (file_path)
            print (new_file_path)

            if os.path.isdir(file_path):
                print ("Into loop...")
##            for subfiles in get_dir_paths(file_path):
##                yield file_path
                main_list.append(file_path)
##            yield file_path
                print (new_file_path)
                print ("Restarting...")
                get_dir_paths(file_path)
##            
##        else:
##            yield file_path
            

    return (main_list)
   
##def get_dir_paths(directory):
##    global main_list
##    main_list = [os.path.join(root, f) for root, dirs, files in os.walk(directory) for f in files]
##    allfiles = [os.path.basename(i) for i in main_list]
##
##    return main_list, allfiles

    

## Run stuff
my_dir = "C:\Schedules & Lists"
##d = get_paths("E:\Movies")
d = get_dir_paths(my_dir)
##for item in get_dir_paths(my_dir):
##    print (item)
