import os, unittest
from datetime import date
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condition
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from commonClass import CommonExec
from selenium.webdriver.common.action_chains import ActionChains

class BasicEvent(object):

    def __init__(self, driver):
        self.driver = driver

    # set value for input text fields
    def set_text_value(self, obj):
        try:
            CommonExec.check_parameter(True, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )
            element.clear()
            element.send_keys(obj['value'])
        except:
            CommonExec.print_message(0, "input text value", obj)
        finally:
            CommonExec.print_message(1, "input text value", obj)

    # set value for input selection field
    def set_option_value(self, obj):
        try:
            CommonExec.check_parameter(False, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )
            element = Select(element)
            if obj.get('value') is None or obj.get('value') == '':
                element.select_by_index(1)
            else:
                element.select_by_value(obj['value'])
        except:
            CommonExec.print_message(0, "select option value", obj)
        finally:
            CommonExec.print_message(1, "select option value", obj)

    # select/click element
    def click_element(self, obj):
        try:
            CommonExec.check_parameter(False, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )
            element.click()
        except:
            CommonExec.print_message(0, "click element", obj)
        finally:
            CommonExec.print_message(1, "click element", obj)

    # mouse over
    def mouse_over_element(self, obj):
        try:
            action = ActionChains(self.driver) 
            CommonExec.check_parameter(False, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )
            action.move_to_element(element).perform()
        except:
            CommonExec.print_message(0, "Hover element", obj)
        finally:
            CommonExec.print_message(1, "Hover element", obj)

    # get inner text label
    def get_inner_text(self, obj):
        try:
            CommonExec.check_parameter(False, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )
            return element.text
        except:
            CommonExec.print_message(0, "get inner text", obj)
        finally:
            CommonExec.print_message(1, "get inner text", obj)

        return ""

    # get value by attribute
    def get_attribute_text(self, obj):
        try:
            CommonExec.check_parameter(False, obj)
            element = WebDriverWait(self.driver, CommonExec.element_wait_time).until(
                Condition.presence_of_element_located((CommonExec.get_selector(obj['selector']), obj['locator']))
            )

            # set default attribute to name
            if obj.get('attribute') is None or obj.get('attribute') == '':
                obj['attribute'] = "name"
            return element.get_attribute(obj['attribute'])
        except:
            CommonExec.print_message(0, "get attribute text", obj)
        finally:
            CommonExec.print_message(1, "get attribute text", obj)

        return ""

    # save page screenshot
    def get_screenshot(self, obj = {}):
        directory = CommonExec.prepare_dir_name(obj);
        obj['origin'] =  directory['file_path']

        try:
            if not os.path.exists(directory['base_path']):
                os.makedirs(directory['base_path'])
            if not os.path.exists(directory['file_path']):
                self.driver.save_screenshot(directory['file_path'])
        except:
            CommonExec.print_message(0, "get screenshot", obj)
        finally:
            CommonExec.print_message(1, "get screenshot", obj)

class AssertEvent(object):
    def __init__(self, driver):
        self.driver = driver
        self.tc = unittest.TestCase()

    # main assertion methods
    def statement(self, obj = {}):
        obj['log_status'] = True

        # halt process and raise error
        raise_error = obj['raise_error'] if obj.get('raise_error') is not None and not obj['raise_error'] else True;

        # assertion type
        assert_type = obj['operator'] if obj.get('operator') is not None else "equal";

        # option message
        option_message = obj['message'] if obj.get('message') is not None else "..."

        # defined assert parameters
        first_value = ""
        second_value = ""
        if obj.get('value') is not None:
            value_obj = obj['value']
            first_value = value_obj[0] if 0 < len(value_obj) else ""
            second_value = value_obj[1] if 1 < len(value_obj) else ""

        # execute assert method
        try:
            match assert_type:
                case "equal":
                    self.tc.assertEqual(first_value, second_value)
                case "not_equal":
                    self.tc.assertNotEqual(first_value, second_value)
                case "true":
                    print(assert_type)
                    self.tc.assertTrue(first_value)
                case "false":
                    self.tc.assertFalse(first_value, msg=None)
                case "is":
                    self.tc.assertIs(first_value, second_value)
                case "is_not":
                    self.tc.assertIsNot(first_value, second_value)
                case "is_none":
                    self.tc.assertIsNone(first_value)
                case "is_not_none":
                    self.tc.assertIsNotNone(first_value)
                case "in":
                    self.tc.assertIn(first_value, second_value)
                case "not_in":
                    self.tc.assertNotIn(first_value, second_value)
                case "is_instance":
                    self.tc.assertIsInstance(first_value, second_value)
                case "not_is_instance":
                    self.tc.assertNotIsInstance(first_value, second_value)
                case "almost_equal":
                    self.tc.assertAlmostEqual(first_value, second_value)
                case "not_almost_equal":
                    self.tc.assertNotAlmostEqual(first_value, second_value)
                case "greater":
                    self.tc.assertGreater(first_value, second_value)
                case "greater_equal":
                    self.tc.assertGreaterEqual(first_value, second_value)
                case "less":
                    self.tc.assertLess(first_value, second_value)
                case "less_equal":
                    self.tc.assertLessEqual(first_value, second_value)
                case "regex":
                    self.tc.assertRegex(first_value, second_value)
                case "not_regex":
                    self.tc.assertNotRegex(first_value, second_value)
                case "count_equal":
                    self.tc.assertCountEqual(first_value, second_value)
                case _:
                    self.tc.assertEqual(first_value, second_value)

            CommonExec.print_message(1, option_message, obj)

        except AssertionError as asserterror:
            CommonExec.print_message(0, option_message, obj)
            if raise_error:
                raise asserterror



