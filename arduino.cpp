#include <ESP8266WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "PASSWORD");  // SSID ve şifreyi girin

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Bağlanılıyor...");
  }

  Serial.println("Bağlandı.");
}

void loop() {
  long rssi = WiFi.RSSI();
  Serial.print("Sinyal Gücü: ");
  Serial.print(rssi);
  Serial.println(" dBm");
  delay(1000);  // 1 saniye bekle
}
