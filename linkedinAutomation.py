from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#-------------------------------
#   Created by Taner Sekmen
#-------------------------------

# email, password, login button and network button could change, please let me know if it is changed

def automation(location, website_page):
    # You have to give the chromedriver location and
    # the link of the web page you want to access as input value.
    browser = webdriver.Chrome(location)
    browser.get(website_page)
    browser.fullscreen_window()
    time.sleep(2)


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

    # js code. It benefits to scroll down 3 times.
    # you can change in range part.
    for i in range(1, 3):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(5)

    # Automation system will write when it see your network one by one.
    followers = browser.find_elements_by_class_name("mn-connection-card__details")
    followerList = []
    for follower in followers:
        followerList.append(follower.text)
    # It saves information in follower.txt
    with open("follower.txt", "w", encoding="UTF-8") as file:
        for follower in followerList:
            file.write(follower + "\n")

    time.sleep(10)

    # It will quit after it is done.
    browser.quit()



# For example:
# first my chromedriver location and website page
if __name__=='__main__':
    automation("/usr/bin/chromedriver","https://www.linkedin.com/")

