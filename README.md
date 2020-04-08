**Simple tray icon switch for openvpn**

Rely on openvpn CLI and Gtk.

**installation**

Install via pip, only python3 is supported :
```
python3 -m pip install git+https://github.com/carsteen/vpn_icon
```
for Gtk dependencies see https://pygobject.readthedocs.io/en/latest/getting_started.html

**Run the app**

```
python3 -m openvpn_icon /path/to/your/conf.ovpn
```

Your ovpn conf file should only contains absolute paths.

*credits*

openvpn_icon https://openvpn.net/
Gtk https://www.gtk.org/

*todo*

- :heavy_check_mark: icon creation/design
- :heavy_check_mark: vpn controler in python
- :heavy_check_mark: packaging
- :heavy_check_mark: create daemon
- improve ui
- logging
