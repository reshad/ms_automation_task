import time
from common import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def select_plan_before_checkout(driver):
	plan_selector = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]')))
	
	walk_in_closet_plan = plan_selector.find_element_by_xpath('//li[1]')

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/ul/li[2]/div/div[1]/div/div[3]/button')))
	walk_in_closet_plan.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/ul/li[2]/div/div[1]/div/div[3]/button').click()

	bin_field = plan_selector.find_element_by_xpath("//input[@placeholder='0']")
	bin_field.send_keys('4')
	walk_in_closet_plan.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/ul/li[2]/div/div[2]/div/div[2]/button').click()

	walk_in_closet_plan.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div[1]/button').click()


def select_services_before_checkout(driver):
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'large-items')))
	
	driver.find_element_by_name('large-items').click()
	driver.find_element_by_name('bulky-items').click()
	driver.find_element_by_name('walk-up').click()
	driver.find_element_by_name('fragile-items').click()
	driver.find_element_by_name('disassembly').click()

	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/button').click() # Click Continue 

def provide_contact_information_in_checkout(driver, name, phone, email):
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'fullName')))

	driver.find_element_by_name('fullName').send_keys(name)
	driver.find_element_by_name('phone').send_keys(phone)
	driver.find_element_by_name('email').send_keys(email)
	driver.find_element_by_xpath("//label[@for='radio-isMilitary-_no']").click()

	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[1]/div[2]/form/button').click() # Click Continue 

def provide_appointment_address_in_checkout(driver, address, floor):
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'address_pretty')))

	driver.find_element_by_name('address_pretty').send_keys(address)
	time.sleep(3)
	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[2]/div[2]/form/div[1]/ul/li[1]').click()
	driver.find_element_by_xpath('//input[@placeholder="Optional"]').send_keys(floor)
	driver.find_element_by_xpath('//button[@data-testid="address-form-submit-button"]').click()


def provide_appointment_date_and_time_in_checkout(driver):
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@placeholder="mm/dd/yyyy"]')))

	datefield = driver.find_element_by_xpath('//div[@placeholder="mm/dd/yyyy"]')
	datefield.click()
	# TODO: need to find a proper locator to pick available date
	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div/div[1]/div[2]/div[6]/div[3]').click()

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'Time')))
	
	timefield = driver.find_element_by_name('Time')
	timefield.click()
	time.sleep(2)
	# TODO: need to find a proper locator to pick available time slots
	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[26]/div').click()
	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/div[3]/div[2]/button').click()

def provide_billing_in_checkout(driver, cc_number, cc_expire_date, cc_cvc, fullName):
	iframe = driver.find_element_by_xpath('//iframe[@title="Secure card number input frame"]')
	driver.switch_to.frame(iframe)
	driver.find_element_by_name('cardnumber').send_keys(cc_number)
	driver.switch_to.default_content()

	iframe = driver.find_element_by_xpath('//iframe[@title="Secure expiration date input frame"]')
	driver.switch_to.frame(iframe)
	driver.find_element_by_name('exp-date').send_keys(cc_expire_date)
	driver.switch_to.default_content()

	iframe = driver.find_element_by_xpath('//iframe[@title="Secure CVC input frame"]')
	driver.switch_to.frame(iframe)
	driver.find_element_by_name('cvc').send_keys(cc_cvc)
	driver.switch_to.default_content()

def agree_and_confirm_in_checkout(driver):
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="agrees-to-tos-checkbox"]')))

	driver.find_element_by_xpath('//label[@for="agrees-to-tos-checkbox"]').click()

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/button')))
	driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div/div[1]/button').click()

	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'js-skip')))
	driver.find_element_by_id('js-skip').click()

	









