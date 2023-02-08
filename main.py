from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import dotenv
import os
import time
import random

new_file = dotenv.find_dotenv()
dotenv.load_dotenv(new_file)
CHROME_DRIVER = os.environ.get("CHROME_PATH")
ISP = os.environ.get("ISP")
TWITTER_URL = "https://twitter.com"
SPEEDTEST_URL = "https://www.speedtest.net"
SHORT = 3  # Amount of delay in seconds to be used
DELAY = 5  # Amount of delay in seconds to be used
END = 9
DIVIDE_BY = 10
promised_down = None   # Download speed(Mbps) advertised by ISP. It will be determined later
promised_up = None   # Upload speed(Mbps) advertised by ISP. It will be determined later
SERVICE = Service(executable_path=CHROME_DRIVER)


def generate_random_time(number_of_secs):
    """Generates a random time between 1 and 5 seconds once it receives the number of seconds"""
    return round(random.randint(DELAY, END) / DIVIDE_BY, 1) * number_of_secs


class InternetSpeedTwitterBot:
    def __init__(self):
        prefs = {
            "profile.default_content_setting_values":
                {
                    "geolocation": 1,  # enables location settings
                    'notifications': 0,  # disables notifications
                },
            'profile.managed_default_content_settings':
                {
                    'geolocation': 1  # sets your current location
                }
        }
        self.driver = None
        self.mouse_pointer = None
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", prefs)
        self.options.add_argument("--disable-popup-blocking")    # allows pop-ups to input your gmail login details
        self.down = None
        self.up = None
        self.twitter_user = os.environ.get("USERNAME")
        self.twitter_pass = os.getenv("PASSWORD")
        self.isp_name = None

    def get_internet_speed(self):
        """Runs an Internet Speed Test and gets the values for download speed and upload speed"""
        with webdriver.Chrome(service=SERVICE, options=self.options) as self.driver:
            self.driver.get(url=SPEEDTEST_URL)
            time.sleep(DELAY + DELAY)
            self.mouse_pointer = ActionChains(self.driver)
            WebDriverWait(self.driver, DELAY*6).until(ec.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, ".js-start-test .start-text")))
            self.isp_name = self.driver.find_element(By.CSS_SELECTOR, ".ispComponent .result-label").text
            print(self.isp_name)
            # Locate the speedtest button
            start_speedtest = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test .start-text")
            self.mouse_pointer.move_to_element(start_speedtest).click().perform()   # Click to run the speedtest
            time.sleep(generate_random_time(DELAY * DELAY))
            up = self.driver.find_element(By.CSS_SELECTOR, ".result-item-upload .upload-speed")
            up_value = up.get_attribute("data-upload-status-value")    # Track completion of Speedtest
            while up_value == "NaN":   # Wait until it has an actual value before quitting
                time.sleep(generate_random_time(DELAY + DELAY))
                up = self.driver.find_element(By.CSS_SELECTOR, ".result-item-upload .upload-speed")
                up_value = up.get_attribute("data-upload-status-value")    # Tracks completion of Speedtest
                try:
                    if float(up_value) >= 0:   # becomes true when up_value becomes a number
                        self.down = self.driver.find_element(By.CSS_SELECTOR, ".result-item-download .download-speed").text
                        self.up = self.driver.find_element(By.CSS_SELECTOR, ".result-item-upload .upload-speed").text
                except ValueError:
                    pass
            print(f"Download Speed: {self.down}Mbps Upload Speed: {self.up}Mbps")

    def tweet_at_provider(self):
        """Tweets the complaint to the ISP"""
        with webdriver.Chrome(service=SERVICE, options=self.options) as self.driver:   # Activates Selenium bot
            self.driver.get(url=TWITTER_URL)
            time.sleep(DELAY + DELAY)
            self.mouse_pointer = ActionChains(self.driver)    # activates the mouse pointer
            log_in = self.driver.find_element(By.CSS_SELECTOR, ".r-1niwhzg .r-poiln3 span")   # locate the login button
            self.mouse_pointer.move_to_element(log_in).click().perform()   # click it
            time.sleep(generate_random_time(DELAY + DELAY))
            self.login_details(self.twitter_user)    # Enter Twitter Username
            self.login_details(self.twitter_pass)    # Enter Twitter Password
            # Locate the tweet button and wait for it to be clickable
            WebDriverWait(self.driver, DELAY*6).until(ec.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, ".r-42olwf .r-jwli3a")))
            to_tweet = self.driver.find_element(By.CSS_SELECTOR, ".r-42olwf .r-jwli3a")
            self.mouse_pointer.click(on_element=to_tweet).perform()    # Click it
            time.sleep(generate_random_time(DELAY+DELAY))
            type_tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
            self.mouse_pointer.click(on_element=type_tweet).perform()   # click the text area to type the tweet
            time.sleep(generate_random_time(DELAY + DELAY))
            type_tweet.send_keys(f"Hey {ISP}, why is my internet speed {self.down}Mbps down / {self.up}Mbps up, "
                                 f"when I pay for {promised_down}Mbps down / {promised_up}Mbps up?")  # the tweet
            time.sleep(generate_random_time(DELAY + DELAY))
            tweet = self.driver.find_element(By.CSS_SELECTOR, ".r-42olwf .r-jwli3a span")  # locate tweet button
            self.mouse_pointer.move_to_element(tweet).click().perform()   # click the tweet button to send the tweet
            time.sleep(generate_random_time(DELAY + DELAY))

    def login_details(self, detail):
        time.sleep(generate_random_time(DELAY))
        send_login_detail = self.driver.find_element(By.CLASS_NAME, "r-homxoj")   # locate username tab
        send_login_detail.send_keys(detail)   # sends the username/password
        time.sleep(generate_random_time(SHORT))
        send_login_detail.send_keys(Keys.ENTER)   # presses the Enter Key
        time.sleep(generate_random_time(DELAY + DELAY))


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
if twitter_bot.isp_name == "Airtel":
    promised_up = 10  # Upload speed(Mbps) advertised by ISP
    promised_down = 35  # Download speed(Mbps) advertised by ISP
elif twitter_bot.isp_name == "Tizeti":
    promised_down = 5   # Download speed(Mbps) advertised by ISP
    promised_up = 1   # Upload speed(Mbps) advertised by ISP
if float(twitter_bot.down) < promised_down or float(twitter_bot.up) < promised_up:
    twitter_bot.tweet_at_provider()
