### openvpn-icon

Simple ubuntu tray icon for openvpn allowing to activate and deactivate vpn conection. It Relies on openvpn cli and Gtk.

*installation*

download package

* [openvpn-icon_0.1.0_all.deb](https://drive.google.com/uc?export=download&id=1neaPxDBnxzrPa8O3IcTB615T04_GviLO)

```
dpkg -i <openvpn-icon.deb> 
```

Install dependencies with 

```
apt install -f
```

Run the app providing your .ovpn config file.

```
openvpn-icon /path/to/your/conf.ovpn
```

*credits*

https://openvpn.net/  
https://www.gtk.org/

*todo*

- :heavy_check_mark: icon creation/design
- :heavy_check_mark: vpn controler in python
- :heavy_check_mark: packaging
- improve ui with switch button
- logging


