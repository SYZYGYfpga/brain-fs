#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


brain.www_print_head("Waveform Generator", "")
brain.www_print_title("Waveform Generator", "A simple waveform generator for the POD-DAC-AD9116")

brain.www_start_section()
print("""
  <ol>
    <li>Make sure the DAC peripheral is on <strong>SYZYGY Port A</strong></li>
    <li><a href="/waveform-generator/setup.py">Configure the waveform generator bitfile</a></li>
    <li><a href="/waveform-generator/set-waveform.py">Set the output waveform</a></li>
  </ol>
""")
brain.www_end_section()

brain.www_print_foot()

