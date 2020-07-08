from selenium import webdriver
from time import sleep
from credientials import username, password

driver = webdriver.Chrome(executable_path="F:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element_by_xpath("//input[@name=\"username\"]") \
    .send_keys(username)
driver.find_element_by_xpath("//input[@name=\"password\"]") \
    .send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]') \
    .click()
sleep(4)
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
    .click()
sleep(3)
driver.find_element_by_xpath("//button[contains(text(), 'Turn On')]") \
    .click()
sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div") \
    .click()
sleep(3)

for i in range(250):
    driver.find_element_by_xpath('//button[text()="Follow"]') \
        .click()
    sleep(10)
