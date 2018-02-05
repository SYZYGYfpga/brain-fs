#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


brain.www_print_head("Simple Scope", "")
brain.www_print_title("Simple Scope", "A simple data acquisition app for the POD-ADC-LT226x")

brain.www_start_section()
print("""
  <ol>
    <li>Make sure the ADC peripheral is on <strong>SYZYGY Port D</strong></li>
    <li><a href="/simple-scope/setup.py">Configure the simple scope bitfile</a></li>
    <li><a href="/simple-scope/acquire.py">Acquire an input waveform</a></li>
  </ol>
""")
brain.www_end_section()

brain.www_print_foot()

