from selenium import webdriver
import time

def logintolinkedin():
	myemail='rajeevkumar25@gmail.com'
	mypassword='rajeev25'

	chromedriver=webdriver.Chrome('C:\Rajeev\Projects\Python\Practice\Python\chromedriver.exe')
	url='https://www.linkedin.com/uas/login'
	chromedriver.get(url)
	#print(chromedriver.page_source)
	#time.sleep(10)
	login_email=chromedriver.find_element_by_xpath('//*[@id="session_key-login"]')
	login_email.send_keys(myemail)

	login_pass.=chromedriver.find_elements_by_xpath('//*[@id="session_password-login"]')
	login_pass.send_keys(mypassword)


	click_login_button=chromedriver.find_element_by_xpath('//*[@id="btn-primary"]')
	click_login_button.click()

	time.sleep(10)
	chromedriver.quit()


logintolinkedin()