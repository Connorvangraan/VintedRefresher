import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class VintedHandler:
    def __init__(self, username:str, password:str):
        url = "https://www.vinted.co.uk/"
        url = "https://www.vinted.co.uk/member/signup/select_type?ref_url=%2F"
        driver = webdriver.Edge()
        driver.get(url)
        element = driver.find_element(By.ID, "onetrust-reject-all-handler")
        element.click()

        time.sleep(1000)
        driver.close()

def main(user, passw):
    vh = VintedHandler(user, passw)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user = "bekah.justice11@gmail.com"
    passw = "StormTrooper321!"
    main(user, passw)

