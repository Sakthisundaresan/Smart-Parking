import RPi.GPIO as 
GPIO 
 import time import 
paho.mqtt.client as mqtt 
 # Initialize the MQTT client 
client = 
mqtt.Client("ParkingSensor") 
client.connect("your_broker_ip", 
1883, 60) 
 GPIO.setmode(GPIO.BCM) 
 TRIG = 23 
 ECHO = 24 
 GPIO.setup(TRIG,GPIO.OUT) 
 GPIO.setup(ECHO,GPIO.IN) 
 while True: 
 GPIO.output(TRIG, False) 
 time.sleep(2) 
 GPIO.output(TRIG, True) 
time.sleep(0.00001) 
 GPIO.output(TRIG, False) 
 while GPIO.input(ECHO)==0: 
 pulse_start = time.time() 
 while GPIO.input(ECHO)==1: 
pulse_end = time.time() 
 pulse_duration = pulse_end -
pulse_start distance = 
pulse_duration * 17150 distance = 
round(distance, 2) 
 if distance < 10: # Adjust this threshold based on your setup 
client.publish("parking/spot1", "Occupied") 
 else: 
 client.publish("parking/spot1", "Vacant") 