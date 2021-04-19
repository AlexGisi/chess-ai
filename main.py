import getopt
import sys
from driver import *
if __name__ == "__main__": 
    argList = sys.argv[1:]
    short_options = "p:"
    long_options = ["Play_Mode="]
    try:
        args, vals = getopt.getopt(argList, short_options, long_options)
        for arg, val in args:
            if arg in ("-p", "--Play_Mode"):
                drv = Driver(play_mode=str(val))
                drv.run_game()
            else:
                print("Argument: ", str(arg), " not recognized. Exiting...")
    except getopt.error as err:
        print (str(err))
    if len(argList) == 0:
        pm = str(input("Input play mode(PvP, PvAI, AIvP, AIvAI): "))
        drv = Driver(play_mode=pm)
        drv.run_game()