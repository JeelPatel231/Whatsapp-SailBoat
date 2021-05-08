import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
# options.add_argument('--headless')
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edge/46.1.2.5140"')
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-data-dir=chrome-data")
options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")
options.add_argument("--allow-running-insecure-content")
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

driver.get("https://web.whatsapp.com")
time.sleep(10)
driver.close()
exit()