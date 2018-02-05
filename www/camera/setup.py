#!/usr/bin/python3

import sys
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


from subprocess import call
call("cat /home/root/brain-fs/camera/syzygy_hub_camera.bit > /dev/xdevcfg", shell=True)
call("/home/root/brain-fs/camera/software/camera_regs.sh", shell=True)


brain.www_print_head("Camera Example", "")
brain.www_print_title("Camera Example", "Image capture example for the POD-CAMERA")

brain.www_start_section()
print("""
  <p>FPGA has been configured with the camera example configuration.</p>
  <p><a href="/camera/">&larr; Go back to the camera example index</a></p>
""")
brain.www_end_section()

brain.www_print_foot()

