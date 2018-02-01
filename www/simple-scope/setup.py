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
""")

print("<p>Configuring the FPGA...</p>")
sys.stdout.flush

from subprocess import call
call("cat /home/root/brain-fs/adc/syzygy_hub_adc.bit > /dev/xdevcfg", shell=True)

print("""
  <p>FPGA has been reconfigured with the ADC simple scope configuration.</p>
</body>
</html>
""")

