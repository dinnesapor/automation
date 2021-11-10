import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from commonClass import ErrorHandler
import testcase

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		service = Service("C:\Program Files (x86)\chromedriver.exe")
		# webdriver.Chrome(service=service) | webdriver.Edge(service=service) | webdriver.Firefox(service=service) | webdriver.Safari(service=service)
		self.driver = webdriver.Chrome(service=service)
		self.driver.maximize_window()

	# add "test" prefix on any method names that contains the testcases script (e.g. test_application)
	def test_application(self):
		testScenario = testcase.TestCaseProcess(self.driver)
		testScenario.lp_purchase_process()

	# testcase 2
	def test_application_second(self):
		testScenario = testcase.TestCaseProcess(self.driver)
		testScenario.view_order_details()

	def tearDown(self):
		ErrorHandler.assert_element()
		self.driver.close()

if __name__ == "__main__":
    unittest.main()