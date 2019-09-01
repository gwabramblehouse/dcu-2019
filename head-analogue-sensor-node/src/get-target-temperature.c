// ###########################################################################
// Home Mobility Monitoring
//
// Reads the temperature of an DS3231 sensor attached to the top of the
// head analogue and prints to stdout.
// ###########################################################################

#include<stdio.h>
#include <time.h>
#include<fcntl.h>
#include<sys/ioctl.h>
/* #include<linux/i2c.h> */
#include<linux/i2c-dev.h>
#define BUFFER_SIZE 19      //0x00 to 0x12

// the time is in the registers in encoded decimal form
int bcdToDec(char b) { return (b/16)*10 + (b%16); }

int main(){
    int file;
    unsigned timeHigh, timeLow, timeCalc4;
    double timeCalc;
 
    if((file=open("/dev/i2c-1", O_RDWR)) < 0){
       perror("failed to open the bus\n");
       return 1;
    }
    if(ioctl(file, I2C_SLAVE, 0x68) < 0){
       perror("Failed to connect to the sensor\n");
       return 1;
    }
    char writeBuffer[1] = {0x00};
    if(write(file, writeBuffer, 1)!=1){
       perror("Failed to reset the read address\n");
       return 1;
    }
    char buf[BUFFER_SIZE];
    if(read(file, buf, BUFFER_SIZE)!=BUFFER_SIZE){
       perror("Failed to read in the buffer\n");
       return 1;
    }
    timeHigh = buf[0x11];
    timeLow = buf[0x12] & 0xC0;
    timeCalc4 = (timeHigh << 2) + (timeLow >> 6);
    time_t T= time(NULL);
    struct  tm tm = *localtime(&T);
      
    printf("%04d-%02d-%02d %02d:%02d:%02d %u %0.2f\n",
        tm.tm_year+1900, tm.tm_mon+1, tm.tm_mday, tm.tm_hour, tm.tm_min,
        tm.tm_sec, (unsigned long) T, timeCalc4 / 4.0);
 
    close(file);
    return 0;
}
