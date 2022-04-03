from selenium.webdriver import Firefox



url = 'http://selenium.dunossauro.live/aula_11_a.html'

browser = Firefox()
browser.get(url)
#wdw = WebDriverWait(browser, 40)

#wdw.until(visibility_of(browser.find_element_by_css_selector('h1')))

print('h1 vaila')

browser.find_element_by_css_selector("#alert").click()
alerta = browser.switch_to.alert
alerta.text
alerta.confirm()
browser.find_element_by_css_selector("#alert").click()
alerta.dismiss()
