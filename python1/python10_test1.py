#!/usr/bin/env python3

#Exercise 7: Create a script that runs a command with subprocess.run

import subprocess

subprocess.run('ls -l', shell=True)
if subprocess.check_output('ls -l', shell=True):
    print('ok')
