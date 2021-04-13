import selenium, time, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument('--headless')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edge/46.1.2.5140"')
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-data-dir=chrome-data")
options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")
options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

def get_nth_chat(n):
    chatpixels = n*72
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Chat list']")))
    nthchat = driver.find_element_by_xpath(f"//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY({chatpixels}px)')]/div/div/div[2]/div[1]/div[1]/span")
    print(nthchat.text)
    return nthchat

def get_latest_msg():
    try:
        latest_msg = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span").text
        driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/div/span")
        latest_msg_from = "Me"
    except:
        latest_msg = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[3]").text
        latest_msg_from = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[1]").text
    print(latest_msg)
    print(latest_msg_from)

def select_chat(chat_name):
    # search_input_box = 
    driver.find_element_by_xpath("//div[@id='side']/div[1]/div/label/div/div[2]").send_keys(chat_name + Keys.ENTER)
    # get_nth_chat(1).click()

def write_msg(text):
    driver.find_element_by_xpath("//footer/div[1]/div[2]/div/div[2]").send_keys(text)
    driver.find_element_by_xpath("//footer/div[1]/div[3]/button/span").click()

def scanqr():
    driver.get("https://web.whatsapp.com")
    time.sleep(1)
    driver.get_screenshot_as_file("screenshot.png")
scanqr()




##################### functions start here ########################

