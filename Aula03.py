from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser.get(url)

sleep(2)

a = browser.find_element_by_tag_name('a')
p = browser.find_element_by_tag_name('p')

for click in range (110):
    a.click()
#browser.quit()
