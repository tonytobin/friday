//tested in a nodemcu 12e(esp8266)
//connect different color led to pin 12,13,15

char data;
char mcu;
void setup() {  
  pinMode(15,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect.
  }
}

void loop() { // run over and over
  if (Serial.available()) {
    data=(Serial.read());
    
  }
    delay(10);
    if(data=='l'){
     // simulates listening
      digitalWrite(12,0);
      digitalWrite(15,0);
      digitalWrite(13,1);
      
    }
    if(data=='s'){
      //simulates speaking
     digitalWrite(13,0);
     digitalWrite(15,0);
     digitalWrite(12,1);
      
    }
    if(data=='q'){
      //simulates shutdown
      digitalWrite(12,0);
      digitalWrite(13,0);
      for(int i =1;i<5;i++){
       // digitalWrite(13,1);
        digitalWrite(15,1);
        delay(500);
        //digitalWrite(13,0);
        digitalWrite(15,0);
        delay(500);
      }
      digitalWrite(13,0);
      digitalWrite(15,0);
      digitalWrite(12,0);
      data=' ';
    }
    if(data=='e'){
      //turn off all pins
      digitalWrite(12,0);
      digitalWrite(13,0);
      digitalWrite(15,0);
    }
}
