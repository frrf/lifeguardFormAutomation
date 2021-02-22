from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date
from data import EmployeeID,LastName,FirstName
import time

web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSeO73qZVWozM0G717mgEKRIxevYwId7bOMIHS3AD4kayQyURg/viewform")

time.sleep(1)

Next = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Next.click()

id = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
id.send_keys(EmployeeID)

last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

# Date
DateToday = date.today().strftime("%m/%d/%Y")
datePicker = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
datePicker.send_keys(DateToday)

# Facility
facilityDrop = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]/div[1]')
facilityDrop.click()
time.sleep(1)
# Algin Sutton
facilitySelect = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[4]')
facilitySelect.click()
time.sleep(1)

# Time of Arrival on Site
ArrivalTimeHour = "07"
arrivalHour = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
arrivalHour.send_keys(ArrivalTimeHour)

ArrivalTimeMin = "00"
arrivalMin = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
arrivalMin.send_keys(ArrivalTimeMin)

# Submit
submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
submit.click()

# Confirmation

get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
print(get_confirmation_div_text)

if((get_confirmation_div_text.text) == 'Thank you for completing the form.'):
  print("Test Was Successfull")
else:
  print("Test Was Not Successful")