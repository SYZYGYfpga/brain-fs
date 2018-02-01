# Syzygy Hub Helloworld
Simple "hello world" FPGA design for the SYZYGY Hub that runs a counter on the LEDs.

The pre-built bitfile for this design can be found in the "binary" folder.

# Building
To build this design, start a new Vivado project with the xc7z012s part selected and
add the sources in the HDL folder to the project. The "design_1.bd" file can be added
as an IP.

With the project created and sources added, simply click the "Generate Bitstream"
button in the Vivado Flow Navigator to build a bitstream. The result can be found
in the Vivado project folder under (project name).runs/impl_1/(project name).bit.

