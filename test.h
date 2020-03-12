int current = 0;
int dat = 0;
int code = 2424;
int attempts = 3;
boolean triggered = true;
// 7segment display
#include <TM1637Display.h>
#define CLK 2
#define DIO 3
TM1637Display display = TM1637Display(CLK, DIO);
const uint8_t data[] = {0xff, 0xff, 0xff, 0xff};
const uint8_t blank[] = {0x00, 0x00, 0x00, 0x00};

// buttons
const int btn1 = 8, btn2 = 9, btn3 = 6, btn4 = 7;
int prev1 = 0, prev2 = 0, prev3 = 0, prev4 = 0;
int btnst1 = 1, btnst2 = 1, btnst3 = 1, btnst4 = 1;
int read1, read2, read3, read4;
unsigned long lastDebounceTime = 0; // the last time the output pin was toggled
unsigned long debounceDelay = 50;   // the debounce time; increase if the output flickers

void setup()
{
    // put your setup code here, to run once:
    display.clear();
    Serial.begin(9600);
    pinMode(btn1, INPUT_PULLUP);
    pinMode(btn2, INPUT_PULLUP);
    pinMode(btn3, INPUT_PULLUP);
    pinMode(btn4, INPUT_PULLUP);
}

void loop()
{
    // put your main code here, to run repeatedly:
    if (current != 0)
    {
        display.setBrightness(7);
        display.showNumberDec(dat, false, 4, 0);
    }

    read1 = digitalRead(btn1);
    read2 = digitalRead(btn2);
    read3 = digitalRead(btn3);
    read4 = digitalRead(btn4);

    if ((read1 != prev1) || (read2 != prev2) || (read3 != prev3) || (read4 != prev4))
    {
        lastDebounceTime = millis();
    }

    if ((millis() - lastDebounceTime) > debounceDelay)
    {
        if (read1 != btnst1)
        {
            btnst1 = read1;
            if (btnst1)
            {
                Serial.print("1");
                dat = dat * 10;
                dat += 1;
                current++;
            }
        }
        if (read2 != btnst2)
        {
            btnst2 = read2;
            if (btnst2)
            {
                Serial.print("2");
                dat = dat * 10;
                dat += 2;
                current++;
            }
        }
        if (read3 != btnst3)
        {
            btnst3 = read3;
            if (btnst3)
            {
                Serial.print("3");
                dat = dat * 10;
                dat += 3;
                current++;
            }
        }
        if (read4 != btnst4)
        {
            btnst4 = read4;
            if (btnst4)
            {
                Serial.print("4");
                dat = dat * 10;
                dat += 4;
                current++;
            }
        }
    }

    if (current == 4)
    {
        if (dat == code)
        {
            triggered = false;
            Serial.println("disarmed");
        }
        else
        {
            Serial.println("Wrong code");
            attempts--;
            current = 0;
            dat = 0;
            if (attempts == 0)
            {
                Serial.println("trigger alarm");
            }
        }
    }

    prev1 = read1;
    prev2 = read2;
    prev3 = read3;
    prev4 = read4;
}