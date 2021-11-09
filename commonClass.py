import time,sys
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

class ErrorHandler(object):
	error_occured = False
	error_log_string = []
	def assert_element(error_occured):
		assert not error_occured, "An error occured when defining page element"

class CommonExec(object):

	# Specify element selector
	def get_selector(selector):
		default_selector = By.NAME

		if selector == 'css':
			default_selector = By.CSS_SELECTOR

		elif selector == 'id':
			default_selector = By.ID

		elif selector == 'class_name':
			default_selector = By.CLASS_NAME

		elif selector == 'xpath':
			default_selector = By.XPATH

		elif selector == 'link_text':
			default_selector = By.LINK_TEXT

		return default_selector

	# check basic parameters
	def check_parameter(input, obj_param):
		# primary parameters validation
		if obj_param.get('selector') is None or obj_param.get('selector') == '':
			sys.exit("\n\nERROR: parameter [selector] was not set or is empty.")

		elif obj_param.get('locator') is None or obj_param.get('locator') == '':
			sys.exit("\n\nERROR: parameter [locator] was not set or is empty.")

		elif obj_param.get('value') is None or obj_param.get('value') == '':
			if input :
				sys.exit("\n\nERROR: parameter [value] was not set or is empty.")

		# execute time delay
		if 'time_delay' in obj_param:
			time.sleep(int(obj_param['time_delay']))

	# print default log
	def print_message(status, text, obj_param = {}):
		origin = ""
		if obj_param.get('locator') is not None and obj_param.get('locator') != '':
			origin = "| " + obj_param.get('locator')
		elif obj_param.get('origin') is not None and obj_param.get('origin') != '':
			origin = "| " + obj_param.get('origin')

		allow_print = False
		if obj_param.get('log_status') is not None and obj_param.get('log_status'):
			allow_print = obj_param.get('log_status')

		support_message = "{} {}".format(text, origin)
		if allow_print:

			if status == 1 and allow_print:
				if support_message not in ErrorHandler.error_log_string:
					print("\033[32m" + "OK" + "\033[37m" + "\t: {}".format(support_message))

			else:
				print("\033[31m" + "FAIL" + "\033[37m" + "\t: {}".format(support_message))
				ErrorHandler.error_log_string.append(support_message)

				if not ErrorHandler.error_occured:
					ErrorHandler.error_occured = True

	# contruct file directory path/name
	def prepare_dir_name(obj_param):
		default_path 		= date.today()
		default_filename 	= time.strftime("%H-%M-%S", time.localtime())
		base_path 			= "capture/"+ (obj_param['path'] if (obj_param.get('path') is not None and obj_param.get('path') != '')  else default_path)
		filename 			= obj_param['filename'] if (obj_param.get('filename') is not None and obj_param.get('filename') != '') else default_filename + ".png"
		file_path 			= base_path + "/" + filename
		return {"file_path":file_path, "base_path":base_path, "base_file":filename}