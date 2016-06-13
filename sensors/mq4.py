import math
import time
from adc import readadc
from Sensor import Sensor
from my_libs import *

setup_logging()
log = logging.getLogger("MQ4Exception")

#delay = 0.2 second
class MQ4(Sensor):
    def __init__(self, analog):
        self.analog = analog
        self.interval = 0.2
        self.verbose = False
        self.device_name = "MQ4"

        self.RL_VALUE = 6.0
        self.RO_CLEAN_AIR_FACTOR = 10
        self.CALIBARAION_SAMPLE_TIMES = 30
        self.CALIBRATION_SAMPLE_INTERVAL = 500 / 1000
        # cablibration phase
        self.READ_SAMPLE_INTERVAL = 1
        self.READ_SAMPLE_TIMES = 5
        #
        self.GAS_meth = 1
        self.GAS_cng = 0
        #
        self.methCurve = [2.3, 0.2788, -.3856]
        #cngCurve= [x,y,m]
        self.Ro= 13.0


    def MQResistanceCalculation(self, raw_adc):
        return ( (self.RL_VALUE*(1023-raw_adc)/raw_adc))


    def MQCalibration(self):
        val=0.0
        for i in range (0, self.CALIBARAION_SAMPLE_TIMES):
            val += self.MQResistanceCalculation(readadc(self.analog))
            time.sleep(self.CALIBRATION_SAMPLE_INTERVAL)

        val = val/self.CALIBARAION_SAMPLE_TIMES

        val = val/self.RO_CLEAN_AIR_FACTOR

        return val


    def MQGetGasPercentage(self, rs_ro_ratio, gas_id):

        if  gas_id == self.GAS_meth :
            return (10**( ((math.log(rs_ro_ratio)- self.methCurve[1])/self.methCurve[2]) + self.methCurve[0]))
        if  gas_id == self.GAS_cng :
            return (10**( ((math.log(rs_ro_ratio)-self.cngCurve[1])/self.cngCurve[2]) + self.cngCurve[0]))

        return 0


    def read(self):
        val = -1
        try:
            # print("Calibrating..")
            Ro = self.MQCalibration()
            # print("Calibration is done...")
            # print "Ro=", Ro, "kohm"
            ans = 0.0
            # print("Methane: "),
            for i in range(0, 20):
                cur = self.MQGetGasPercentage(readadc(self.analog) / Ro, self.GAS_meth)
                ans += cur
                time.sleep(1.0 / 100.0)
            if (self.verbose):
                print "<{}> Methane concentration: ".format(self.device_name), ans / 20.0, " ppm"
            val = ans / 20.0

        except:
            eprint("ERROR in READ...PI/sensors/mq4.py")
            log.exception('ERROR in READ...PI/sensors/mq4.py')
        return val


#print("CNG: "),
#print(MQGetGasPercentage(readadc(MQ_PIN)/Ro,GAS_cng) ),
#print( " ppm" )

# sensor = MQ4(2)
# sensor.takeAvgReading(3)
