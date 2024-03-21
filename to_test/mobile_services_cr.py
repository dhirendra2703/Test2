import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

# driver.implicitly_wait(10)
# driver.get("https://stackoverflow.com/questions/20316864/how-to-perform-right-click-using-selenium-chromedriver")
# actions_chain_obj = ActionChains(driver)
# a = driver.find_element('xpath', '(//a[text()="Sign up"])[2]')
# actions_chain_obj.context_click(a).perform()

driver.implicitly_wait(10)
driver.get("https://testtips.vidalhealthtpa.com:7443/LoginAction.do")

handles = driver.window_handles
print(handles)
driver.find_element('xpath', '//input[@id="LoginId"]').send_keys("DD")
driver.find_element('xpath', '//input[@id="Password"]').send_keys("E")
driver.find_element('xpath', '//input[@type="submit"]').click()
time.sleep(5)
handles1 = driver.window_handles
print(handles1)
driver.switch_to.window(handles1[1])
driver.find_element('xpath', '//a[contains(text(), "Policies")]').click()
driver.find_element('xpath', '//input[@name="sPolicyNO"]').send_keys('100000/145/MAR/24/CORP/A027')
# driver.find_element('xpath', '//input[@name="sPolicyNO"]').send_keys('021800/145/CARD/C0672')
driver.find_element('xpath', '//a[@class="search"]').click()
driver.find_element('xpath', '//a[@title="Edit Policy No"]').click()
driver.find_element('xpath', '//a[contains(text(),"Web Config")]').click()
driver.find_element('xpath', '//a[text()="Mobile services"]').click()
dro = driver.find_element('xpath', '//select[@name="mobileServices"]')
a = Select(dro)
value = a.first_selected_option.text
print(value)
wait_obj = WebDriverWait(driver, 10)
try:
    wait_obj.until(expected_conditions.text_to_be_present_in_element(value, "Select from list"))
    # if value == "Select from list":
    print("No Value is selected")

except:
    if value == "Both":
        print("Both condition")
    if value == "IPD":
        print("IPD condition")
    else:
        print("OPD condition")
    for b in a.options:
        print(b.text)

else:
    print("Else")

#
# driver.quit()

# if a.first_selected_option.get_attribute("BOTH") == "BOTH":
#     print("Both is selected")
# else:
#     print("Other is selected")
