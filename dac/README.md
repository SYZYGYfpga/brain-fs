# Syzygy Hub DAC Sample

## Overview

This sample project is designed to demonstrate usage of the POD-DAC-AD911X
SYZYGY module from Opal Kelly. This sample is designed to interface with the
pod connected to PORT A on the Brain-1.

The Q output of the DAC will output a continuous triangle wave at a frequency 
of approximately 15 kHz. The I output of the DAC can be configured to output 
an arbitrary waveform by programming its waveform memory from the PS of the 
Zynq through the software found in the software directory.

## Software

Software for the Zynq PS portion of the design is included in the software
directory. The software allows for configuration of the PL portion of the DAC
design. Available configuration includes writing a waveform to block RAM for
the I channel, setting the counting rate (frequency) of the I channel, and
control over the I and Q channel amplitudes through the FSADJ register on the
DAC.

Both C and Python examples are provided, both programs share the same features.
The Python sample is designed for Python 3.5 and requires the pynq library from
Xilinx, available on [github](https://github.com/Xilinx/PYNQ/tree/master/pynq).

The C example can be built with:

`gcc -o dac_set -lm dac_set.c`
