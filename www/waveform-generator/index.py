#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY DAC Waveform Generator Example</title></head>
<body>
  <h3>SYZYGY DAC Waveform Generator Example</h3>

  <ol>
    <li>Make sure the DAC peripheral is on <strong>SYZYGY Port A</strong></li>
    <li><a href="/waveform-generator/setup.py">Setup the waveform generator</a></li>
    <li><a href="/waveform-generator/set-waveform.py">Set the output waveform</a></li>
  </ol>

</body>
</html>
""")

