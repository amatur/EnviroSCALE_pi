import os
#cmd = 'ifdown wlan0'
#os.system(cmd)
#cmd = "bash start3g.sh"
#os.system(cmd)

def reconnect():
    cmd = 'sudo bash netpi/restart_net.sh'
    os.system(cmd)

#def reconnect():
#    cmd = 'sudo bash /home/pi/workshop/DEPLOYv1.1/netpi/restart_wifi.sh'
#    os.system(cmd)

