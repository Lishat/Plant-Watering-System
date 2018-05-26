const int trigPin = 6;
const int echoPin = 7;
/*#define ACTUATORHIGH 9
#define ACTUATORLOW 10*/
long duration;
int distance;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);
  /*pinMode(ACTUATORHIGH, OUTPUT); 
  pinMode(ACTUATORLOW, OUTPUT);*/ 
}

void loop() {
  // put your main code here, to run repeatedly:
  //digitalWrite(ACTUATORLOW, LOW);
  float soilMoisture = analogRead(A0);
  float waterLevel = analogRead(A1);
  float rainDrop = analogRead(A2);
  float soilMoisture2 = analogRead(A3);
  
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    // Calculating the distance
    distance= duration*0.034/2;
  Serial.println(String(soilMoisture) + " " + String(waterLevel) + " " + String(rainDrop) + " " + String(distance) + " " + String(soilMoisture2));
  /*if(soilMoisture >= 700 and rainDrop >= 700)
  {
    digitalWrite(ACTUATORHIGH, HIGH);
  }*/
  delay(3000);
  /*digitalWrite(ACTUATORHIGH, LOW);*/
}
