#!/usr/bin/env python3
#coding: utf-8

import os
import subprocess 
import signal
import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator

OPENVPN_CONF='/home/ysance.local/r.carmona-hagelsteen/.config/vpn/ys-fw001-UDP4-1194-raphael.carmona-hagelsteen.ovpn'

'''
Icon UI
'''
def main():
	print('execute main')
	indicator = appindicator.Indicator.new("customtray", "semi-starred-symbolic", appindicator.IndicatorCategory.APPLICATION_STATUS)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(menu())
	gtk.main()


def menu():
	print('define menu')
	menu = gtk.Menu()
	
	print('instantiate process manager')
	vpn_process = VpnControler()
	
	activate_cmd = gtk.MenuItem('Activate')
	activate_cmd.connect('activate', vpn_process.activate)
	menu.append(activate_cmd)
	
	deactivate_cmd = gtk.MenuItem('Deactivate')
	deactivate_cmd.connect('activate', vpn_process.deactivate)
	menu.append(deactivate_cmd)
	
	status_cmd = gtk.MenuItem('Status')
	status_cmd.connect('activate', vpn_process.status)
	menu.append(status_cmd)
	
	separator = gtk.SeparatorMenuItem()
      menu.append(separator)
        
	exittray = gtk.MenuItem('Quit')
	exittray.connect('activate', quit)
	menu.append(exittray)	

	menu.show_all()
	return menu
	
	
def quit(_):
	gtk.main_quit()
	
'''
Process Management
'''	
class VpnControler:
	def __init__(self):

		self.activate_cmd = 'pkexec openvpn --config {}'.format(OPENVPN_CONF)
		self.deactivate_cmd = 'pkexec pkill -g {}'
		
	def activate(self, _):
		try:
			self.process = subprocess.Popen(self.activate_cmd, shell=True, start_new_session=True, stderr=subprocess.STDOUT, universal_newlines=True)		
			print('pid: ', self.process.pid)
			
		except SubprocessError as e:
			print('process crashed : ', e) 
	
	def deactivate(self, _):
		print(self.process.pid)
		print(self.process.poll())
		subprocess.call(self.deactivate_cmd.format(self.process.pid).split())
		print(self.process.poll())

	def status(self, _):
		print('pid : ', self.process.pid)
		print('exit status (None if still running) : ' , self.process.poll())

	
if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	main()
