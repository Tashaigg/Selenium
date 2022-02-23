from selenium.webdriver import Chrome
from time import sleep
browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep (0.5)

p = browser.find_elements_by_tag_name('p')

texto = p[1].text
#print(texto)
#print(texto[-1])
numero_esperado = str(texto)[-1]
atual = '0'
a = browser.find_element_by_tag_name('a')
while atual[-1] != numero_esperado:
    a.click()
    p = browser.find_elements_by_tag_name('p')
    atual = p[-1].text
    #print (atual)

print('Vitoria Absoluta')
#browser.quit()
