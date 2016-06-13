sudo ifdown wlan0
sleep 2
sudo bash /home/pi/msarwaru/sakis3g  connect --console APN='CUSTOM_APN' USBINTERFACE='0' USBDRIVER='sierra' OTHER='USBMODEM' USBMODEM="12d1:1417" CUSTOM_APN='blweb' APN_USER='blank' APN_PASS='blank'
sleep 2

if [ "$(ping -c2 -w1 -q 192.168.1.1 |grep -wc "1 packets")" -ne 1 ]; then
   echo "ping fail" 
   sudo bash /home/pi/msarwaru/sakis3g disconnect
   sudo ifup wlan0
fi

