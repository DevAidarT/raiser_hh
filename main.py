import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


print('Hello! If you wanna enter site www.hh.ru and rise your curriculum vitae, enter edditional information below')
email = getpass.getpass(prompt='Enter your e-mail (from hh.ru): ')
pwd = getpass.getpass(prompt='Enter your password (from hh.ru): ')

try:
    browser = webdriver.Firefox()
    browser.get('https://hh.ru/account/login?backurl=%2F&hhtmFrom=main')
    browser.find_element(by=By.CSS_SELECTOR, value=".account-login-actions .bloko-link").click()
    email_text = browser.find_element(by=By.CSS_SELECTOR, value=".bloko-form-item .bloko-input-text-wrapper .bloko-input-text")
    email_text.send_keys(email)
    pwd_text = browser.find_element(by=By.CSS_SELECTOR, value=".bloko-form-item .bloko-input-text-wrapper_icon-right .bloko-input-text")
    pwd_text.send_keys(pwd)
    browser.find_element(by=By.CSS_SELECTOR, value=".account-login-actions .bloko-button").click()
    time.sleep(2)
    browser.get('https://kazan.hh.ru/applicant/resumes?hhtmFrom=main')
    browser.find_element(By.CSS_SELECTOR, value='.applicant-resumes-actions-wrapper .applicant-resumes-action .bloko-link').click()
    browser.quit()
    print('Success, your curriculum vitae is raised in the HH search!')
except Exception:
    print('Error occured!')
finally:
    browser.quit()
