import Adafruit_DHT
from datetime import datetime
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        now = datetime.now()
        format_time = now.strftime("%d-%m-%Y %H:%M:%S")
        with open('/home/pi/projects/humidity-temp.log', 'a') as file:
            if humidity and temperature:
                file.write(f"{format_time} temperature={temperature:0.1f}*C  humidity={humidity:0.1f}%\n")
            else:
                file.write(f"{format_time} Failed to retrieve data from humidity sensor\n")
        time.sleep(300)


if __name__ == '__main__':
    main()
