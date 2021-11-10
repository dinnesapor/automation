import time,sys,os
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition

class ErrorHandler(object):
	error_occured = False
	error_log_string = []
	general_log_string = []

	# verify testcase status
	def assert_element():
		ErrorHandler.create_log_file()
		assert not ErrorHandler.error_occured, "An error occured when defining page element"

	# create testcase log file
	def create_log_file():
		base_path 			= "logs/{}".format(date.today())
		filename 			= time.strftime("%H%M%S", time.localtime()) + ".txt"
		file_path 			= base_path + "/" + filename

		if not os.path.exists(base_path):
		    os.makedirs(base_path)

		if not os.path.exists(file_path):
			with open(file_path, 'w') as log:
				log.write("Date: {} {}". format(date.today(), time.strftime("%H:%M:%S", time.localtime())))
				log.write("\nTestcase Status: {}". format(("PASSED" if not ErrorHandler.error_occured else "FAILED")))
				log.write("\n\nLog Details:")
				for log_details in ErrorHandler.general_log_string:
					log.write("\n{}".format(log_details))

class CommonExec(object):

	# web drive element checking time
	element_wait_time = 10

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

		ErrorHandler.general_log_string.append("{} >>> {}".format(("Passed" if status == 1 else "Failed"), support_message))

		if status == 1:
			if allow_print:
				if support_message not in ErrorHandler.error_log_string:
					print("\033[32m" + "Passed" + "\033[37m" + "\t: {}".format(support_message.encode('utf-8')))
		else:
			if allow_print:
				print("\033[31m" + "Failed" + "\033[37m" + "\t: {}".format(support_message.encode('utf-8')))

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