import pynq
import numpy
import argparse

def waveform_ramp (length, max_value):
	x = numpy.arange(length)
	increment = max_value / length;

	x = x * increment
	return numpy.uint32(numpy.floor(x))

def waveform_sine ( length, max_value ):
	x = numpy.arange(length)
	
	x_scale = 2 * numpy.pi * (1/length)
	y_scale = max_value / 2
	y_adjust = 1.0
	
	y = numpy.floor((numpy.sin(x * x_scale) + y_adjust) * y_scale)
	return numpy.uint32(y)

def compact_data ( array ):
	y = array[0::2] | (array[1::2] << 16)
	return y

parser = argparse.ArgumentParser(description='SYZYGY DAC POD Controller')

parser.add_argument('-c', dest='rate', type=int, help='set the counting rate of the DDS (controls frequency).')
parser.add_argument('-i', dest='iampl', type=int, help='set the amplitude of the I DAC waveform.')
parser.add_argument('-q', dest='qampl', type=int, help='set the amplitude of the Q DAC waveform.')
parser.add_argument('-w', dest='wave', help='set the waveform to either "sine" or "ramp".')
parser.add_argument('-r', dest='reset', action='store_true', help='Reset the design.')

args = parser.parse_args()

bram_handler = pynq.mmio.MMIO(0x41200000, 16384)
gpio_handler = pynq.mmio.MMIO(0x42000000, 16)
reset_handler = pynq.mmio.MMIO(0x40000000, 16)

if (args.reset is True):
	print('Resetting design')
	reset_handler.write(0, 1)
	reset_handler.write(0, 0)

if (args.rate is not None):
	if (args.rate >= 0 and args.rate <= 1023):
		print('setting rate to: ' + str(args.rate))
		gpio_handler.write(0, args.rate)
	else:
		print('rate setting must be between 0 and 1023')

if (args.iampl is not None):
	if (args.iampl >= 0 and args.iampl <= 63):
		print('setting I DAC amplitude to: ' + str(args.iampl))
		current_gpio = gpio_handler.read(8,4)
		current_gpio = (current_gpio & 0xFF00) | (args.iampl & 0x00FF)
		gpio_handler.write(8, current_gpio)
	else:
		print('I Amplitude must be between 0 and 63')

if (args.qampl is not None):
	if (args.qampl >= 0 and args.qampl <= 63):
		print('setting Q DAC amplitude to: ' + str(args.qampl))
		current_gpio = gpio_handler.read(8,4)
		current_gpio = (current_gpio & 0x00FF) | ((args.qampl << 8) & 0xFF00)
		gpio_handler.write(8, current_gpio)
	else:
		print('Q Amplitude must be between 0 and 63')

if (args.wave is not None):
	if (args.wave == 'sine'):
		print('Setting a sine waveform')
		bram_handler.write(0, compact_data(waveform_sine(8192, 4095)).tobytes())
	elif (args.wave == 'ramp'):
		print('Setting a ramp waveform')
		bram_handler.write(0, compact_data(waveform_ramp(8192, 4096)).tobytes())
	else:
		print('Only the "sine" and "ramp" waveforms are supported')
