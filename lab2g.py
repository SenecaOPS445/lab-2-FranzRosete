#!/usr/bin/env python3

##Author: Franz Rosete
##AuthorID: Frosete 157712183
##Date Created: 2025-01-24

import sys
if len(sys.argv) != 2:
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!') 
    sys.exit()

    
if int(sys.argv[1]):
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1
    print('blast off!') 







   
