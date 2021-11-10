import time
from element import *
from commonClass import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

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
		
		# element checking time
		CommonExec.element_wait_time = 5

		# easybuy_value
		self.baseEvent.set_option_value({
			"selector":"id",
			"locator":"easybuy_value",
			"log_status": True
		})

		# item_num
		self.baseEvent.set_option_value({
			"selector":"id",
			"locator":"item_num",
			"value":"5",
			"time_delay": 1,
			"log_status": True
		})

		# family_name
		self.baseEvent.set_text_value({
			"selector":"css",
			"locator":"input[name=family_name]",
			"value":"フリガナ",
			"log_status": True
		})

		# given_name
		self.baseEvent.set_text_value({
			"selector":"css",
			"locator":"input[name=given_name]",
			"value":"フリガナ",
			"log_status": True
		})

		# family_name_kana
		self.baseEvent.set_text_value({
			"selector":"css",
			"locator":"input[name=family_name_kana]",
			"value":"フリガナ",
			"log_status": True
		})

		# given_name_kana
		self.baseEvent.set_text_value({
			"selector":"css",
			"locator":"input[name=given_name_kana]",
			"value":"フリガナ",
			"log_status": True
		})

		# postal_code
		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"postal_code",
			"value":"1100001",
			"log_status": True
		})

		# add_btn
		self.baseEvent.click_element({
			"selector":"id",
			"locator":"add_btn",
			"log_status": True,
			"time_delay": 1
		})

		# address2
		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"address2",
			"value":"0",
			"log_status": True
		})

		# tel
		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"tel",
			"value":"09000321238",
			"log_status": True
		})

		# email
		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"email",
			"value":"samurai.cart.test@email.com",
			"log_status": True
		})

		# payment method
		self.baseEvent.click_element({
			"selector":"id",
			"locator":"pym2",
			"log_status": True
		})

		# gender
		self.baseEvent.click_element({
			"selector":"id",
			"locator":"man",
			"log_status": True
		})

		# birth_year
		self.baseEvent.set_option_value({
			"selector":"name",
			"locator":"birth_year",
			"value":"2000",
			"log_status": True
		})

		# birth_month
		self.baseEvent.set_option_value({
			"selector":"name",
			"locator":"birth_month",
			"value":"01",
			"log_status": True
		})

		# birth_day
		self.baseEvent.set_option_value({
			"selector":"name",
			"locator":"birth_day",
			"value":"21",
			"log_status": True
		})

		# generate input form screenshot
		self.baseEvent.get_screenshot({
			"path": "test",
			"filename": "LP-TEST-SCREEN-FORM.png",
			"log_status": True
		})

		# confirm
		self.baseEvent.click_element({
			"selector":"id",
			"locator":"sub",
			"time_delay": 2
		})

		# confirmation page scree

		# get the phone number displayed
		my_phone_number = self.baseEvent.get_inner_text({
			"selector":"xpath",
			"locator":'//*[@id="content"]/form/div[1]/div[3]/table/tbody/tr[3]/td[2]',
			"log_status": True
		})

		# get the phone number displayed
		my_email = self.baseEvent.get_inner_text({
			"selector":"xpath",
			"locator":'//*[@id="content"]/form/div[1]/div[4]/table/tbody/tr[1]/td[2]',
			"log_status": True
		})

		# check if the phone number provided was displayed correctly
		self.assertEvent.statement({
			"operator" : "equal",
			"value": [my_phone_number, "09000321238"],
			"message":"Phone number was displayed correctly",
			"raise_error" : False
		})

		# check if the email provided was displayed correctly
		self.assertEvent.statement({
			"operator" : "equal",
			"value": [my_email, "samurai.cart.test@email.com"],
			"message":"Phone number was displayed correctly",
			"raise_error" : False
		})

		# generate confirmation page screenshot
		self.baseEvent.get_screenshot({
			"path": "test",
			"filename": "LP-TEST-SCREEN-COMFIRM.png",
			"log_status": True
		})

		# submit puchase
		self.baseEvent.click_element({
			"selector":"name",
			"locator":"keep_submit",
			"time_delay": 2
		})

		# generate completion page screenshot
		self.baseEvent.get_screenshot({
			"path": "test",
			"filename": "LP-TEST-SCREEN-COMPLETE.png",
			"log_status": True
		})

		# purchase form
		self.baseEvent.click_element({
			"selector":"link_text",
			"locator":"トップページへ戻る>>",
			"time_delay": 2,
			"log_status": True
		})