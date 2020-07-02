## import packages
from selenium.webdriver import Firefox
import time 
import datetime
import locale
locale.setlocale(locale.LC_TIME, "de_DE")

# Firefox browser required. 
browser = Firefox()
browser.get('https://intern.sport.uni-goettingen.de/fizdb/index.php?r=login/login')

#Fill in the login form

username = browser.find_element_by_id('id')
username.send_keys('aqibrahimbt@gmail.com')# enter email address
password = browser.find_element_by_name('pass') 
password.send_keys('') # password
submit_button = browser.find_element_by_name('submit')
submit_button.click()

tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
time.sleep(3) # required to delay the running of the script when login completed. 

# Gym opens on weekdays from 7am and at 8:45 on weekends
if tomorrow.weekday() < 5:
    time_slot = '7:00 Uhr'
else:
    time_slot = '8:45 Uhr'


main_div = browser.find_elements_by_xpath("//div[contains(@class, 'row') and contains(@class, 'kachel')]")

sub_div = []
for div in main_div:
    sub_div =  div.find_element_by_xpath(".//div[contains(@class, 'col-5')]")
    try:
        date_div = sub_div.find_element_by_xpath(".//div[contains(text(), '{}')]".format(tomorrow.strftime('%a %d. %b %Y'))) 
        time_div = sub_div.find_element_by_xpath(".//div[contains(text(), '{}')]".format(time_slot))
        button_div = sub_div.find_element_by_xpath('./following-sibling::div')
        submit_button = button_div.find_element_by_xpath("//button[text()='Anmelden']")
        submit_button.click()
    except:
        pass