#!/usr/bin/python

# #################################################### #
# ##                   Report generator             ## #
# #################################################### #
# ##               Reads file_diff.txt              ## #
# ##                Creates two files               ## #
# ##              added.txt & removed.txt           ## #
# #################################################### #

import os
import sys
import shutil

FILE_TO_READ = "file_diff.txt"
FILE_ADDED = "added.txt"
FILE_REMOVED = "removed.txt"


def check_files_exist(f, a, r):
    # Check the file_diff.txt exists - if not, exit
    if os.path.exists(f) == 0:
        print("File file_diff.txt not found - exiting.")
        sys.exit(0)
    # Check if file_added.txt exists - if it does confirm overwrite
    if os.path.exists(a) == 1:
        print("File added.txt already exists; do you wish to overwrite?(y/n)")
        ans = input()
        if ans == "n":
            sys.exit(0)
    # Check if removed.txt exists - if it does confirm overwrite
    if os.path.exists(r) == 1:
        print("File removed.txt already exists; do you wish to overwrite?(y/n)")
        ans = input()
        if ans == "n":
            sys.exit(0)
    # Check if the output directories exist. If not, create them. 
    if os.path.exists("deployPackage") == 0:
        os.mkdir("deployPackage")
    if os.path.exists("deployPackage/added") == 0:
        os.mkdir("deployPackage/added")
    if os.path.exists("deployPackage/removed") == 0:
        os.mkdir("deployPackage/removed")


def read_files(f, a, r):
    # Open the files, and read the first character
    FILE_TO_READ = open(f, "r")
    FILE_ADDED = open(a, "w")
    FILE_REMOVED = open(r, "w")
    for line in FILE_TO_READ:
        element = line.split()
        if element[0] == "M" or element[0] == "A":
            # Split the directory from the filename
            (directory, filename) = list(os.path.split(element[1]))
            # Write just the filename to the FILE_ADDED file.
            FILE_ADDED.write(filename + "\n")
            # Move the file to deployPackage/added
            shutil.copy(os.path.join(directory, filename),
                        "deployPackage/added/" + filename)
        elif element[0] == "R" or element[0] == "D":
            (directory, filename) = list(os.path.split(element[1]))
            FILE_REMOVED.write(filename + "\n")
            # Move the file to deployPackage/removed
            shutil.copy(os.path.join(directory, filename),
                        "deployPackage/removed/" + filename)

    FILE_REMOVED.close()
    FILE_ADDED.close()
    FILE_TO_READ.close()


def main():
    check_files_exist(FILE_TO_READ, FILE_ADDED, FILE_REMOVED)
    read_files(FILE_TO_READ, FILE_ADDED, FILE_REMOVED)


if __name__ == '__main__':
    main()
