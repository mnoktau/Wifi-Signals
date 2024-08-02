import serial
import time

ser1 = serial.Serial('COM3', 115200)  # İlk Arduino için
ser2 = serial.Serial('COM4', 115200)  # İkinci Arduino için

data = []

try:
    while True:
        if ser1.in_waiting > 0:
            line1 = ser1.readline().decode('utf-8').strip()
            print(f"Arduino 1: {line1}")
            if "Sinyal Gücü" in line1:
                rssi1 = int(line1.split(": ")[1].split(" ")[0])
                data.append({'arduino': 1, 'rssi': rssi1, 'timestamp': time.time()})
        
        if ser2.in_waiting > 0:
            line2 = ser2.readline().decode('utf-8').strip()
            print(f"Arduino 2: {line2}")
            if "Sinyal Gücü" in line2:
                rssi2 = int(line2.split(": ")[1].split(" ")[0])
                data.append({'arduino': 2, 'rssi': rssi2, 'timestamp': time.time()})
        
        time.sleep(1)

except KeyboardInterrupt:
    ser1.close()
    ser2.close()

    with open('wifi_signal_data.csv', 'w') as f:
        f.write('arduino,rssi,timestamp\n')
        for entry in data:
            f.write(f"{entry['arduino']},{entry['rssi']},{entry['timestamp']}\n")
