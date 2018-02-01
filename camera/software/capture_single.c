#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

#define DMA_OFFSET     0x40400000
#define GPIO_OFFSET    0x41200000
#define GPIO_IN_OFFSET 8

#define DMA_CONTROL_OFFSET 0x30
#define DMA_STATUS_OFFSET  0x34
#define DMA_ADDR_OFFSET    0x48
#define DMA_LENGTH_OFFSET  0x58

#define GPIO_STATUS_MASK 0x10000
#define GPIO_FRAMES_MASK 0xff00
#define GPIO_ERROR_MASK  0x00ff
#define GPIO_START_MASK  0x1

#define DMA_REG_SIZE 65536
#define GPIO_REG_SIZE 4096

#define DMA_DEST_ADDR 0x3FB00000
// At 1 byte per pixel the size is equal to the resolution
#define DMA_LENGTH_BYTES 2304 * 1296
#define DMA_RESET_BIT 0x4
#define DMA_START_BIT 0x1

int setup_dma (int mem_fd)
{
	int *dma_addr;
	int temp;

	dma_addr = mmap(0x00, DMA_REG_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, DMA_OFFSET);

	printf ("dma_addr: %.8X\n", dma_addr);

	*(dma_addr + (DMA_CONTROL_OFFSET/4)) = DMA_RESET_BIT;

	while ((*(dma_addr + (DMA_CONTROL_OFFSET/4))) & 0x4);

	*(dma_addr + (DMA_CONTROL_OFFSET/4)) = DMA_START_BIT; // Start DMA Transfer

	while ((*(dma_addr + (DMA_STATUS_OFFSET/4))) & 0x1);

	*(dma_addr + (DMA_ADDR_OFFSET/4)) = DMA_DEST_ADDR;

	*(dma_addr + (DMA_LENGTH_OFFSET/4)) = DMA_LENGTH_BYTES;


	temp = *(dma_addr + (DMA_STATUS_OFFSET/4));
	printf("dma_status = %.8X\n", temp);
	temp = *(dma_addr + (DMA_ADDR_OFFSET/4));
	printf("dma_addr = %.8X\n", temp);
	temp = *(dma_addr + (DMA_LENGTH_OFFSET/4));
	printf("dma_length = %.8X\n", temp);
	temp = *(dma_addr + (DMA_CONTROL_OFFSET/4));
	printf("dma_control = %.8X\n", temp);

	munmap(dma_addr, DMA_REG_SIZE);

	return 0;
}

int check_dma_status (int mem_fd)
{
	int *dma_addr;
	int return_val;
	int temp;

	dma_addr = mmap(0x00, DMA_REG_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, DMA_OFFSET);

	printf ("dma_addr: %.8X\n", dma_addr);

	return_val = *(dma_addr + (DMA_STATUS_OFFSET/4));

	temp = *(dma_addr + (DMA_LENGTH_OFFSET/4));
	printf("dma_length = %.8X\n", temp);
	
	munmap(dma_addr, DMA_REG_SIZE);

	return return_val;
}

int start_capture (int mem_fd)
{
	int *gpio_in_addr; // GPIO to FPGA

	gpio_in_addr = mmap(0x00, GPIO_REG_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, GPIO_OFFSET);

	printf ("gpio_in_addr: %.8X\n", gpio_in_addr);

	*(gpio_in_addr + 2) = 1 & GPIO_START_MASK;

	usleep(10); // Give a short wait for the signal to sync

	*(gpio_in_addr + 2) = 0 & GPIO_START_MASK;

	munmap(gpio_in_addr, GPIO_REG_SIZE);

	return 0;
}

int check_status (int mem_fd)
{
	int *gpio_out_addr;
	int status_val;

	gpio_out_addr = mmap(0x00, GPIO_REG_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, GPIO_OFFSET);

	//printf ("gpio_out_addr: %.8X\n", gpio_out_addr);

	status_val = (*(gpio_out_addr) & GPIO_STATUS_MASK);

	munmap(gpio_out_addr, GPIO_REG_SIZE);

	return status_val;
}

int main()
{
	int mem_fd;
	FILE *capture_file_ptr;
	char *capture_mem_ptr;

	mem_fd = open("/dev/mem", O_RDWR);

	printf("Setting up DMA\n");
	setup_dma(mem_fd);

	printf("Setting up Camera Interface\n");
	start_capture(mem_fd);

	printf("Waiting for capture to complete\n");
	while (check_status(mem_fd) == 0) {
	}

	usleep(100000);
	printf("DMA Status: %.8X\n", check_dma_status(mem_fd));

	printf("Image captured, saving data...\n");

	capture_file_ptr = fopen("capture.bin","wb");

	capture_mem_ptr = mmap(0x00, DMA_LENGTH_BYTES, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, DMA_DEST_ADDR);

	fwrite(capture_mem_ptr, 1, DMA_LENGTH_BYTES, capture_file_ptr);

	fclose(capture_file_ptr);
	munmap(capture_mem_ptr, DMA_LENGTH_BYTES);

	printf("Done!\n");

	return 0;
}

