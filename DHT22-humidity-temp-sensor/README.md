### Using systemd to autostart the script on Raspberry Pi

#### 1. 
Place the configuration file [`humidity-temp-sensor.service`] into `/etc/systemd/system/`

Or run `nano/etc/systemd/system/humidity-temp-sensor.service` and copy&paste the file content.

#### 2. 
Inform the system

```
systemctl daemon-reload
systemctl enable service_name
```

#### 3.
Reboot your Raspberry Pi

#### handy systemd commands

`systemctl status|start|stop|restart service_name`

`journalctl -u service_name` > show log

### Resources
- https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/
- https://www.thedigitalpictureframe.com/ultimate-guide-systemd-autostart-scripts-raspberry-pi/
- https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
