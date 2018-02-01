#!/usr/bin/python3

import sys
import pynq
import numpy
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY DAC Waveform Generator Example</title></head>
<body>
  <h3>SYZYGY DAC Waveform Generator Example</h3>
""")

print("<p>Configuring the FPGA...</p>")
sys.stdout.flush

from subprocess import call
call("cat /home/root/brain-fs/dac/syzygy_hub_dac.bit > /dev/xdevcfg", shell=True)

reset_handler = pynq.mmio.MMIO(0x40000000, 16)
reset_handler.write(0, 1)
reset_handler.write(0, 0)

print("""
  <p>FPGA has been reconfigured with the DAC waveform generator configuration.</p>
</body>
</html>
""")

