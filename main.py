
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

screenshot_counter = 1

def create_browser():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    # REMOVE this line to make Chrome visible, but Replit won't show GUI anyway
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def run_loop():
    global screenshot_counter
    while True:
        driver = None
        try:
            print("[+] Opening incognito browser...")
            driver = create_browser()
            driver.delete_all_cookies()

            driver.get("https://youtu.be/bNDG74QS7JI")  # Replace this
            time.sleep(3)

            # Press 'k'
            print("[+] Pressing 'k' key...")
            actions = ActionChains(driver)
            actions.send_keys("k").perform()

            time.sleep(25)
            driver.quit()
            print("[+] Closed browser. Waiting 2 sec...\n")
            time.sleep(2)

        except Exception as e:
            print("[-] Error:", e)
            if driver:
                driver.quit()
            time.sleep(5)

run_loop()
