# Syzygy Brain 1 ADC Sample

## Overview

This sample project is designed to demonstrate usage of the POD-ADC-LTC2264-12
SYZYGY module from Opal Kelly. This sample is designed to interface with the
pod connected to PORT D on the Brain-1.

Both analog inputs on the ADC are deserialized by logic in the PL portion
of the Zynq and fed into PS memory by a DMA transfer.

This project is based heavily on Xilinx Application Note 524 (XAPP524) and
implements a simplified version of the design described by Xilinx.

## Software

Software for the Zynq PS portion of the design is included in the software
directory. This software simply configures the ADC DMA and begins a DMA
transfer of ADC data to PS DRAM. This data is then written to a file. A script
for gnuplot is also included to plot this data and generate an image.

The continuous capture script will loop through ADC captures and plot image
generation continuously. This continuously updating image can then be displayed
on a webpage or similar for a very basic non-triggered analog scope
functionality. This script assumes that a lighttpd server is running on the
Brain 1 displaying an image from the webroot. Please see the included
`index.html` file for an example of this.

The C example can be built with:

`gcc -o capture -lm capture_single.c`
