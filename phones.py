#!/usr/bin/env python3

# This is a dumb little 5 minute script that performs basic searches of a CSV
# export from Mitel Connect Director. This should probably be a Go program, so 
# my poor coworkers can use it.

import csv
import re
import sys


def usage():
    print("Enter an argument.")

# Assumes valid input
def clean(unclean):
    return re.sub(r'\W+', '', unclean)


if __name__ == "__main__":
    st = ""

    # If it starts with zero, assume it's a MAC address.
    if sys.argv[1].startswith("0"):
        st = clean(sys.argv[1]).upper()
    else:
        st = sys.argv[1]

    with open('export.csv') as f:
        for line in f:
            if st in line:
                f = line.split(',')
                print(f"Extension: {f[0]}")
                print(f"Person: {f[3]}")
                print(f"DID Override: {f[7]}")
                print(f"DID: {f[30]}")
                print(f"Site: {f[9]}")
                print(f"Phone MAC: {f[33]}")
                print("---")
                #print(f"DEBUG: {line}")
