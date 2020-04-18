#!/usr/bin/env python3

from setuptools import setup

data_files = [
	('share/applications', ['data/desktop/openvpn-icon.desktop']),
	('share/icons/ubuntu-mono-dark/status/22/openvpn-icon-panel.svg', ['data/icons/ubuntu-mono-dark/status/22/openvpn-icon-panel.svg'])]

setup(name = "openvpn-icon",
	version = "0.1.0",
	description = "Simple tray icon for controlling openvpn CLI",
	author = "Raphael Carmona-Hagelsteen",
	author_email = "uncorporation@gmail.com",
	url='https://github.com/carsteen/vpn_icon',
	scripts = ['openvpn-icon'],
	data_files=data_files
	)
