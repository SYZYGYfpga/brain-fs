#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define BRAM_ADDR       0x41200000
#define GPIO_RATE_FSADJ 0x42000000
#define GPIO_RESET      0x40000000

int waveform_ramp (int *wave_array, int length, int max_val)
{
	int i;
	float temp1 = 0;
	float increment = (float)max_val / (float)length;
	printf("increment = %f\n", increment);
	float temp2 = increment;

	for (i = 0; i < length / 2; i++) {
		wave_array[i] = ((int)floor(temp2) << 16) | (int)floor(temp1);
		temp1 += 2*increment;
		temp2 += 2*increment;
	}

	return 0;
}

int waveform_sine (int *wave_array, int length, int max_val)
{
	int i;
	float x, x_scale, y_scale, y_adjust;
	int y1,y2;

	x_scale = 2 * M_PI * (1/(float)length);
	y_scale = (float)max_val / 2;
	y_adjust = 1.0;

	for (i = 0; i < length; i++) {
		x = x_scale * i;
		y1 = (int) floor((sin(x) + y_adjust) * y_scale);
		i++;
		x = x_scale * i;
		y2 = (int) floor((sin(x) + y_adjust) * y_scale);
		wave_array[i >> 1] = (y2 << 16) | y1;
	}

	return 0;
}

int main (int argc, char *argv[])
{
	int *bram_addr;
	int *rate_addr;
	int *reset_addr;
	int waveform_array[4096];
	int mem_fd;
	int i;
	int rate = 0, selected_waveform = 0;
	int iampl = -1, qampl = -1;
	int reset = 0;

	if (argc == 1) {
		printf("USAGE: %s [-w sine|ramp] [-c RATE] [-i AMPL] [-q AMPL] [-r]\n", argv[0]);
		printf("  RATE is given as an integer from 1 to 1024\n");
		printf("  AMPL is given as an integer from 0 to 63\n");
		printf("    AMPL controls the amplitude of the {i,q} channels through the IRSET/QRSET SPI code\n");
		printf("    See the AD9114 Datasheet Figure 98 for the effect of this code on the full scale output\n");
		printf("  -r will send a software reset signal to the design\n");
		exit(0);
	} else {
		for(i = 1; i <= argc-1; i++) {
			if(!strcmp(argv[i],"-w")) {
				i++;
				if(!strcmp(argv[i],"sine")) {
					printf("Sine wave selected.\n");
					selected_waveform = 1;
				} else if(!strcmp(argv[i],"ramp")) {
					printf("Ramp wave selected.\n");
					selected_waveform = 2;
				} else {
					printf("Unknown waveform\n");
					exit(1);
				}
			} else if (!strcmp(argv[i],"-c")) {
				i++;
				rate = atoi(argv[i]);
			} else if (!strcmp(argv[i],"-i")) {
				i++;
				iampl = atoi(argv[i]);
			} else if (!strcmp(argv[i],"-q")) {
				i++;
				qampl = atoi(argv[i]);
			} else if (!strcmp(argv[i],"-r")) {
				reset = 1;
			} else {
				printf("Unknown command\n");
				exit(1);
			}
		}
	}
				
	mem_fd = open("/dev/mem", O_RDWR);
	
	printf("mem_fd: %d\n", mem_fd);

	if(selected_waveform == 1) {
		waveform_sine(waveform_array, 8192, 4096);
	} else if (selected_waveform == 2) {
		waveform_ramp(waveform_array, 8192, 4096);
	}

	if(reset != 0) {
		reset_addr = mmap(0x00, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, GPIO_RESET);

		printf("reset_addr: %08X\n", reset_addr);

		// Toggle reset
		*(reset_addr) = 1;
		*(reset_addr) = 0;
	}


	if(selected_waveform > 0) {
		bram_addr = mmap(0x00, 16384, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, BRAM_ADDR);

		printf("bram_addr: %08X\n", bram_addr);

		for (i = 0; i < 4096; i++) {
			*(bram_addr + i) = waveform_array[i];
			//printf("\rCurrent location: %d", i);
		}
	}
	
	if(rate > 0 | iampl >= 0 | qampl >= 0) {
		rate_addr = mmap(0x00, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, GPIO_RATE_FSADJ);
		printf("rate_addr: %08X\n", rate_addr);
	}

	if(rate > 0) {
		*(rate_addr) = rate;
	}

	if(iampl >= 0) {
		*(rate_addr + 2) = (*(rate_addr + 2) & 0xFF00) | (iampl & 0x00FF);
	}

	if(qampl >= 0) {
		*(rate_addr + 2) = (*(rate_addr + 2) & 0x00FF) | ((qampl << 8) & 0xFF00);
	}

	printf("\nDone\n");

	return 0;
}
