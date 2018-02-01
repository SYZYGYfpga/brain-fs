#!/usr/bin/python3

import os
import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from subprocess import call


print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY ADC Simple Scope Example</title></head>
<body>
  <h3>SYZYGY ADC Simple Scope Example</h3>
""")

cwd = os.getcwd()
try:
    os.stat("/tmp/simple-scope")
except:
    os.mkdir("/tmp/simple-scope")

os.chdir("/tmp/simple-scope")

print("<p>Capturing waveform...</p>")
call("/home/root/brain-fs/adc/software/capture_single >/dev/null", shell=True)
call("/usr/bin/gnuplot /home/root/brain-fs/www/simple-scope/plot_capture.gp", shell=True)


try:
    os.stat(cwd + "/output.png")
except:
    os.symlink("/tmp/simple-scope/output.png", cwd + "/output.png")

print("""
  <img src="output.png" width="1000">
</body>
</html>
""")

