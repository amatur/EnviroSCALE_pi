import paho.mqtt.publish as pub
from socket import *
from my_libs import *

setup_logging()
log = logging.getLogger("MQTTException")


####################################################
#   For publishing sensor data to iot.eclipse.org
####################################################
def publish(topic, message):
    try:
        msgs = [{'topic': "paho/test/iotBUET/"+topic, 'payload': message},
                ("paho/test/multiple", "multiple 2", 0, False)]
        pub.multiple(msgs, hostname="iot.eclipse.org")
        return True

    except gaierror:
        log.exception('[MQTT] Publish ERROR.', exc_info=True)
        eprint ("[MQTT] Publish ERROR." )
        return False


def publish_packet(message):
    try:
        msgs = [{'topic': "paho/test/iotBUET/bulk/", 'payload': message},
                ("paho/test/multiple", "multiple 2", 0, False)]
        pub.multiple(msgs, hostname="iot.eclipse.org")
        return True

    except gaierror:
        log.exception('[MQTT] Publish ERROR.', exc_info=True)
        eprint ("[MQTT] Publish ERROR." )
        return False

def publish_packet_raw(message):
    try:
        msgs = [{'topic': "paho/test/iotBUET/bulk_raw/", 'payload': message},
                ("paho/test/multiple", "multiple 2", 0, False)]
        pub.multiple(msgs, hostname="iot.eclipse.org")
        return True

    except gaierror:
        log.exception('[MQTT] Publish ERROR.', exc_info=True)
        eprint ("[MQTT] Publish ERROR." )
        return False


def test_connection():
    try:
        msgs = [{'topic': "paho/test/iotTEST/" },
                ("paho/test/multiple", "multiple 2", 0, False)]
        pub.multiple(msgs, hostname="iot.eclipse.org")
        return True

    except gaierror:
        log.exception('[MQTT] Connection Test ERROR.', exc_info=True)
        eprint ("[MQTT] Connection Test ERROR." )
        return False

