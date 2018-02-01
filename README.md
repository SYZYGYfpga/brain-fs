# Brain-1 Filesystem

This repository contains the home folder filesystem distributed with the
[SYZYGY Brain-1](http://syzygyfpga.io/hub/).

Demo software is included for the launch peripherals. This software includes
a C-based application for each peripheral enabling interaction with the 
peripheral from a Linux software environment running on the Zynq CPU.

Also included are a set of web pages that, when hosted on a Brain-1,
enable the user to interact with the peripherals through a web interface
running on a remote computer.

HDL sources for the FPGA bitstreams can be found in the brain-sample-hdl
repository.

## Requirements

The contents of this repository are intended to be used as part of the
official SYZYGY Brain-1 SD Card image. This image is configured to host
a web server distributing content out of the brain-fs/www folder.

Each demo requires that the associated pod be attached to the Brain-1.

## Updating

Updates to this filesystem can be obtained by running `git pull`, updating
both the FPGA bitfiles along with the associated web pages and sample
applications.

