char data;
char mcu;
void setup() {
  // Open serial communications and wait for port to open:
  pinMode(15,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
}

void loop() { // run over and over
  if (Serial.available()) {
    data=(Serial.read());
    
  }
  //Serial.println(data);
    delay(10);
    if(data=='l'){
     // Serial.println("welcome sir");
      digitalWrite(12,0);
      digitalWrite(15,0);
      digitalWrite(13,1);
      
    }
    if(data=='s'){
     // Serial.println("goodbye sir");
     digitalWrite(13,0);
     digitalWrite(15,0);
     digitalWrite(12,1);
      
    }
    if(data=='q'){
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
      digitalWrite(12,0);
      digitalWrite(13,0);
      digitalWrite(15,0);
    }
}
