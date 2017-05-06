#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable
import os
import sys
import operator
from termcolor import colored

def boost_mode():
    print colored('Warning: Some features may not be available except to Titan Series GPUs, nvidia-smi will tell you which ones you can do','red',attrs=['bold'])
    gpu_clock = str(raw_input("Enter your maximum GPU clock in mhz (e.g. 1124): "))
    mem_clock = str(raw_input("Enter your maximum memory clock in mhz (e.g. 960): "))
    os.system('nvidia-smi -pm 1')
    os.system('nvidia-smi -e 1')
    cmd_String = 'nvidia-smi -ac %s,%s' % (mem_clock,gpu_clock)
    os.system(cmd_String)
    os.system('nvidia-smi --auto-boost-permission=0')
    os.system('nvidia-smi --auto-boost-default=1')
    print colored('[*] Clock set to 1124 mhz GPU, 960 mhz memory','yellow',attrs=['bold'])
    main()
    return

def monitor_systems():
    cmd_String = "gnome-terminal -e 'bash -c \"nvidia-smi dmon; exec bash\"'"
    os.system(cmd_String)
    cmd_String = "gnome-terminal -e 'bash -c \"nvidia-smi stats; exec bash\"'"
    os.system(cmd_String)
    print colored('[*] All monitoring modes enabled','yellow',attrs=['bold'])
    return

def main():
    print colored('MAIN MENU','cyan',attrs=['bold'])
    opt_List = [
        '\n\t#0. Exit Program',
        '#1. Set my video card to full constant-boost mode',
        '#2. Activate all monitoring systems'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))


    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        boost_mode()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        monitor_systems()
        main()
main()
