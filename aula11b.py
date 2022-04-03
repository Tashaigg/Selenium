from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert


url = 'http://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()
browser.get(url)
#wdw = WebDriverWait(browser, 40)

#wdw.until(visibility_of(browser.find_element_by_css_selector('h1')))

print('h1 vaila')

alerta = Alert(browser)
browser.find_element_by_css_selector("#alert").click()

'''

'''
#lerta.text()
