#!/usr/bin/python3

import sys
import subprocess
import cgi
import cgitb; cgitb.enable();
import json

sys.path.insert(0, '/home/root/brain-fs/www/common')
import brain


# Query SmartVIO peripherals
from subprocess import call
try:
  svio = subprocess.check_output("/usr/bin/smartvio -j /dev/i2c-1", shell=True)
except subprocess.CalledProcessError as e:
  print(e.output)
print(svio.decode('utf-8'))
svioj = json.loads(svio.decode('utf-8'))
svio_ports = svioj["port"]
svio_vio = svioj["vio"]



brain.www_print_head("SYZYGY Status", "")
brain.www_print_title("SYZYGY Status", "Shows system SYZYGY peripheral information.")

brain.www_start_section()


print("""
        <div class="container text-content">
          <div class="row">
            <div class="col-sm-12 mb-md">
              <div class="col-sm-12 table-responsive">
              <table class="table table-datatable">
                <thead>
                  <tr>
                    <th>Parameter</th>
                    <th>Port A</th>
                    <th>Port B</th>
                    <th>Port C</th>
                    <th>Port D</th>
                  </tr>
""")
titles = ["Manufacturer", "Product", "Model", "Version", "Serial Number"]
match = ["manufacturer", "product_name", "product_model", "product_version", "serial_number"]
for i in range(0,5):
  print("<tr>")
  print("<th>" + titles[i] + "</th>")
  for j in range(0,4):
    if svio_ports[j] is not None:
      print("<td>" + svio_ports[j][match[i]] + "</td>")
    else:
      print("<td>-</td>")
  print("</tr>")

print("<tr>")
print("<th>SmartVIO</th>")
if svio_vio[0] == 0:
  print('<td colspan="1">Disabled</td>')
else:
  print('<td colspan="1">' + ("%.1f" % (svio_vio[0] / 100)) + '</td>')

if svio_vio[1] == 0:
  print('<td colspan="3" style="text-align:center;">Disabled</td>')
else:
  print('<td colspan="3" style="text-align:center;">' + ("%.1f" % (svio_vio[0] / 100)) + '</td>')

print("</tr>")

print("""
                </tbody>
              </table>
              </div>
            </div>
          </div>
        </div>
""")


brain.www_end_section()

brain.www_print_foot()
