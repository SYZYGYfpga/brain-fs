#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY HelloWorld!</title></head>
<body>
  <h3>SYZYGY HelloWorld Example</h3>
""")

print("<p>Configuring the FPGA...</p>")
sys.stdout.flush

from subprocess import call
script = "cat /home/root/brain-fs/helloworld/syzygy-helloworld.bit > /dev/xdevcfg";
call(script, shell=True)

print("""
  <p>FPGA has been reconfigured with <tt>helloworld.bit</tt></p>
</body>
</html>
""")

