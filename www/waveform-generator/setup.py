#!/usr/bin/python3

import sys
import pynq
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


from subprocess import call
call("cat /home/root/brain-fs/dac/syzygy_hub_dac.bit > /dev/xdevcfg", shell=True)
reset_handler = pynq.mmio.MMIO(0x40000000, 16)
reset_handler.write(0, 1)
reset_handler.write(0, 0)


brain.www_print_head("Waveform Generator", "")
brain.www_print_title("Waveform Generator", "A simple waveform generator for the POD-DAC-AD9116")

brain.www_start_section()
print("""
  <p>FPGA has been reconfigured with the DAC waveform generator configuration.</p>
  <p><a href="/waveform-generator/">&larr; Go back to the waveform generator index</a></p>
""")
brain.www_end_section()

brain.www_print_foot()

