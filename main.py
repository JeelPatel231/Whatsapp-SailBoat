import selenium, time, json
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from modules import cow

def driverSetup():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edge/46.1.2.5140"')
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-data-dir=chrome-data")
    options.add_argument('--disable-gpu')
    options.add_argument("--start-maximized")
    options.add_argument("--allow-running-insecure-content")
    global driver
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
        try:
            driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/div/span[@data-testid='status-check']")
            latest_msg_from = "Me"
        except:
            driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/div/span[@data-testid='status-dblcheck']")
            latest_msg_from = "Me"
        chat_type = "noidea"
    except:
        try:
            latest_msg = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[3]").text
            latest_msg_from = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[1]").text
            chat_type = "group"
        except:
            latest_msg = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span").text
            chat_type = "personal"
            latest_msg_from = driver.find_element_by_xpath("//div[@aria-label='Chat list']/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[1]/div[1]/span").text
    return(latest_msg,chat_type,latest_msg_from)

def select_chat(chat_name):
    driver.find_element_by_xpath("//div[@id='side']/div[1]/div/label/div/div[2]").send_keys(chat_name + Keys.ENTER)

def send_msg(driver,text):
    driver.find_element_by_xpath("//footer/div[1]/div[2]/div/div[2]").send_keys(text)
    driver.find_element_by_xpath("//footer/div[1]/div[3]/button/span").click()

def active_chat_last():
    last_msg = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()]").text
    try:
        driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]").text
        is_replied = True
    except:
        is_replied = False
    last_msg_time = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()]").text
    try:
        last_msg_sender = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-2]").text
    except:
        last_msg_sender = "me"
    print(last_msg,"\n",last_msg_sender,"\n",last_msg_time,"\n",is_replied)

def polling():
    get_nth_chat(0).click()
    text_catch = get_latest_msg()[0]
    if get_latest_msg()[2] == "Me":
        if "." in text_catch[0]:
            print(text_catch)
            if text_catch == ".cow":
                cow()
        while text_catch == get_latest_msg()[0]:
            pass
    time.sleep(1)
    polling()

def scanqr():
    driver.get("https://web.whatsapp.com")
    time.sleep(1)
    driver.get_screenshot_as_file("screenshot.png")
    time.sleep(5)

if __name__ == "__main__":
    print("module imported")
else:
    driverSetup()
    scanqr()
    Thread(target=polling).start()