import Adafruit_DHT, time
from datetime import datetime

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    now = datetime.now()
    with open('humidity-temp.log', 'a') as file:
        if humidity is not None and temperature is not None:
            file.write(f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second} "
            f"temperature={temperature:0.1f}*C  humidity={humidity:0.1f}%\n")
        else:
            file.write(f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second} "
            f"Failed to retrieve data from humidity sensor\n")
    time.sleep(30)
