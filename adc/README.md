# Syzygy Brain 1 ADC Sample

## Overview

This sample project is designed to demonstrate usage of the POD-ADC-LTC2264-12
SYZYGY module from Opal Kelly. This sample is designed to interface with the
pod connected to PORT D on the Brain-1.

Both analog inputs on the ADC are deserialized by logic in the PL portion
of the Zynq and fed into PS memory by a DMA transfer.

This project is based heavily on Xilinx Application Note 524 (XAPP524) and
implements a simplified version of the design described by Xilinx.

## Simulation

A simple simulation of the design can be performed using the syzygy-adc-tb.v.
Note that this is not intended as a full simulation and verification suite, the
user must confirm that the data output from the simulation matches the expected
values. This simulation is provided as-is and its accuracy is not guaranteed.

## Building

To build this design, start a new Vivado project with the xc7z012s part
selected and add the sources in the HDL folder to the project. The
"design\_1.bd" file can be added as an IP. A wrapper for the block design
must be generated before the project can be built. This can be accomplished
by right clicking on the block design in the "Design Sources" view and
selecting the "Generate HDL Wrapper" option.

With the project created and sources added, simply click the "Generate
Bitstream" button in the Vivado Flow Navigator to build a bitstream.
The result can be found in the Vivado project folder under:

`(project name).runs/impl\_1/(project name).bit`

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
