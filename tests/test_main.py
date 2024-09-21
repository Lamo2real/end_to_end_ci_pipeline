from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_browser():
    """
    Sets up the Chrome WebDriver and returns the driver object.
    """
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver


def accept_cookies(driver):
    """
    Accepts cookies on the Google homepage.
    """
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "L2AGLb"))
        )
        accept_cookies_button.click()
    except Exception as e:
        print(f"Cookies acceptance failed: {e}")



def search_google(driver, query):
    """
    Performs a search on Google for the specified query.
    
    Args:
        driver: The WebDriver object used to interact with the browser.
        query (str): The search term to be entered into Google.
    """
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )
    search_box.clear()
    search_box.send_keys(query + Keys.ENTER)


def click_first_link(driver, link_text):
    """
    Clicks on the first link that partially matches the provided link text.
    
    Args:
        driver: The WebDriver object used to interact with the browser.
        link_text (str): The partial text of the link to click.
    """
    try:
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, link_text))
        )
        link.click()
    except Exception as e:
        print(f"Could not click on the link: {e}")


def test_run_test():
    """
    Orchestrates the end-to-end test: opens the browser, accepts cookies,
    performs a search, and clicks a link.
    """
    driver = None
    try:
        driver = setup_browser()
        driver.get("https://google.com")
        
        accept_cookies(driver)
        search_google(driver, "coffee")
        click_first_link(driver, "coffee")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        if driver:
            time.sleep(3)
            driver.quit()


if __name__ == "__main__":
    test_run_test()
