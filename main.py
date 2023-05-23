import random
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Key

class VintedHandler:
    def __init__(self, username:str, password:str):
        url = "https://www.vinted.co.uk/"
        url = "https://www.vinted.co.uk/member/signup/select_type?ref_url=%2F"
        driver = webdriver.Edge()
        driver.get(url)
        self.random_halt()

        element = driver.find_element(By.ID, "onetrust-reject-all-handler")
        element.click()
        self.random_halt()

        # u-cursor-pointer
        buttons = driver.find_elements(By.CLASS_NAME, "u-cursor-pointer")
        login_button = buttons[1]
        login_button.click()
        self.random_halt()

        buttons = driver.find_elements(By.CLASS_NAME, "u-cursor-pointer")
        email_button = buttons[0]
        email_button.click()
        self.random_halt()

        fields = driver.find_elements(By.CLASS_NAME, "web_ui__Input__value")
        username_field = fields[0]
        username_field.send_keys(username)
        self.random_halt()

        password_field = fields[1]
        password_field.send_keys(password)
        self.random_halt()
        #password_field.submit()

        #password_field.send_keys(password)
        # time.sleep(1000)
        # buttons = driver.find_elements(By.TAG_NAME, 'button')
        # for b in buttons:
        #     print(b.text)
        #     print(b.id)
        #     print(b.accessible_name)
        #     print(b.tag_name)
        #     print()
        #
        # continue_button = list(filter(lambda x: x.text == "Continue", buttons))
        # print(continue_button)
        # continue_button = continue_button[0]
        # continue_button.click()
        #
        # wait = WebDriverWait(driver, 10)
        time.sleep(1000)
        driver.close()

    def random_halt(self):
        time.sleep(random.random()+3)

def main(user, passw):
    vh = VintedHandler(user, passw)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user = "bekah.justice11@gmail.com"
    passw = "StormTrooper321!"
    main(user, passw)

