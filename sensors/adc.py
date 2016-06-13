import spidev
import time


#import sys

#if len(sys.argv) <= 1:
#    print('Pass channel number [0-3]')
#    sys.exit(0)

#if adc_channel < 0 or adc_channel > 3:
#    print('Invalid channel. Channel should be [0-3]')
#    sys.exit(0)

#print("Reading from channel %d" % (adc_channel))

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
# read SPI data from MCP3004 chip, 4 possible adc's (0 thru 3)
    if adcnum >3 or adcnum <0:
       return-1
    r = spi.xfer2([1,8+adcnum <<4,0])
    adcout = ((r[1] &3) <<8)+r[2]
    return adcout

#while True:
#    value=readadc(adc_channel)
#    volts=(value*3.3)/1024
#    print("%4d/1023 => %5.3f V" % (value, volts))
#    time.sleep(0.5)
#"""'''

