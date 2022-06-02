// Loading the ESP32 WiFi library and the PubSubClient library
#include <WiFi.h>
#include <PubSubClient.h>
#define WIFI_TIMEOUT_MS 20000

// Change the credentials below, so your ESP8266 connects to your router
const char* ssid = "UGM-Hotspot";
const char* password = "";

const char* mqtt_server = "10.33.162.50";

// Initializes the espClient
WiFiClient espClient;
PubSubClient client(espClient);

// Connect an LED
const int ledGPIO5 = 4;
const int ledGPIO4 = 5;

void connectToWiFi(){
  Serial.print("");
  Serial.println("Connecting to WiFi");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  unsigned long startAttemptTime = millis();

  while (WiFi.status() != WL_CONNECTED && millis () - startAttemptTime < WIFI_TIMEOUT_MS){
    Serial.print(".");
    delay(500);
   }

   if(WiFi.status() != WL_CONNECTED){
    Serial.println("Failed!"); 
   }
   else {
    Serial.print("Connected");
    Serial.println(WiFi.localIP());
   }
}

void callback(String topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messageTemp += (char)message[i];
  }
  Serial.println();

  if(topic=="esp32/4"){
      Serial.print("Changing GPIO 4 to ");
      if(messageTemp == "1"){
        digitalWrite(ledGPIO4, HIGH);
        Serial.print("On");
      }
      else if(messageTemp == "0"){
        digitalWrite(ledGPIO4, LOW);
        Serial.print("Off");
      }
  }
  if(topic=="esp32/5"){
      Serial.print("Changing GPIO 5 to ");
      if(messageTemp == "1"){
        digitalWrite(ledGPIO5, HIGH);
        Serial.print("On");
      }
      else if(messageTemp == "0"){
        digitalWrite(ledGPIO5, LOW);
        Serial.print("Off");
      }
  }
  Serial.println();
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");

    if (client.connect("ESP32Client")) {
      Serial.println("connected");  
      // Subscribe or resubscribe to a topic
      client.subscribe("esp32/4");
      client.subscribe("esp32/5");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println("try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  pinMode(ledGPIO4, OUTPUT);
  pinMode(ledGPIO5, OUTPUT);
  
  Serial.begin(115200);
  connectToWiFi();
  client.setServer(mqtt_server, 1833);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  if(!client.loop())
    client.connect("ESP32Client");
}
