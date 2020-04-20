## openvpn-icon

Simple Ubuntu tray icon for activating and deactivating vpn conection with openvpn. Relies on openvpn cli and Gtk.

### Installation

<!-- 
* [openvpn-icon_0.1.0_all.deb](https://drive.google.com/uc?export=download&id=1neaPxDBnxzrPa8O3IcTB615T04_GviLO)
-->

Install downloaded package

```
dpkg -i <openvpn-icon.deb> 
```

Fix dependencies with 

```
apt install -f
```

### Use

Run the app providing your .ovpn config file.

```
openvpn-icon /path/to/your/conf.ovpn
```

### Make it launch at startup

Once installed, change path/to/conf in
```
sudo gedit /usr/share/applications/openvpn-icon.desktop
```

Copy to user applications 
```
sudo cp /usr/share/applications/openvpn-icon.desktop ~/.local/share/applications/
```

uncomment that line in ~/.local/share/applications/openvpn-icon.desktop
```
# X-GNOME-Autostart-enabled=false
```

### Credits

https://openvpn.net/  
https://www.gtk.org/


