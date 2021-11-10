import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from commonClass import ErrorHandler
import testcase

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		service = Service("C:\Program Files (x86)\chromedriver.exe")
		self.driver = webdriver.Chrome(service=service)
		self.driver.maximize_window()

	def test_application(self):
		testScnario = testcase.TestCaseProcess(self.driver)
		testScnario.lp_purchase_process()

	def tearDown(self):
		ErrorHandler.assert_element()
		self.driver.close()

if __name__ == "__main__":
    unittest.main()