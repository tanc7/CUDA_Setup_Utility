#!/usr/bin/env python
# coding=UTF-8
import os
import socket
import operator
import sys

os.system('chmod 777 ./*')
print 'Installing required Python modules'
os.system('pip install termcolor')
os.system('cp -r ./CUDA_setup_utility.py ./CUDAcontroller.py /usr/local/bin')
print 'Setup Complete'
print 'Type "CUDA_setup_utility.py" in Terminal to begin the process'
print 'In the event that your Kali Linux Install breaks, access this utility via the TTY menu to figure out what is wrong'
