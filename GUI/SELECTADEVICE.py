#!/usr/bin/python3
import tkinter as tk # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
import os
from tkinter import messagebox
from util import *
from GUI.GUI_utils import *

class DEVICE(tk.Frame):

	def __init__(self, config, *args, **kwargs):
		self.config = config

		# ADB find connect devices
		self.devices = self.get_devices()

		n = len(self.devices)

		#check if emu connected adb
		if n < 2:
			self.connect_adb()
			ss(5)

		if not n > 0:
			messagebox.showinfo("Didn't find a device", "Please enable the development mode for Android \n or using an emulator")
			exit()

		elif n == 1:
			self.config['device'] =  self.devices[0]
		
		else:
			self.window = tk.Tk()
			tk.Frame.__init__(self, self.window, *args, **kwargs)
			self.select_GUI(n)
			
	

	def connect_adb(self):
		if 'emu' not in self.config.keys():
			messagebox.showinfo("Didn't find a device", "Please enable the development mode for Android \n or using an emulator")
			exit()

		emu = self.config['emu'][:-1]
		num = int(self.config['emu'][-1])

		ports = {
				"夜神" : 62001
				}

		addon_base = {
				"夜神" : 23
		}

		addons = {
				"夜神" : 1
		}

		try:
			port = ports[emu]
		
		except Exception as e:
			raise e
			messagebox.showinfo("Error Can not connect to ADB", "Emu is not support")


		port_addon = 0
		if num > 1:
			port_addon += addon_base[emu]
		port_addon += (num - 1) * addons[emu]


		device_name = '127.0.0.1:' + str(port + port_addon)



		if len(self.devices) == 0 or \
			(len(self.devices) == 1 and self.devices[0] != device_name):
			connect = 'adb\\adb connect ' + device_name
			#print( connect  )
			os.system(connect)

		
	def get_devices(self):
		#restart = 'adb/adb kill-server && adb/adb start-server'
		#os.system(restart)

		get_devices = 'adb\\adb devices'
		stream = os.popen(get_devices)

		devices_adb = stream.read()
		#devices_adb = devices_adb.decode("utf-8")
		devices_adb = devices_adb.replace("List of devices attached","")
		devices_adb = devices_adb.strip().split()

		#port=os.system('netstat -aon|findstr "555"')#25端口号
		#out=os.system('tasklist|findstr "3316"')#3316进是程

		print("Found Device:")
		devices = list()
		for i in range(0,len(devices_adb),2):
			if devices_adb[i + 1] != "offline":
				devices.append( devices_adb[i] )
				print(devices_adb[i])

		return devices

	def select_GUI(self,n):
		def set_devices(i):
				self.window.destroy()
				self.config['device'] =  self.devices[i]

		#--------------------Windows-----------------------------------------
		self.window.title("Select A Devices")
		self.window.resizable(width = False, height = False)
		self.window.grid_columnconfigure(0, weight=1)

		for i in range(n):
			tk.Button(self.window, text = self.devices[i] ,anchor = "center" ,
			 command = lambda id=i:set_devices(id) ).grid(row=i,column=0, sticky='nesw')
			
		self.window.geometry("300x" + str(n*30))
		set_close(self.window)
		self.window.mainloop()