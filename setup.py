#!/usr/bin/env python3

from setuptools import setup

setup(name = "openvpn-switch",
	version = "0.1.0",
	description = "Simple tray icon for controlling openvpn CLI",
	author = "Raphael Carmona-Hagelsteen",
	author_email = "uncorporation@gmail.com",
	url='https://github.com/carsteen/vpn_icon',
	scripts = ['openvpn_icon.py'],
	package_data={"data": ["*.desktop"]}
	)
