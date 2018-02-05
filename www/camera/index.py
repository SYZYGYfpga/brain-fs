#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


brain.www_print_head("Camera Example", "")
brain.www_print_title("Camera Example", "Image capture example for the POD-CAMERA")

brain.www_start_section()
print("""
  <ol>
    <li>Make sure the camera peripheral is on <strong>SYZYGY Port A</strong></li>
    <li><a href="/camera/setup.py">Configure the camera example bitfile</a></li>
    <li><a href="/camera/capture.py">Capture an image</a></li>
  </ol>
""")
brain.www_end_section()

brain.www_print_foot()

