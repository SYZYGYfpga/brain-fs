#!/usr/bin/python3

import os
import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from subprocess import call

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


brain.www_print_head("Simple Scope", "")
brain.www_print_title("Simple Scope", "A simple data acquisition app for the POD-ADC-LT226x")

cwd = os.getcwd()
try:
    os.stat("/tmp/simple-scope")
except:
    os.mkdir("/tmp/simple-scope")

os.chdir("/tmp/simple-scope")

call("/home/root/brain-fs/adc/software/capture_single >/dev/null", shell=True)
call("/usr/bin/gnuplot /home/root/brain-fs/www/simple-scope/plot_capture.gp", shell=True)


try:
    os.stat(cwd + "/output.png")
except:
    os.symlink("/tmp/simple-scope/output.png", cwd + "/output.png")

brain.www_start_section()
print("""
  <a href="/simple-scope/acquire.py" class="button button-sm button-secondary">Acquire</a><br />
  <a href="/simple-scope/">&larr; Go back to the simple scope index</a>
  <img src="output.png" width="1000">
""")
brain.www_end_section()

brain.www_print_foot()

