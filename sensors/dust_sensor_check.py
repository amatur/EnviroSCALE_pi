import dust
import time

while True:
	data = dust.read()
	print data
	time.sleep(0.5)
