from selenium import webdriver
from datetime import date
import time

web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSevs0OMEJAmnybXuqiUCpaSGJigaPUaQzISWkBct2sXi3E9Yw/viewform?fbzx=2146169304140704904")

time.sleep(1)

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Next.click()

EmployeeID = "377686"
id = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
id.send_keys(EmployeeID)

LastName = "Rubio Fernandez"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = "Francisco"
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

today = date.today().strftime("%m/%d/%Y")
print("Today's date:", today)