#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY ADC Simple Scope Example</title></head>
<body>
  <h3>SYZYGY ADC Simple Scope Example</h3>

  <ol>
    <li>Make sure the ADC peripheral is on <strong>SYZYGY Port D</strong></li>
    <li><a href="/simple-scope/setup.py">Setup the simple scope</a></li>
    <li><a href="/simple-scope/get-waveform.py">Capture an input waveform</a></li>
  </ol>

</body>
</html>
""")

