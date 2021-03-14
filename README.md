# Camel Convert Script

## To use with Git Bash (Or other Linux kernel)

0. Copy the camelConvert.py script to wherever is convenient (hopefully somewhere near your home directory.
	
	- A Helpful note is that your home directory can be found with: 
	
        cd
        # and then typing:
        ls
        # in Linux
	
1. Create a .bashrc in home directory, if one does not yet exist.

        cd # automatically takes you to home directory
        touch .bashrc
        # this file configures certain startup properties of your terminal

3. Add the following to that file (in VI or other editor): 

        alias camel='python {insert absolute path of camelConvert.py script}'
	
	
3. Restart Linux terminal, and try typing in camel to the terminal and pressing enter. Cheers!
