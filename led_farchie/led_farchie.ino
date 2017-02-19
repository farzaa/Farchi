#define SLEEP_LED 13


int flashes_left = 10;
int state = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  digitalWrite(SLEEP_LED, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (flashes_left > 0)
  {
    flashes_left -= 1;
    digitalWrite(SLEEP_LED, state);
    state ^= HIGH;
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
      flashes_left = 10; 
    }

    // Received byte to turn on FOCUS LED
    if (received == 'f')
    {
      
    }
  }

}

void toggle_sleep_light()
{
  static int on = 0;

  digitalWrite(SLEEP_LED, on);
  on ^= 1;
}


void toggle_text_light()
{
  static int on = 0;
}

void toggle_focused_light()
{
  static int on = 0;
}

