### Using systemd to autostart the script on Raspberry Pi

#### 1. 
Place the configuration files [`DHT22.service`,`pigpiod.service`] into `/etc/systemd/system/`

#### 2. 
Inform the system

```
systemctl daemon-reload
systemctl enable DHT22.service
systemctl enable pigpiod
```

#### handy systemd commands

`systemctl status|start|stop|restart DHT22`

`journalctl -xn` 

### Resources
- https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
- https://www.thedigitalpictureframe.com/ultimate-guide-systemd-autostart-scripts-raspberry-pi/
- https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
- https://abyz.me.uk/rpi/pigpio/
