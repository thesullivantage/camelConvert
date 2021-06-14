# Camel Convert Script

#### To use with Git Bash (Or other Linux kernel) (__*Must have Python Installed*__)

1. Copy the camelConvert.py script to wherever is convenient (hopefully somewhere near your home directory.
	
2. Create a .bashrc in home directory, if one does not yet exist.

```
cd # automatically takes you to home directory
touch .bashrc
# this file configures certain startup properties of your terminal
```

3. Add the following to that file (in VI or other editor): 

```
alias camel='python {insert absolute path of camelConvert.py script}'
```

4. Type:

```shell
camel -sing [./filename] 
```
in your command line after restarting bash (or sourcing .bashrc immediately)

5. Enjoy your filenames without spaces! Cheers!

--- 

See batch mode feature (commented out)
