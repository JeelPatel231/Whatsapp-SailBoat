import selenium, time, json,os,importlib,sys,socketserver,http.server,base64
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



# import cutoms mods from list   
mods=['cow','evaluate','ripaud','ripvid','help','getsticker','fuckyou','gimg','reverse','rbg','reddit']

for lib in mods:
    globals()[lib] = importlib.import_module("modules."+lib)

#PORT = int(sys.argv[1])

#def screenshot_server():
#    print("THREAD STARTED")
#    with socketserver.TCPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
#        print("Server started at localhost:" + str(PORT))
#        httpd.serve_forever()

def driverSetup():
    options = Options()
    #   options.add_argument('--headless')
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
    nthchat = driver.find_element_by_xpath(f"//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY({chatpixels}px)')]/div/div/div[2]/div[1]/div[1]/span")
    return nthchat

def get_latest_msg():
    try:
        latest_msg = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span").text
        try:
            driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/div/span[@data-testid='status-check']")
            latest_msg_from = "Me"
        except:
            driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/div/span[@data-testid='status-dblcheck']")
            latest_msg_from = "Me"
        chat_type = "noidea"
    except:
        try:
            latest_msg = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[3]").text
            latest_msg_from = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span[1]").text
            chat_type = "group"
        except:
            try:
                latest_msg = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span/span").text
                chat_type = "personal"
                latest_msg_from = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[1]/div[1]/span").text
            except:
                latest_msg = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span").text
                if latest_msg == "typing...":
                    chat_type = "personal"
                    latest_msg_from = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[1]/div[1]/span").text
                else:
                    chat_type = "group"
                    latest_msg_from = driver.find_element_by_xpath("//div[@id='pane-side']/div[1]/div/div/div[contains(@style,'transform: translateY(0px)')]/div/div/div[2]/div[2]/div[1]/span").text.split(" ")[0]

    return(latest_msg,chat_type,latest_msg_from)

def select_chat(chat_name):
    driver.find_element_by_xpath("//div[@id='side']/div[1]/div/label/div/div[2]").send_keys(chat_name + Keys.ENTER)

def send_msg(text):
    for part in text.split('\n'):
        driver.find_element_by_xpath("//footer/div[1]/div[2]/div/div[2]").send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    driver.find_element_by_xpath("//footer/div[1]/div[3]/button/span").click()

def active_chat_last():
    last_msg = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()]").text
    try:
        driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]").text
        replied_text = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div/div/div[2]").text
        replier = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div/div/div[1]").text
        is_replied = True
    except:
        replied_text = None
        is_replied = False
    last_msg_time = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()]").text
    try:
        last_msg_sender = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-2]").text
    except:
        last_msg_sender = "me"
    if is_replied == True:
        return(last_msg,last_msg_sender,last_msg_time,is_replied,replied_text, replier)
    else:
        return(last_msg,last_msg_sender,last_msg_time,is_replied)

def stickers():
    try:
        driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div/div/div[2]/span/div")
        sticker_uri = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div/div/div[2]/span/div/img").get_attribute("src")
        is_animated = True
    except:
        sticker_uri = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div/div/div[2]/span/img").get_attribute("src")
        is_animated = False
    return(sticker_uri,is_animated)

def replied_media():
    photo_uri = driver.find_element_by_xpath("//div[@role='region']/div[last()]/div/div/div/div[last()-1]/div[last()-1]/div/div/div[2]/div/div/div[2]/div").get_attribute("style").split("\"")[1]
    return photo_uri

def send_media(rpath):
    driver.find_element_by_xpath("//span[@data-testid='clip']").click()
    driver.find_element_by_xpath("//span[@data-testid='attach-image']/following-sibling::input").send_keys(os.path.abspath(rpath))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='send']")))
    driver.find_element_by_xpath("//span[@data-testid='send']").click()

def send_doc(rpath):
    driver.find_element_by_xpath("//span[@data-testid='clip']").click()
    driver.find_element_by_xpath("//span[@data-testid='attach-document']/following-sibling::input").send_keys(os.path.abspath(rpath))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='send']")))
    driver.find_element_by_xpath("//span[@data-testid='send']").click()

def get_file_content_chrome(uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  if type(result) == int :
    raise Exception("Request failed with status %s" % result)
  return base64.b64decode(result)

def polling():
    # while True:
        text_catch = get_latest_msg()[0]
        if get_latest_msg()[2] == "Me":
            get_nth_chat(0).click()
            try:
                if "." in text_catch[0]:
                    command = text_catch.split(".",1)[1].split(" ",1)[0]
                    if command in mods:
                        print(command)
                        try:
                            args = text_catch.split(".",1)[1].split(" ",1)[1]
                        except:
                            if active_chat_last()[3] == True:
                                args = active_chat_last()[4]
                            else:
                                args = ""
                        print(args )
                        eval(command+"."+command+"('"+args+"')")
            except:
                pass
            while text_catch == get_latest_msg()[0]:
                pass
        polling()

def scan_qr():
    driver.get("https://web.whatsapp.com")
    time.sleep(2)
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='initial_startup']")))
    driver.save_screenshot('screenshot.png')
    print("screenshot taken")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='pane-side']/div[1]/div/div")))

def helpinside(command):
    if command in mods:
        eval(command+".help()")

if __name__ == "__main__":
    print("module imported")
else:
    driverSetup()
 #   Thread(target=screenshot_server).start()
    scan_qr()
    Thread(target=polling).start()
