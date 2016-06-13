from sensors.dust import Dust
from sensors.dust_raw_voltage import Dust_Raw
from sensors.mq135 import MQ135
import time

def calibrate():
	dust_raw = Dust_Raw(3, 17)
	dust_raw.verbose = True
	i = 0
	total = 0
	while i < 50:
		total += dust_raw.read()
		i += 1
	mean = total / 50.0
	no_dust = mean - 150
	dust = Dust(3, 17, no_dust)
	return dust

#dust = calibrate()
#dust.verbose = True
#while True:
	#dust.calibrate135()
#	data = dust.read()
#	print data
#	time.sleep(0.5)
