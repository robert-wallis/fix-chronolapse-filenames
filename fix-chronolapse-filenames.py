#!/usr/bin/python3
"""
fix the screencaps file names from ChronoLapse
that are in this folder so Adobe After Effects understands them

Usage:
    double click it in your screenshots folder
    to update, just run it again, it looks for the largest number

Output:
    renames the files in sequential order from 1

Copyright (C) 2013 Robert Wallis
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer. Redistributions
in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
import re
import math

def main():
    "run from double click / command line"
    path = "./"
    i = find_max(path) + 1
    for filename in os.listdir(path):
        i = rename(path, filename, i)
    pad_digits(path)

def rename(path, filename, i):
    """rename the file sequentially for AE,\
    because it's dumb or chronolapse is dumb"""
    match = re.match(r'(screen_).*\.\d+\.jpg', filename)
    if match:
        new_name = "screen_%d.jpg" % i
        print("renaming " + path + filename + " to " + new_name)
        os.rename(path + filename, new_name)
        i += 1
    return i

def find_max(path):
    "find the highest int in the list"
    i = 0
    for filename in os.listdir(path):
        match = re.match(r'(screen_)(\d+)(\.jpg)', filename)
        if match:
            i = max(i, int(match.groups()[1]))
    return i

def pad_digits(path):
    "prepend 0 to frame numbers so AE doesn't get confused"
    max_i = find_max(path)
    digits = math.floor(math.log(max_i, 10)) + 1
    for filename in os.listdir(path):
        match = re.match(r'(screen_)(\d{1,' + str(digits - 1) +'})(\.jpg)', filename)
        if None == match:
            continue
        number = match.group(2).zfill(digits)
        os.rename(path + filename, path + match.group(1) + number + match.group(3)) 
            
if __name__ == '__main__':
    main()
