## `openvpn-icon`

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

### Credits

https://openvpn.net/  
https://www.gtk.org/


