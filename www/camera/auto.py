#!/usr/bin/python3

import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from subprocess import call

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY Camera Example!</title></head>
<meta http-equiv="refresh" content="0">
<body>
  <h3>SYZYGY Camera Example</h3>
  <a href="/camera/single.py">Capture a Single Image</a><br /><br />
  <a href="/camera/auto.py">Autorefresh Capture (~4 second intervals)</a><br /><br />
""")


cwd = os.getcwd()
try:
  os.stat("/tmp/camera")
except:
  os.mkdir("/tmp/camera")

os.chdir("/tmp/camera")
call("/home/root/brain-fs/camera/software/capture_single >/dev/null", shell=True)
call("/usr/bin/bayer2rgb -i capture.bin -o output.tiff -w 2304 -v 1296 -b 8 -f GRBG -m NEAREST -t", shell=True)
call("/usr/bin/convert -quality 85% output.tiff output.jpg 2>/dev/null", shell=True)


try:
  os.stat(cwd + "/output.jpg")
except:
  os.symlink("/tmp/camera/output.jpg", cwd + "/output.jpg")

print("""
  <img src="output.jpg" width="1152" height="648">
</body>
</html>
""")

