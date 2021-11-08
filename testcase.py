import time
from element import *
from commonClass import *
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseEvent = BasicEvent(self.driver)
        self.assertEvent = AssertEvent(self.driver)

class TestCaseProcess(BasePage):

	# perform purchase action in LP Screen
	def lp_purchase_process(self):
		# target page
		self.driver.get("https://v2off55itlab05.web-store.jp/product-buy-form/LP-TEST-SCREEN")
		driver = self.driver