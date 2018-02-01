# Simple GNUPlot script to generate an image of a plot
# from an ADC data capture. This assumes that the data
# is interleaved between channels and is stored with
# two bytes per sample (uint16).

set terminal png size 1000,750
set output 'output.png'

set xrange[-1:262144]
set yrange[0:65535]

plot 'capture.bin' binary format='%uint16%*uint16' using 1 title "channel 1" with lines,\
     'capture.bin' binary format='%*uint16%uint16' using 1 title "channel 2" with lines

