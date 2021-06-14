
"""
Camel Case Conversion for Command Line (Python)
Copyright 2021 Jack Sullivan. All rights reserved.

SETUP: 
1. Source this command in your .bashrc
2. Type camel [./filename] in your command line after restarting bash (or sourcing .bashrc immediately)

"""

import numpy as np
import os
import sys

if sys.argv[1] == "-sing":
    inFile = sys.argv[2]

    inFileSplit = inFile.split(".")

    fileType = inFileSplit[1]

    pieces = inFileSplit[0].split()

    z = []


    for i in range(len(pieces)):
        
        if(i == 0):
            z.append(pieces[i].lower())
        elif (i>0): 
            z.append(pieces[i].capitalize())

    cameled = ''.join(z)

    os.rename(inFile, cameled + "." + fileType)

# In retrospect this is useless to make words concatenated together camel cased; code cannot distinguish.

# elif sys.argv[1] == "-batch":
#     files = os.listdir(".")

#     for j in range(len(files)):
#         # Check if need remove file/folder
#         exp1 = (files[j] == "README.md")
#         # check first character "."
#         exp2 = (files[j][:1] == ".")
#         exp3 = ("_" in files[j])
#         exp4 = ("-" in files[j])
#         combExp = (exp1 or exp2 or exp3 or exp4)
#         if(combExp):
#             files.pop(j)
        

#     for i in range(len(files)):
#         inFileSplit = files[i].split(".")

#         fileType = inFileSplit[1]

#         pieces = inFileSplit[0].split()

#         z = []


#         for a in range(len(pieces)):
#             print(a)
#             if(a == 0):
#                 z.append(pieces[a].lower())
#             elif (a > 0): 
#                 z.append(pieces[a].capitalize())

#         cameled = ''.join(z)

#         os.rename(files[i], cameled + "." + fileType)


    

