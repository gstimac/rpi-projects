#!/usr/bin/env python3

import sys
import pigpio
import DHT
import time
import datetime

pin = 4
sensor = DHT.DHTAUTO

def output_data(timestamp, temperature, humidity):
    # Sample output Date: 2019-11-17T10:55:08, Temperature: 25°C, Humidity: 72%
    date = datetime.datetime.fromtimestamp(timestamp).replace(microsecond=0).isoformat()
    output = u"Date: {:s}, Temperature: {:g}\u00b0C, Humidity: {:g}%\n".format(date, temperature, humidity)
    print(output)
    with open('./humidity-temp.log', 'a') as file:
        file.write(output)
while True:
    pi = pigpio.pi()
    if not pi.connected:
        continue
  
    s = DHT.sensor(pi, pin, model = sensor)
    
    tries = 5   # try 5 times if error
    while tries:
        try:
            timestamp, gpio, status, temperature, humidity = s.read()   #read DHT device
            if(status == DHT.DHT_TIMEOUT):  # no response from sensor
                continue
            if(status == DHT.DHT_GOOD):
                output_data(timestamp, temperature, humidity)
                tries = 0
                continue
            time.sleep(5)
            tries -=1
        except KeyboardInterrupt:
            break
    
    time.sleep(10) 
