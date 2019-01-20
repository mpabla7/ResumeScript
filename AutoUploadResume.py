from selenium import webdriver
import os, pyautogui

###########################################
#     Upload resume to Linkdin            #
###########################################

os.chdir('C:\\Users\\mpabl\\Desktop\\fix_resume')

browser = webdriver.Chrome(r'C:\Users\mpabl\Desktop\PythonAutomation\chromedriver')
browser.get(r'https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin')

# login = browser.find_element_by_css_selector('#join-form > p.form-subtext.login > a')
# login.click()
#
# signinButton = browser.find_element_by_css_selector('#login-email')
# signinButton.click()

pyautogui.typewrite('mpabla7@gmail.com', interval=0.1)
pyautogui.hotkey('tab') #keyboard shortcuts
pyautogui.typewrite('PASSWORD', interval=0.1)
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')

pyautogui.moveTo(194,368,duration=4.4)
pyautogui.click()

pyautogui.moveTo(998,593,duration=4.4)
pyautogui.click()

pyautogui.moveTo(1118,390, duration=2.5)
pyautogui.dragTo(1117,853,1,button='left')

# nestedPen =  browser.find_element_by_css_selector('#ember684 > div.form-preview > div > button > span.pe-treasury__preview-info > span > span > li-icon > svg')
# nestedPen.click()
pyautogui.moveTo(468,792, duration=2)
pyautogui.click()

pyautogui.moveTo(301,938, duration=1)
pyautogui.click()

pyautogui.moveTo(293,765, duration=1)
pyautogui.click()

pyautogui.moveTo(293,765, duration=3)
#Path to Resume
#C:\Users\mpabl\Desktop\fix_resume\Mandeep_Pabla.pdf
pyautogui.typewrite('\\Users\\mpabl\\Desktop\\fix_resume\\Mandeep_Pabla.pdf', interval=0.2)
pyautogui.hotkey('enter')

pyautogui.moveTo(1050,931,duration=20)
pyautogui.click()
pyautogui.moveTo(1050,931,duration=2)
pyautogui.click()

###########################################
#     Upload resume to SJSU Handshake     #
###########################################
pyautogui.moveTo(1050,931,duration=2)

browser = webdriver.Chrome(r'C:\Users\mpabl\Desktop\PythonAutomation\chromedriver')
browser.get(r'https://sjsu.joinhandshake.com/login')

sjsu = browser.find_element_by_css_selector('#sso-button > div')
sjsu.click()

pyautogui.moveTo(1050,931,duration=1.5) #let webpage load

pyautogui.typewrite('012721943', interval=0.1)
pyautogui.hotkey('tab')
pyautogui.typewrite('PASSWORD', interval=0.1)
pyautogui.hotkey('enter')

pyautogui.moveTo(1154,200,duration=7)
pyautogui.click()

profile = browser.find_element_by_css_selector('#permanent-topbar > div > div > div:nth-child(1) > div > div > div > div > div > div.style__links___QUPuv > div.dropdown.pull-right.open > ul > li:nth-child(1) > a > div > div:nth-child(1)')
profile.click()

pyautogui.moveTo(1299,279,duration=2.5)
pyautogui.dragTo(1300,737,1,button='left')

clickMe = browser.find_element_by_css_selector('#main > div.student-profile-container > div > div > div:nth-child(1) > div > div > div:nth-child(2) > div.col-md-4 > div.student-profile-card.card-student-documents.style__card___1rhof > div > div > a')
clickMe.click()

pyautogui.moveTo(1087,346,duration=2.7)
pyautogui.click()

pyautogui.moveTo(705,517,duration=2.7)
pyautogui.click()

pyautogui.moveTo(705,517,duration=2.7)
pyautogui.typewrite('\\Users\\mpabl\\Desktop\\fix_resume\\Mandeep_Pabla.pdf', interval=0.2)
pyautogui.hotkey('enter')

pyautogui.moveTo(497,342,duration=2.7)
pyautogui.click()

pyautogui.moveTo(497,342,duration=1.7)

import random
g=random.randint(1,10000)

pyautogui.typewrite('Mandeep Pabla' + str(g))    #name must be unique so assing a rand num

pyautogui.hotkey('enter')

pyautogui.moveTo(732,364,duration=11.7)
pyautogui.click()

pyautogui.moveTo(946,417,duration=1.7)
pyautogui.click()
