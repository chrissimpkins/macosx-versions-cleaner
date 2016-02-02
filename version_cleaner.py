#!/usr/bin/env python


# ------------------------------------------
#
# Mac OSX Versions Cleaner
# version_cleaner.py
# Copyright 2016 Christopher Simpkins
# MIT License
#
# ------------------------------------------

import os
import sys
import subprocess
import shutil


def execute(command):
    try:
        response = subprocess.call(command, shell=True)
        if response == 0:
            return True
        else:
            return False
    except subprocess.CalledProcessError as cpe:
        try:
            sys.stderr.write(cpe.output)
        except TypeError:
            sys.stderr.write(str(cpe.output))

versions_dir = "/.DocumentRevisions-V100"

if os.path.isdir(versions_dir):
    print("Versions directory size before cleaning:")
    execute_command = "du -sh " + versions_dir
    execute(execute_command)
    print(" ")

    try:
        shutil.rmtree(versions_dir)
    except Exception as e:
        print("Error in the attempt to remove the files. Error message: " + str(e))
        sys.exit(1)

    if not os.path.isdir(versions_dir):
        print("The versions directory was deleted.")

        if sys.version_info[0] == 2:
            user_response = raw_input("Reboot to complete cleanup? (y/n): ")
        else:
            user_response = input("Reboot to complete cleanup? (y/n): ")

        if user_response.lower() == "y":
            print("Rebooting...")
            execute("reboot")
        else:
            print("Skipping system reboot.  Please reboot your system manually to begin using document versioning again.")
else:
    print("Unable to locate a versions directory at the path '" + versions_dir + "'. It appears that it was already cleaned.")
    print("Complete the cleanup process by rebooting your system.")
