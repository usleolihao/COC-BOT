import os, time, json, unittest
from HtmlTestRunner import HTMLTestRunner
from COC.Bot import COC_BOT
from COC.Donation import *
from COC.Harvest import *
from COC.Lrank import *
from COC.Ngtworld import *
from COC.Scenario import *
from COC.Upgrade import *

'''
test_dir = './COC'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="*.py")
'''

if __name__ == "__main__":
	'''
	TEST = lambda : HTMLTestRunner(combine_reports=True, report_name="test_report", add_timestamp=False).run(discover)

	mode
	'''
	device = "emulator-5554"
	config = {
	'donation': Donation(),
	'Lrank': Lrank()
	}
	bot = COC_BOT(device = device, config = config)
	bot.run()

