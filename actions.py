import logger
from logger import get_colored_text
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

def check_cart(driver,expected_cart):
    pass

def change_url(driver,url):
    try:
        driver.get(url)
        logger.Log.success(f"Changed Url to {get_colored_text(url, logger.bcolors.BOLD)}")
    except:
        logger.Log.error(f"Couldn't change Url to {get_colored_text(url, logger.bcolors.BOLD)}, timedout")

def click(driver : WebDriver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath).click()
    except:
        logger.Log.error(f"Couldn't click on {get_colored_text(xpath, logger.bcolors.BOLD)}")
actions_map = {
    "ChangeUrl" : change_url,
    "Click" : click,
    "CheckCart" : check_cart
}