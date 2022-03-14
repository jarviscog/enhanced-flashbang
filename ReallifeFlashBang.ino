 // Arduino code to switch relay
#define relay_pin 5
#define check 7

int command = 0;

void setup() {
	pinMode(relay_pin, OUTPUT);
	Serial.begin(9600);
}

void loop() {

	while (Serial.available() > 0){
		command = Serial.read();
	}

	if (check == command){
		digitalWrite(7, HIGH);
		delay(3000);
		digitalWrite(7, LOW);
	}

	command = 0;
}
