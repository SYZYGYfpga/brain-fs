#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable();

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


# Configure the FPGA
from subprocess import call
call("cat /home/root/brain-fs/helloworld/syzygy-helloworld.bit >/dev/xdevcfg", shell=True)


brain.www_print_head("Hello World", "")
brain.www_print_title("Hello World", "A simple starter application to motivate you.")

brain.www_start_section()
print("""
Each time you reload this page, the FPGA will be reconfigured with the hello world bitfile.
""")
brain.www_end_section()

brain.www_print_foot()

