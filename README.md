**Simple tray icon switch for openvpn**

Rely on openvpn CLI and Gtk.

*installation*

```
dpkg -i <openvpn-icon.deb> 
```

Install dependencies if needed with 
```
apt install -f
```

from Gtk dependencies see https://pygobject.readthedocs.io/en/latest/getting_started.html


*Run the app*

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
- :heavy_check_mark: daemon 
- improve ui with switch button
- logging


