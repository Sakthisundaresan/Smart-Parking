import RPi.GPIO as 
GPIO import time 
# Define GPIO pins for ultrasonic sensors 
TRIG_PIN = 23 
ECHO_PIN = 24 
# Set up GPIO mode 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TRIG_PIN, GPIO.OUT) 
GPIO.setup(ECHO_PIN, GPIO.IN) 
def distance(): 
 # Trigger the ultrasonic sensor 
GPIO.output(TRIG_PIN, True) 
 time.sleep(0.00001) 
 GPIO.output(TRIG_PIN, False) 
 # Measure the time it takes for the echo to return 
 while GPIO.input(ECHO_PIN) == 0: 
 pulse_start = time.time() 
 while GPIO.input(ECHO_PIN) == 1: 
 pulse_end = time.time() 
 # Calculate the distance pulse_duration = 
pulse_end - pulse_start distance = pulse_duration * 
17150 # Speed of sound in cm/s 
 return round(distance, 2) 
try: 
while 
True:
 dist = distance() 
if dist < 10: 
# Adjust this threshold for your parking space 
print("Parking space occupied") 
 else: 
 print("Parking space available") 
time.sleep(2) # Wait before checking again 
except KeyboardInterrupt: 
 GPIO.cleanup()
