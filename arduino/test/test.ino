
const int ledPin = 6;
int incomingByte = 0; 
String inString = ""; 
void setup() {  
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
    analogWrite(ledPin, 0);
    digitalWrite(ledPin, HIGH);
}

void loop() {
    if (Serial.available() > 0) {
        incomingByte = Serial.read();
        analogWrite(ledPin, incomingByte);
    }
//  listen();
}

int output = 0;
void dim(int a){
  if (output == 0){
    analogWrite(ledPin, 1);
  }
  else{
    analogWrite(ledPin, 0);
  }
  output ++;
  output = output % a;
  delay(1);
}

void listen(){
  if (Serial.available() > 0) {
   while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string, then the string's value:
    delay(2);
  }
        Serial.print("Value:");
      Serial.println(inString.toInt());
      analogWrite(ledPin, inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      // clear the string for new input:
      inString = "";
}
}

