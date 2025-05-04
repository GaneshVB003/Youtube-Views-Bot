import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from flask import Flask, render_template

app = Flask(__name__)

# Global counter for automation runs
run_count = 0
status_message = "Idle"

def create_browser():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')  # Remove this if you want the GUI to be visible
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920x1080')

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def run_script():
    global run_count, status_message
    driver = None
    try:
        status_message = "Running"
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

        run_count += 1  # Increment the count after successful run
        status_message = "Completed"
    except Exception as e:
        print("[-] Error:", e)
        if driver:
            driver.quit()
        time.sleep(5)
        status_message = f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html', status=status_message, count=run_count)

@app.route('/start', methods=['GET'])
def start_script():
    try:
        run_script()
        return "✅ Successfully ran the automation!", 200
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
