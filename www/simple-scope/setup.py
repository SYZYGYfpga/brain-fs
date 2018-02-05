#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


from subprocess import call
call("cat /home/root/brain-fs/adc/syzygy_hub_adc.bit > /dev/xdevcfg", shell=True)


brain.www_print_head("Simple Scope", "")
brain.www_print_title("Simple Scope", "A simple data acquisition app for the POD-ADC-LT226x")

brain.www_start_section()
print("""
  <p>FPGA has been reconfigured with the ADC simple scope configuration.</p>
  <p><a href="/simple-scope/">&larr; Go back to the simple scope index</a></p>
""")
brain.www_end_section()

brain.www_print_foot()

