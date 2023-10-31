const int TRIG_PIN_1 = 4; 
const int ECHO_PIN_1 = 12; 
const int TRIG_PIN_2 = 2; 
const int
ECHO_PIN_2 = 5; 
const int RED_PIN_1 = 27;
const int
GREEN_PIN_1 = 26; 
const int RED_PIN_2 = 33; 
const int
GREEN_PIN_2 = 32; 
int counter = 
0; float
duration_us_1, 
duration_us_2, 
distance_cm_1, 
distance_cm_2; 
void
setup() 
{ 
 Serial.begin(9600); 
 pinMode(TRIG_PIN_1, OUTPUT); 
pinMode(ECHO_PIN_1, INPUT); 
pinMode(TRIG_PIN_2, OUTPUT); 
pinMode(ECHO_PIN_2, INPUT); 
 pinMode(RED_PIN_1, OUTPUT); 
pinMode(GREEN_PIN_1, OUTPUT); 
 pinMode(RED_PIN_2, OUTPUT); 
pinMode(GREEN_PIN_2, OUTPUT); 
} 
void loop() 
{ counter = 
0; 
 
ultrasonic_1(); 
ultrasonic_2(); 
Serial.print("1: 
"); 
 Serial.println(distance_cm_1); 
Serial.print("2: "); 
 Serial.println(distance_cm_2); 
 
 Serial.print("Counter: "); 
 Serial.println(counter); 
 Serial.println(""); 
} void ultrasonic_1(){ 
digitalWrite(TRIG_PIN_1, 
HIGH); 
delayMicroseconds(10); 
digitalWrite(TRIG_PIN_1, 
LOW); 
 
 // measure duration of pulse from ECHO pin 
duration_us_1 = pulseIn(ECHO_PIN_1, 
HIGH); 
 
 // calculate the distance 
distance_cm_1 = 0.017 * 
duration_us_1; 
 if(distance_cm_1 < 
50) { red_1(); 
 Serial.println("Slot 1 Terisi"); 
counter++; 
 } else { 
green_1(); 
 } 
} void ultrasonic_2(){ 
digitalWrite(TRIG_PIN_2, 
HIGH); 
delayMicroseconds(10); 
digitalWrite(TRIG_PIN_2, 
LOW); 
 
 // measure duration of pulse from ECHO pin 
duration_us_2 = pulseIn(ECHO_PIN_2, 
HIGH); 
 
 // calculate the distance 
distance_cm_2 = 0.017 * 
duration_us_2; 
 if(distance_cm_2 < 
50) { red_2(); 
 Serial.println("Slot 2 Terisi"); 
counter++; } else { 
green_2(); 
 } 
} 
void red_1(){ 
digitalWrite(RED_PIN_1, 
HIGH); 
digitalWrite(GREEN_PIN_1, 
LOW); delay(1000); 
} void red_2(){ 
digitalWrite(RED_PIN_2, 
HIGH); 
digitalWrite(GREEN_PIN_2, 
LOW); delay(1000); 
} void green_1(){ 
digitalWrite(RED_PIN_1, 
LOW); 
digitalWrite(GREEN_PIN_1, 
HIGH); delay(1000); 
} void green_2(){ 
digitalWrite(RED_PIN_2, 
LOW); 
digitalWrite(GREEN_PIN_2, 
HIGH); delay(1000); 
}