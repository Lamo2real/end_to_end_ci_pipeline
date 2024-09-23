
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def setup_driver():
    """Set up the Chrome WebDriver and return the driver object."""
    
    the_service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=the_service)
    return driver




def open_website(driver, url):
    """Open the website using the driver and wait for it to load."""
    
    return driver.get(url)




def accept_cookies(driver):
    """Accept cookies by clicking the button with class 'fc-button-label'."""
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-button-label"))
    )
    cookie_button = driver.find_element(By.CLASS_NAME, "fc-button-label")
    cookie_button.click()




def select_language(driver):
    """Select English language for the game."""
    
    language_button_id = "langSelect-EN"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, language_button_id))
    )
    language_button = driver.find_element(By.ID, language_button_id)
    language_button.click()
    
    
    

def click_cookie_and_buy_products(driver):
    """Continuously click the cookie and buy available products"""
    
    cookie_id = "cookies"
    big_cookie_id = "bigCookie"
    product_price_prefix = "productPrice"
    product_prefix = "product"

    # Wait for cookie and game elements to load
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, big_cookie_id)))
    click_cookie = driver.find_element(By.ID, big_cookie_id)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, cookie_id)))
    cookie_count_elem = driver.find_element(By.ID, cookie_id)

    while True:
        # Click the big cookie
        click_cookie.click()

        # Get current cookie count
        cookie_count = int(cookie_count_elem.text.split(" ")[0].replace(",", ""))
        print(cookie_count)

        # Check if we can buy products
        for i in range(10):  # i am not gonna let it run over 3 let alone 10 hahaha
            product_price_text = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
            if not product_price_text.isdigit():
                continue

            product_price = int(product_price_text)
            if cookie_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click() 
                break

def main():
    """
    Main function to execute the script.
    """
    driver = setup_driver()
    open_website(driver, "https://orteil.dashnet.org/cookieclicker/")
    accept_cookies(driver)
    select_language(driver)
    click_cookie_and_buy_products(driver)

if __name__ == "__main__":
    main()
