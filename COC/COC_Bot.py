import threading,os

from tkinter import messagebox
from util import *
from CONSTANT import *
from GUI.GUI_logs import *

from COC.Func.Others import Utils as u
from COC.Func.General import General

#模拟器分辨需求为 860x732 dpi 160
class COC_BOT():

	def __init__(self,config,lang,frame):

		self._error = 0
		self._config = config
		self._lang = lang
		self._gui = frame
		self.d = self._config['d']

		prt(self._config,title = "配置信息")
		u.prt("机器信息",self.d.info)

		self._app = config['game']
		self._count = dict()

	def run(self):
		#配置
		while True:
			#如果是果盘COC 点进入游戏
			self.GPstart()

			#打印统计
			#prt(self._count,title = "统计")
			#ss(10,1, precent = 2)


	def Launch_app(self):
		self.d.app_start(self._app)

	def Stop_app(d):
		self.d.app_stop(self._app)

	def GPstart(self):
		EXISTS = lambda a,b: self.d(text=a, className=b).exists()
		CLICK = lambda a,b: self.d(text=a, className=b).click()
		#Watcher = lambda a,b:self.d.xpath("//*[@text="+ a +"]/../" + b).click()
		activity = u.current_act(self.d)
		
		if self._app == 'com.supercell.clashofclans.guopan' \
		and activity == 'com.flamingo.sdk.view.PluginActivity':
			try:
				if EXISTS("登录",TEXTVIEW):
					CLICK("登录",TEXTVIEW)
					ss(1)
				if EXISTS("进入游戏",TEXTVIEW):
					CLICK("进入游戏",TEXTVIEW)
					if '果盘进入' in self._count:
						self._count['果盘进入'] += 1
						u.prt("果盘游戏进入次数: ",self._count['果盘进入'])
					else:
						self._count['果盘进入'] = 1 
					ss(1)
					u.tap(self.d,1,1,r = True)
				#Watcher("添加小号",TEXTVIEW)
			except Exception as e:
				ss(30,1)

		



		