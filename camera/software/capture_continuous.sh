
#for i in 1 2 3 4 5 6 7 8 9 10
while :
do
	./capture_single > /dev/null
	bayer2rgb -i capture.bin -o output.tiff -w 2304 -v 1296 -b 8 -f GRBG -m NEAREST -t
	convert output.tiff output.jpg 2> /dev/null
	cp output.jpg /www/pages/temp.jpg
	mv /www/pages/{temp.jpg,output.jpg}
done
