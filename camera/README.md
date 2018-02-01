# SYZYGY Brain 1 Camera Sample

## Overview

This project is a simple demo for the POD-CAMERA peripheral and the SYZYGY
Brain 1 carrier.

This demo implements a physical interface to the camera that is used to 
constantly retrieve pixel and frame information from the camera.
When triggered by software, an image is copied via an AXI DMA into DRAM
attached to the PS portion of the Zynq. Software running on the PS then writes
the image data from DRAM to a raw binary file. The data in this file can be
manipulated into an image and viewed with Octave or other image manipulation
tools.

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
directory. The `single_capture.c` file contains an example program that can
capture a single frame from the camera and store it in a file. This file can
then either be viewed using the `disp_capture.m` octave script or converted
to an image using the `bayer2rgb` program and `imagemagick`.

If both imagemagick and bayer2rgb are installed on the Brain 1, the continuous
capture script can be used to continually retrieve images from the sensor and
prepare them for display. This script assumes that a lighttpd server is running
on the Brain 1 displaying an image from the webroot. Please see the included
`index.html` file for an example of this.

The `camera_regs.sh` script is used to configure the cameras I2C registers
for use with the Brain 1. This script depends on the `i2cread` and `i2cwrite`
programs to perform 16-bit addressed reads/writes over I2C. The default
register settings in this script should perform well in most reasonably
well-lit rooms, though some settings may need to be adjusted.

The C example can be built with:

`gcc -o capture_single -lm capture_single.c`
