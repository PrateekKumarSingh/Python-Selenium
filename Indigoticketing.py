from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://goindigo.in/")
driver.maximize_window()
# driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[@href='javascript:void(0)'][@class='close-cookie']").click()
b = driver.find_element_by_xpath("//input[@class='or-mob-src airport-city-field form-control']")
b = driver.find_element_by_xpath("//input[@class='form-control or-src-city']")
print(b)
b.click()
c=driver.find_element_by_xpath("//div[@class='airport-code'][contains(text(), 'CCU')]")
c.click()

driver.find_element_by_xpath('//*[@id="bookFlightTab"]/form/div[3]/div[1]/div[2]/div/div/input').send_keys("LKO")
driver.find_element_by_xpath('//*[@id="bookFlightTab"]/form/div[3]/div[1]/div[2]/div/div/input').send_keys(Keys.ENTER)

# .click()
# driver.find_element_by_xpath('//*[@id="bookFlightTab"]/form/div[3]/div[1]/div[2]/div/div/input').submit()

# driver.find_element_by_xpath('//*[@id="orDestModal"]/div/div/div[2]/div/div/div/div/div/div[7]').send_keys("LKO")
# driver.find_element_by_xpath('//*[@id="orDestModal"]/div/div/div[2]/div/div/div/div/div/div[7]').submit()
