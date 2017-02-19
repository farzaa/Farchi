#define SLEEP_LED 13
#define TEXT_LED 14
#define FOCUS_LED 15

int flashes_left = 21;
int state = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  digitalWrite(SLEEP_LED, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (flashes_left == 0)
    digitalWrite(TEXT_LED, LOW);
  if (flashes_left > 0)
    flashes_left -= 1;
    
  if (flashes_left % 2 == 0 && flashes_left != 0)
  {
    digitalWrite(TEXT_LED, LOW);
    delay(100);
  }

  if (flashes_left % 2 == 1 && flashes_left != 0)
  {
    digitalWrite(TEXT_LED, HIGH);
    delay(100);
  }
  
  if (Serial.available())
  {
    char received = Serial.read();

    // Received byte to turn on SLEEP LED
    if (received == 's')
    {
      digitalWrite(SLEEP_LED, HIGH); 
    }

    // SLEEP IS OFF
    if (received == 'r')
    {
      digitalWrite(SLEEP_LED, LOW); 
    }
    
    // Received byte to turn on TEXTING LED
    if (received == 't')
    {
      flashes_left = 21; 
    }

    // Received byte to turn on FOCUS LED
    if (received == 'f')
    {
      digitalWrite(FOCUS_LED, HIGH);
    }

    // NOT FOCUSED
    if (received == 'g')
    {
      digitalWrite(FOCUS_LED, LOW); 
    }
  }

}
