#!/usr/bin/python3

import sys
import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from subprocess import call

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


# Capture the image.
# We bring things into a volatile temporary disk for speed.
# Process it with a Bayer filter, then convert to JPG.
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



args = cgi.FieldStorage()
if ("auto" in args):
  brain.www_print_head("Camera Example", '<meta http-equiv="refresh" content="0">')
else:
  brain.www_print_head("Camera Example", "")


brain.www_print_title("Camera Example", "Image capture example for the POD-CAMERA")

brain.www_start_section()
print("""
  <p><a href="/camera/capture.py" class="button button-sm button-secondary">Single Capture</a>
  <a href="/camera/capture.py?auto=1" class="button button-sm button-secondary">Auto Capture (~4 second interval)</a><br />
  <a href="/camera/">&larr; Go back to the camera example index</a></p>
""")
brain.www_end_section()

print('<img src="output.jpg" width="1152" height="648">')

brain.www_print_foot()


