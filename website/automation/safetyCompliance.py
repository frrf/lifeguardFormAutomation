from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date
from data import EmployeeID,LastName,FirstName, PhoneNumber,RecStaff
import time

web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSewGHNBEI09X3VQxkTD5Fkm4qwXL0pi3tXykTqpczJ9Lim2WA/formResponse")

time.sleep(1)

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Next.click()

safetyTime = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label')
safetyTime.click()

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Next.click()

sentHome = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
sentHome.click()

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Next.click()

enterID1 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
enterID1.send_keys(EmployeeID)

enterID2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
enterID2.send_keys(EmployeeID)

LastName = "Rubio Fernandez"
last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = "Francisco"
first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

phone = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone.send_keys(PhoneNumber)

# Facility
facilityDrop = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div')
facilityDrop.click()
time.sleep(1)
# Algin Sutton
facilitySelect = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[4]')
facilitySelect.click()
time.sleep(1)


rec = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
rec.send_keys(RecStaff)

wearPPE = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div/span/div/div[1]/label')
wearPPE.click()

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Next.click()

socialDist = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label')
socialDist.click()

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Next.click()

faceCover = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label')
faceCover.click()

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Next.click()

Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
Submit.click()

# Confirmation

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(get_confirmation_div_text)

if((get_confirmation_div_text.text) == 'Thank you for completing the form.'):
  print("Test Was Successfull")
else:
  print("Test Was Not Successful")