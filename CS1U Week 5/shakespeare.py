#!/usr/bin/env python

import sys
import os
import subprocess
import re

arguments = sys.argv
if (len(arguments) >= 2):
	word = arguments[1]
	word = '[' + word[0].upper() + word[0].lower() + ']' + word[1:]
	command = subprocess.Popen(['grep', word, 'shakes.txt'], stdout=subprocess.PIPE);
	out = command.stdout.read()
	print(len(re.findall(word, out)))
