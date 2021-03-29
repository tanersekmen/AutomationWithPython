from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#-------------------------------
#   Created by Taner Sekmen
#-------------------------------


# I download the chromedriver that I used. My operating system Linux/Ubuntu
browser = webdriver.Chrome("/usr/bin/chromedriver")

# I want to pull data from linkedin.
# When linkedin page open, it will be full screen
# and it will wait 2 seconds.
browser.get("https://www.linkedin.com/")
browser.fullscreen_window()
time.sleep(2)

# It will click login button
login = browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(5)

# First it will find email and password location and enters the values that you given
# You can acces your linkedin account with your email and password. I passed that area.
email = browser.find_element_by_xpath("//*[@id='username']")
password = browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("your mail")
password.send_keys("your password")

# It click login button after you fill your email and password information
login_buton = browser.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
login_buton.click()
time.sleep(7)

# When the page opens, click on the my networks tab
contact = browser.find_element_by_xpath("//*[@id='ember30']")
contact.click()
time.sleep(7)

contact_second = browser.find_element_by_class_name("mn-community-summary__entity-info")
contact_second.click()
time.sleep(5)

#
# js code to scroll down little bit.
for i in range(1,3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)

# Automation system will write when it see your network one by one.
followers = browser.find_elements_by_class_name("mn-connection-card__details")
followerList = []
for follower in followers:
    followerList.append(follower.text)
# It saves information in follower.txt
with open("follower.txt", "w", encoding = "UTF-8" ) as file:
    for follower in followerList:
        file.write(follower + "\n")

time.sleep(10)

# It will quit after it is done.
browser.quit()
