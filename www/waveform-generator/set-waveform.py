#!/usr/bin/python3

import sys
import pynq
import numpy
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

def waveform_ramp (length, max_value):
    x = numpy.arange(length)
    increment = max_value / length
    x = x * increment
    return numpy.uint32(numpy.floor(x))

def waveform_sine (length, max_value):
    x = numpy.arange(length)
    x_scale = 2 * numpy.pi * (1/length)
    y_scale = max_value / 2
    y_adjust = 1.0
    y = numpy.floor((numpy.sin(x * x_scale) + y_adjust) * y_scale)
    return numpy.uint32(y)

def compact_data(array):
    y = array[0::2] | (array[1::2] << 16)
    return y

def gpio_update(addr, mask, value):
    current_gpio = gpio_handler.read(addr, 4)
    current_gpio = (current_gpio & ~mask) | (value & mask)
    gpio_handler.write(addr, current_gpio)

print("Content-type: text/html")
print

print("""
<html>
<head><title>SYZYGY DAC Waveform Generator Example</title></head>
<body>
  <h3>SYZYGY DAC Waveform Generator Example</h3>
""")

print("<p>Setting waveform...</p>")
sys.stdout.flush

bram_handler = pynq.mmio.MMIO(0x41200000, 16384)
gpio_handler = pynq.mmio.MMIO(0x42000000, 16)

# Write the rate (0..1023)
gpio_handler.write(0, 2)

# Write the I DAC amplitude (0..63)
gpio_update(8, 0x00ff, 35)

# Write the Q DAC amplitude (0..63)
gpio_update(8, 0xff00, 35<<8)

# Write out a sine wave
bram_handler.write(0, compact_data(waveform_sine(8192, 4095)).tobytes())
#bram_handler.write(0, compact_data(waveform_ramp(8192, 4095)).tobytes())


print("""
  <p>Waveform updated.</p>
</body>
</html>
""")

