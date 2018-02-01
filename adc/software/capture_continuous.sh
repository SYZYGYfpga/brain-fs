
#while :
for i in 1 2 3 4 5 6 7 8 9 10
do
	./capture > /dev/null
	gnuplot plot_capture.gp
	cp output.png /www/pages/temp.png
	mv /www/pages/{temp.png,output.png}
done
