import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from flask import Flask, render_template

app = Flask(__name__)

run_count = 0
status_message = "Idle"

def create_browser():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')  # Headless for Vercel
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
        driver = create_browser()
        driver.delete_all_cookies()

        driver.get("https://youtu.be/bNDG74QS7JI")  # YouTube URL
        time.sleep(3)

        # Press 'k'
        actions = ActionChains(driver)
        actions.send_keys("k").perform()

        time.sleep(25)
        driver.quit()

        run_count += 1  # Increment run count after success
        status_message = "Completed"
    except Exception as e:
        status_message = f"Error: {str(e)}"
        if driver:
            driver.quit()

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

# Vercel requires this to run Flask app
if __name__ == '__main__':
    app.run()
