#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY Camera Example</title></head>
<body>
  <h3>SYZYGY Camera Example</h3>

  <ol>
    <li>Make sure the camera is on SYZYGY Port A</li>
    <li><a href="/camera/setup.py">Setup the camera</a></li>
    <li><a href="/camera/single.py">Capture a Single Image</a></li>
  </ol>

</body>
</html>
""")

