# Obsolete code
# This will store obselete functions, just in case I want to use them again.


##def get_fullfilepaths(directory):
##
##    allfiles = []    
##    allfiles = [os.path.join(root,f) for root,dirs,files in os.walk(directory) for f in files if root != directory]
##    allfiles = [os.path.join(root, f) for root, dirs, files in os.walk(directory) for f in files]
##
##    for root, dirs, files in os.walk(directory):
##        if root == directory:
##            x1 = [f for f in files]
##            allfiles.append(x1)
##        elif root != directory:
##            x1 = [os.path.join(, f) for f in files]
##            allfiles.extend(x1)
##
##    return allfiles
##


##def get_fulldirpaths(directory):
##
##    alldirs = [os.path.join(root, d) for root, dirs, files in os.walk(directory) for d in dirs]
##
##    return alldirs
##
##def clean_files(a_list):
##
##    new_list = []
##    split = [os.path.split(i) for i in a_list]
####    for i in range(len(split)):
####        new_list.append(split[i][1])
##
##    [new_list.append(split[i][1]) for i in range(len(split))]
##
##    return new_list
##
##def clean_folders(a_list, directory):
##
##    return [i.lstrip(directory) for i in a_list]



