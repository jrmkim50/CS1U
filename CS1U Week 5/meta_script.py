#!/usr/bin/env python
import os
import subprocess

words = ["love", "thee", "to", "eternal"]

for word in words:
	output = word + ": "
	command = subprocess.Popen(['./shakespeare.py', word], stdout=subprocess.PIPE)
	out = command.stdout.read()
	print(output + out)
