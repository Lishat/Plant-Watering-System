#!/usr/bin/python
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085
import urllib2
import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
L = []
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial = GPIO.LOW)
def publish(Tem, humidity, Press, Alt, Sea_Press, SoilMoisture, SoilMoisture2, WaterLevel, RainSensor, Ultrasonic):
	url = "https://lishat.pythonanywhere.com/temp/display/" +str(Tem)+"/"+str(humidity)+"/"+str(Press)+"/"+str(Alt)+"/"+str(Sea_Press)+"/"+str((1024-float(SoilMoisture))*100/1024)+"/"+str((1024-float(SoilMoisture2))*100/1024)+"/"+str(WaterLevel)+ "/" + str(RainSensor)+"/" +str(Ultrasonic)+"/"+" ".join(str(time.asctime(time.localtime())).split())+"/"
       	print(url)
	result = urllib2.urlopen(url).read()
	#url1 = "http://10.0.3.23:8122/temp/display/" +str(Tem)+"/"+str(humidity)+"/"+str(Press)+"/"+str(Alt)+"/"+str(Sea_Press)+"/"+str((1024-float(SoilMoisture))*100/1024)+"/"+str(WaterLevel)+ "/" + str(RainSensor)+"/" +str(Ultrasonic)+"/"+" ".join(str(time.asctime(time.localtime())).split())+"/"
	#print(url1)
	#result = urllib2.urlopen(url1).read()
t=0		
while (True):
	while(len(L) != 5):
		try:
			ser = serial.Serial('/dev/ttyACM0',9600) 
			read_serial=ser.readline()
			L = read_serial.split()
			print read_serial
		except: 
			pass
	humidity, temperature =Adafruit_DHT.read_retry(11, 4)
	print ("Humidity ={}%; Temperature ={} C".format(humidity,temperature))
	sensor = BMP085.BMP085()
	Tem = sensor.read_temperature()
	Press = sensor.read_pressure()
	Alt = sensor.read_altitude()
	Sea_Press = sensor.read_sealevel_pressure()
	print 'Temp = {0:0.2f} *C'.format(Tem) # Temperature in Celcius
	print 'Pressure = {0:0.2f} Pa'.format(Press) # The local pressure
	print 'Altitude = {0:0.2f} m'.format(Alt) # The current altitude
	print 'Sealevel Pressure = {0:0.2f} Pa'.format(Sea_Press) # The sea-level pressure
	print str(time.asctime(time.localtime()))
	if(urllib2.urlopen("https://lishat.pythonanywhere.com/temp/auto/").read().strip() == "1"):
		if(float(L[0]) >= 700 and float(L[2]) >= 700):
			GPIO.output(22, GPIO.HIGH)
		else:
			GPIO.output(22, GPIO.LOW)
		if(float(L[4]) >= 700 and float(L[2]) >= 700):
			GPIO.output(23, GPIO.HIGH)
		else:
			GPIO.output(23, GPIO.LOW)
	else:
		if(urllib2.urlopen("https://lishat.pythonanywhere.com/temp/motor1/").read().strip() == "1"):
			GPIO.output(22, GPIO.HIGH)
		else:
			GPIO.output(22, GPIO.LOW)
		if(urllib2.urlopen("https://lishat.pythonanywhere.com/temp/motor2/").read().strip() == "1"):
			GPIO.output(23, GPIO.HIGH)
		else:
			GPIO.output(23, GPIO.LOW)
	publish(Tem, humidity, Press, Alt, Sea_Press, L[0], L[4], L[1], L[2], L[3])
	print "YES"
	L = []