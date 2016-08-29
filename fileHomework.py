#!/usr/bin/env python

# File homeworks and copy back grades.
# Copyright 2015 Alex Reinhart
# Unauthorized use punishable by 24 consecutive hours of
# Barry Manilow Christmas music at 110 dB.

import glob, subprocess, re, argparse

HW_DIR = "/Users/alexreinhart/Dropbox/s650/"
DEST_DIR = "/Users/alexreinhart/Dropbox/s650/hw/"

def file_homework(hwnum, dry):
    dest = DEST_DIR + hwnum

    dirs = glob.glob(HW_DIR + "s650-*/" + hwnum)

    print "Found {} assignments".format(len(dirs))

    for d in dirs:
        name = re.search("s650-([a-z]+)/", d).group(1)
        print "Copying {} for {}".format(hwnum, name)
    
        print d, dest + "/" + name
        if not dry:
            subprocess.call(["cp", "-R", d, dest + "/" + name])

def file_grades(hwnum, dry):
    dirs = glob.glob(DEST_DIR + hwnum + "/*/GRADE.txt")

    print "Found {} assignments".format(len(dirs))

    for d in dirs:
        name = d.split("/")[-2]
        print "Copying {} for {}".format(hwnum, name)

        dest = HW_DIR + "s650-{}/".format(name) + hwnum
        print d, dest
        if not dry:
            subprocess.call(["cp", d, dest])

if __name__ == "__main__":
    p = argparse.ArgumentParser(description='File homeworks and copy grades.')
    p.add_argument("command",
                    help="'file' to file homework, 'grade' to file grades.")
    p.add_argument("number", type=str,
                    help="Homework to file, e.g. HW_1")
    p.add_argument("--dry", action="store_true",
                   help="Dry run: show files but don't copy.")
    
    args = p.parse_args()

    if args.command == "file":
        file_homework(args.number, args.dry)
    elif args.command == "grade":
        file_grades(args.number, args.dry)
    
