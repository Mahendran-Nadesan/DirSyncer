# This will recursively look through the directories, and make a list WITHOUT
# the original root directory (i.e. Root\folder -> folder;
# root\folder\file -> folder\file)

import os
import ntpath


def get_full_paths(directory, curr):

    main_list = []
    dir_list = []
    file_list = []

    def get_list(directory, curr):
##        global main_list # So that list isn't reset when it recurses.
        
        files = os.listdir(directory)
        print ("##################")
        print (files)
        print ("##################")

        for f in files:
            print ("This is the file with a path")
            file_with_path = os.path.join(directory, f)
            print (file_with_path)
            print ("This is a file or dir")
            print f

            if os.path.isdir(file_with_path):
                print ("%%%%%%%%%%%")
                print ("This is a dir...")
                
                if directory==my_dir:
                    print ("Directory = my_dir")
                    main_list.append(f)
                    dir_list.append(f)
                    print ("Appending ", f)
                    print ("---------------------")
                    curr_d = f
                else:
                    print ("Directory isn't root!")
                    curr_d = os.path.join(curr, f)
                    main_list.append(curr_d)
                    dir_list.append(curr_d)
                    print ("Appending ", curr_d)

                print ("Restarting!")
                get_list(file_with_path,curr_d)

            else:

                if directory==my_dir:
                    print ("Directory = my_dir")
                    print ("$$$$$$$$$$$$$")
                    print ("This is a file...")
                    main_list.append(f)
                    file_list.append(f)
                    print ("Appending ", f)
                else:
                    print ("Directory isn't root!")
                    curr_f = os.path.join(curr, f)
                    main_list.append(curr_f)
                    file_list.append(curr_f)
                    print ("Appending ", curr_f)

        return main_list, dir_list, file_list

    
    get_list(directory, curr)
    return main_list, dir_list, file_list


my_dir = "C:\Schedules & Lists"
main_list, dir_list, file_list = get_full_paths(my_dir, my_dir)
