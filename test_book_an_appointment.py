import unittest, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from common import *
from checkout import *


class TestAppointmentBooking(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.delete_all_cookies()
		cls.driver.maximize_window()
		cls.driver.get(BASE_URL)
	
	def test_book_appointment(self):
		zip_code = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Zip Code']")))
		zip_code.send_keys(Test_Zip_Code)
		zip_code.send_keys(Keys.RETURN)
		time.sleep(5)

		select_plan_before_checkout(self.driver)
		time.sleep(3)

		select_services_before_checkout(self.driver)
		time.sleep(3)

		provide_contact_information_in_checkout(self.driver, Test_Full_Name, Test_Phone_number, Test_Email)
		time.sleep(2)

		provide_appointment_address_in_checkout(self.driver, Test_Address, Test_Floor)
		time.sleep(20)

		provide_appointment_date_and_time_in_checkout(self.driver)
		time.sleep(2)

		provide_billing_in_checkout(self.driver, Test_CC_Number, Test_CC_Expiration_Date, Test_CC_CVC, Test_Full_Name)
		time.sleep(2)

		agree_and_confirm_in_checkout(self.driver)
		time.sleep(10)

		# Asserts the appointment has a Date.
		# This can be improved when we know specifically we want to check on the appointment date
		appointment_date = self.driver.find_element_by_class_name('dashboard-appointment-date')
		print(appointment_date.text) # this is for debuging purpose
		assert appointment_date.is_displayed()

		# Asserts a new Navigation State, 
		# This can be improved when we know specifically we want to check from the navigation state
		print(self.driver.current_url) # this is for debuging purpose
		assert BASE_URL in self.driver.current_url

	@classmethod
	def tearDownClass(cls):
		print('>>>>>> Finished booking and appointment test cases <<<<<<')
		cls.driver.quit()


if __name__ == '__main__':
	unittest.main()

