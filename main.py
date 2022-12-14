import errno
import os
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

def ft(driver, img):
    time.sleep(4)
    try:
        os.mkdir('pics/'+img)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot('pics/'+img+'/img_'+now+'.png')

def lg():
    driver = webdriver.Chrome()
    driver.get("https://demo-saas.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys("superadmin@example.com")
    driver.find_element(By.ID, 'password').send_keys("123456")
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/div/button').click()
    return driver

def lgUser():
    driver = webdriver.Chrome()
    driver.get("https://demo-saas.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys("client@example.com")
    driver.find_element(By.ID, 'password').send_keys("123456")
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/div/button').click()
    return driver

def lgAdmin():
    driver = webdriver.Chrome()
    driver.get("https://demo-saas.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys("admin@example.com")
    driver.find_element(By.ID, 'password').send_keys("123456")
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/div/button').click()
    return driver

@mark.parametrize("email,psw", [("superadmin@example.com", "123456"), ("eror@gmail.com", "123456")])
def test_login(email, psw):
    driver = webdriver.Chrome()
    driver.get("https://demo-saas.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(psw)
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/div/button').click()
    ft(driver, 'login')
    assert driver.current_url != 'https://demo-saas.worksuite.biz/login'

def test_cerrarsesion():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[4]/div[1]/div[1]/div').click()
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/div[4]/div[1]/div[1]/div/ul/li[2]/a').click()
    ft(driver, 'cerrar')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/login'

def test_packages():
    driver = webdriver.Chrome()
    driver.get("https://demo-saas.worksuite.biz/login")
    driver.maximize_window()
    driver.find_element(By.ID, 'email').send_keys("superadmin@example.com")
    driver.find_element(By.ID, 'password').send_keys("123456")
    driver.find_element(By.XPATH, '//*[@id="loginform"]/div[4]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[4]/a').click()
    ft(driver, 'packages')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/packages'

def test_companies():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[5]/a').click()
    ft(driver, 'companies')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/companies'

def test_invoices():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[6]/a').click()
    ft(driver, 'invoices')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/invoices'

def test_adminFAQ():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[7]/a').click()
    ft(driver, 'adminFAQ')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/faq'

def test_superAdmin():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[8]/a').click()
    ft(driver, 'superadmin')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/super-admin'

def test_offline():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[9]/a').click()
    ft(driver, 'offline')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/offline-plan'
    
def test_frontSettings():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[11]/a').click()
    ft(driver, 'front')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/front-settings/front-theme-settings'

def test_supporticket():
    driver = lg()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[10]/a').click()
    ft(driver, 'supporticket')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/super-admin/support-tickets'

def test_changeLanguage():
    driver = lgUser()
    first = driver.find_element(By.XPATH, '//*[@id="project-timeline"]/div/div[1]').text
    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div[1]/div[2]/div/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div/div[1]/div[2]/div/div/div/ul/li[3]').click()
    time.sleep(5)
    second = driver.find_element(By.XPATH, '//*[@id="project-timeline"]/div/div[1]').text
    ft(driver, 'changelanguage')
    assert first != second

def test_creditNote():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[7]/a').click()
    ft(driver, 'credit')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/credit-notes'

def test_estimates():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[8]/a').click()
    ft(driver, 'estimates')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/estimates'

def test_payments():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[9]/a').click()
    ft(driver, 'payments')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/payments'

def test_events():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[10]/a').click()
    ft(driver, 'events')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/events'

def test_financeDashboard():
    driver = lgAdmin()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li[6]/a').click()
    ft(driver, 'finance')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/admin/finance-dashboard'

def test_products():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]').click()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[9]/a').click()
    ft(driver, 'products')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/admin/products'

def test_employeeList():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[6]').click()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[6]/ul/li[1]/a').click()
    ft(driver, 'employeelist')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/user-chat'

def test_holiday():
    driver = lgUser()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]').click()
    driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[6]/ul/li[5]/a').click()
    ft(driver, 'holiday')
    assert driver.current_url == 'https://demo-saas.worksuite.biz/client/notes'
