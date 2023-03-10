from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time,os,base64,json,csv,re
# import undetected_chromedriver as uc
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
from time import sleep
cwd = os.getcwd()
opts = Options()

# opts.add_argument('--headless=chrome')
# #pts.headless = False
import random
import string

# printing lowercase
 

opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('--disable-infobars')
opts.add_argument('--ignore-certifcate-errors')
opts.add_argument('--ignore-certifcate-errors-spki-list')
opts.add_argument("--incognito")
opts.add_argument('--no-first-run')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--disable-infobars")
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--log-level=3') 
opts.add_argument("--start-maximized")
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option("useAutomationExtension", False)
opts.add_experimental_option("excludeSwitches",["enable-automation"])
 
# mobile_emulation = {
#     "deviceMetrics": { "width": 660, "height": 1080, "pixelRatio": 3.4 },
#     }
def date_show():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date
 
def xpath_type(el,mount):
    return wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(mount)

def xpath_fast(el):
    element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return element_all.click()

def xpath_faster(el):
    element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)  
    return element_all.click()

def xpath_execute(el):
    element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all)

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    
    return element_all.click()

def get_country():
    element_all = wait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@class,"awsc-region-menu-item--")]')))
    return element_all

def login_account(email,password,access_key):
    sleep(2)
    print(f'{date_show()} Input data login')
    xpath_long('//input[@id="iam_user_radio_button"]')
    print(f"[{time.strftime('%d-%m-%y %X')}] Trying to Login {email}")
    sleep(2)
    xpath_type('//input[@id="resolving_input"]',access_key)
    sleep(2)
    xpath_type('//input[@id="resolving_input"]',Keys.ENTER)
    sleep(2)
    xpath_type('//input[@id="username"]',email)
    sleep(2)
    xpath_type('//input[@id="password"]',password)
    sleep(2)
    xpath_type('//input[@id="password"]',Keys.ENTER)
    # xpath_type('//input[@type="email"]',email)
    # sleep(2)
    # xpath_fast('//button[@id="next_button"]')
    # sleep(2)
    # xpath_type('//input[@type="password"]',password)
    # sleep(2)
    # xpath_fast('//button[@id="signin_button"]')
    sleep(10)
    
def main(email,password,accesskey,countries,jumlah):
    global browser
    # opts.add_experimental_option("mobileEmulation", mobile_emulation)
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    # browser = webdriver.Chrome(use_subprocess=True,driver_executable_path=f"{cwd}//chromedriver.exe")
    browser = webdriver.Chrome(options=opts,desired_capabilities=dc,service=Service(ChromeDriverManager().install()))
    browser.get("https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_ap-southeast-2_00b54cf8a219917d&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=l7OEP9SY07oCH2gRn_OvHk8Jn20mNfIgLX_zsiMvDjU&code_challenge_method=SHA-256")
    login_account(email,password,accesskey)
    wait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="more-menu__awsc-nav-account-menu-button"]')))
    print(f'{date_show()} Login success')
    sleep(2)
    print(f'{date_show()} Getting list country')
    country_available = get_country()
    
    country_list = []
    number = 0
    for country in country_available:
        if number == int(countries):
            break
        country_list.append(country.get_attribute('data-region-id'))
        number = number + 1
    
    country_list 
    
    for country_get in country_list:
        print(f'{date_show()} {country_get} List country is {len(country_list)}')
        
        browser.get(f'https://{country_get}.console.aws.amazon.com/ecs/home?region={country_get}#/clusters/create/new')
        print(f'{date_show()} {country_get} Change to old view')
        sleep(10)
        try:
            wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//input[@ng-checked="checked"]')))
        except:
            xpath_fast('(//input[@type="checkbox"])[4]')
            print(f'{date_show()} {country_get} Change to old view success')
    
        sleep(3)
        print(f'{date_show()} {country_get} Trying to add cluster')
        xpath_long('//a[@href="#/clusters"]')
        sleep(3)
        xpath_long('//awsui-button[@id="create-cluster-button"]/button')
        print(f'{date_show()} {country_get} Open cluster menu')
        try:
            sleep(3)
            xpath_fast('//*[@id="ng-app"]/div/ecs-configure-cluster-wizard/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]')
        except:
            pass
        print(f'{date_show()} {country_get} Trying to fill cluster data')
        try:
            sleep(2)
            element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="btn btn-primary"]')))
            browser.execute_script("arguments[0].scrollIntoView();", element_all)
            sleep(2)
            xpath_fast('//div[@class="btn btn-primary"]')
        except:
            pass
        letters = string.ascii_lowercase
        print(f'{date_show()} {country_get} Trying to fill cluster name')
        xpath_type(f'(//input[@type="text"])[1]',''.join(random.choice(letters) for i in range(10)))
        sleep(2)
        xpath_fast('//div[@class="btn btn-primary"]')
        sleep(10)
        #//div[@class="awsui-alert-has-header awsui-alert-inside awsui-alert-type-error"]
        print(f'{date_show()} {country_get} Check cluster status')
        verify = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//span[@ng-bind-html="ecsConfig.statusMsg"]'))).text
        if "successfully" in verify:
            print(f'{date_show()} {country_get} {country_get} success created')
        else:
            print(f'{date_show()} {country_get} {country_get} failed created')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to make Task definitions')
        xpath_long('//awsui-button[@id="launch-status-view-cluster-button"]/button')
        sleep(3)
        print(f'{date_show()} {country_get} Open manu Task definitions')
        xpath_long('//a[@href="#/taskDefinitions"]')
        sleep(2)
        xpath_long('//awsui-button[@id="create-new-task-def-button"]/button')
        sleep(2)
    
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="btn btn-primary"]')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        sleep(2)
        xpath_long('//div[@class="btn btn-primary"]')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to configure via Json')
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//awsui-button[@text="Configure via JSON"]/button')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        sleep(2)
        xpath_long('//awsui-button[@text="Configure via JSON"]/button')
        sleep(2)
        wordlist = "config.json"
        wordlist = open(f"{wordlist}","r",encoding="utf-8")
        wordlist = wordlist.read()
        print(f'{date_show()} {country_get} Fill json input')
        print(wordlist)
        try:
            element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//awsui-textarea/textarea')))
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(wordlist)
        except Exception as e:
            print(e)
            element = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, '//awsui-textarea/textarea')))
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(wordlist)
            
        sleep(2)
        xpath_long('//awsui-button[@text="Save"]/button')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to save task')
        xpath_long('//div[@class="aws-button btn-wrapper"]/div[@class="btn btn-primary"]')
        print(f'{date_show()} {country_get} Check status task')
        sleep(2)
        verify_dua = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//span[@class="ng-binding ng-scope"]'))).text
        if "succeeded" in verify_dua:
            print(f'{date_show()} {country_get} {country_get} task created')
        else:
            print(f'{date_show()} {country_get} failed task created')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to create service')
        xpath_long('//awsui-button[@text="View task definition"]/button')
        sleep(2)
        xpath_long('//div[@class="dropdown ecs-dropdown"]/div[1]')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to open menu create service')
        try:
            xpath_long("//a[text()='Create Service']/parent::li")
        except Exception as e:
            print(e)
            get_url = browser.current_url
            browser.get(f'{get_url}/createService')
        
        sleep(2)
        try:
            xpath_fast('//span[@class="ecs-capacity-provider-switch-type ng-binding ng-scope"]')
        except:
            xpath_fast('//span[@class="ecs-capacity-provider-switch-type ng-binding ng-scope"]/parent::span')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to add provider')
        xpath_fast('//awsui-button[@text="Add another provider"]/button')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to select provider')
        try:
            xpath_fast('(//awsui-select[@placeholder="Select"]/span/span)[2]')
        except:
            xpath_execute('(//awsui-select[@placeholder="Select"]/span/span)[2]')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to select fargate')
        xpath_fast('//li[@data-value="FARGATE"]')
        sleep(2)
        
        xpath_fast('//awsui-button[@text="Add another provider"]/button')
        print(f'{date_show()} {country_get} Select fargate success')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to add provider')
        try:
            xpath_fast('(//awsui-select[@ng-model="item.capacityProvider"])[2]/span/span')
        except:
            xpath_execute('(//awsui-select[@ng-model="item.capacityProvider"])[2]/span/span')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to select fargate spot')
        xpath_fast('(//li[@data-value="FARGATE_SPOT"])[2]')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to fill service name')
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//awsui-textfield[@ng-if="config.showServiceInput"]/input')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        sleep(2)
        xpath_type('//awsui-textfield[@ng-if="config.showServiceInput"]/input',''.join(random.choice(letters) for i in range(10)))
        sleep(2)
        print(f'{date_show()} {country_get} Trying to input number of count')
        xpath_type('//awsui-textfield[@ng-model="config.desiredCount"]/input',jumlah)
        sleep(2)
        print(f'{date_show()} {country_get} Trying to next')
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//aws-button[@button-text="wizardSteps[wizardActiveStep].navigation.nextButton.label"]/div/div')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        sleep(2)
        xpath_long('//aws-button[@button-text="wizardSteps[wizardActiveStep].navigation.nextButton.label"]/div/div')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to select VPC')
        element_all = wait(browser,10).until(EC.presence_of_element_located((By.XPATH, '//html')))
        element_all.send_keys(Keys.HOME)
        sleep(2)
        xpath_long('//awsui-select[@change="ctrl.getSubnetsAndSecurityGroups()"]/span/span')
        sleep(2)
        try:
            xpath_fast('//li[contains(@data-value,"vpc")]')
        except:
            xpath_execute('//li[contains(@data-value,"vpc")]')
        sleep(2)
        print(f'{date_show()} {country_get} Trying to select subnet')
        xpath_fast('//awsui-select[@ng-model="currentItem"]//span[@class="awsui-select-target"]')
        sleep(2)
        click_all = wait(browser,5).until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@data-value,'subnet')]")))
        for i in range(1,len(click_all)+1):
            sleep(5)
            
            try:
                xpath_fast(f"(//li[contains(@data-value,'subnet')])[{i}]")
                print(f'{date_show()} {country_get} Select subnet success')
            except:
                iklieds = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, f"(//li[contains(@data-value,'subnet')])[{i}]")))
                browser.execute_script("arguments[0].click();", iklieds)
                print(f'{date_show()} {country_get} Execute select subnet success')
            sleep(3)
            try:
                
                xpath_faster('//awsui-select[@ng-model="currentItem"]/span/span')
            
            except Exception as e:
                
                iklied = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//awsui-select[@ng-model="currentItem"]/span/span')))
                browser.execute_script("arguments[0].click();", iklied)
                pass
            
        sleep(2)
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//aws-button[@button-text="wizardSteps[wizardActiveStep].navigation.nextButton.label"]/div/div')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        sleep(2)
        element_all.click()
        print(f'{date_show()} {country_get} Trying to next')
        sleep(8)
        xpath_long('//aws-button[@button-text="wizardSteps[wizardActiveStep].navigation.nextButton.label"]/div/div')
        sleep(2)
        sleep(2)
        element_all = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '//aws-button[@button-text="wizardSteps[wizardActiveStep].navigation.nextButton.label"]/div/div')))
        browser.execute_script("arguments[0].scrollIntoView();", element_all)
        print(f'{date_show()} {country_get} Trying to next')
        sleep(2)
        element_all.click()
        sleep(20)
        print(f'{date_show()} {country_get} Check status')
        verify = wait(browser,5).until(EC.presence_of_element_located((By.XPATH, '(//h2[@data-analytics="ECSServiceStatus"]/span)[1]'))).text
        print(f'{date_show()} {country_get} {verify}')
        sleep(10)
    
if __name__ == '__main__':
    print(f'{date_show()} Automation Task AWS')
    get_data = open(f"{cwd}\\data.txt","r")
    get_data = get_data.read()
    get_data = get_data.split("\n")
    for i in get_data:
        email = i.split("|")[0]
        password = i.split("|")[1]
        access_key = i.split("|")[2]
        countries = i.split("|")[3]
        task_number = i.split("|")[4]
        try:
            main(email,password,access_key,countries,task_number)
        except Exception as e:
            print(e)
        
