import os

execution_mode = raw_input("Which mode you want to execute coffee machine simulator in? Type \'1\' if asci art mode, \'2\' if debug mode: ")
if execution_mode == "1":
    os.system("python ExecutionAscii.py")
if execution_mode == "2":
    os.system("python ExecutionDebug.py")
else:
    print "Exit"
