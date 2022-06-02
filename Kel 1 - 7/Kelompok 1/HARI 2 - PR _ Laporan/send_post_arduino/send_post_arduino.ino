// KELOMPOK 1 ARM 2 (CATUR WARDANA, SANTI RAHAYU)
#include <WiFi.h>
#include <HTTPClient.h> 
const int potPin = 34;
int potValue = 0;

const char* ssid = "hghh";
const char* password =  "11111111";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
}

void loop() {

 if(WiFi.status()== WL_CONNECTED){   //Check WiFi connection status
   HTTPClient http;   
   potValue = analogRead(potPin);
   int adc;
   adc = potValue;

   http.begin("http://192.168.232.50:5000/post");
   http.addHeader("Content-Type", "text/plain");             

   int httpResponseCode = http.POST(String(adc));

   if(httpResponseCode >=0 || httpResponseCode <0);
  {
    Serial.print("Data ADC terkirim");
  }
   Serial.print('\n');
   Serial.print("ADC Send: ");
   Serial.println(adc);
   http.end();
 }
 
 else{
    Serial.println("Error in WiFi connection");   
 }
  delay(1000);
}
