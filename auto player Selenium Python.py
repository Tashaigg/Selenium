from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
browser = Chrome()
url = 'https://selenium.dunossauro.live/aula_04.html'
browser.get(url)
sleep(0.5)
main = browser.find_element_by_tag_name('main')
print(main.text)

ancoras = main.find_elements_by_tag_name('a')
for ancora in ancoras:
    print(ancora.text, ancora.get_attribute('href'))
link_ex = (ancoras[2].get_attribute('href'))

browser.get(link_ex)
#pag 0
sleep(0.5)
print('pag 0')
main0 = browser.find_element_by_tag_name('main')
a0 = main0.find_element_by_tag_name('a')
print(f'texto: {a0.text}')
a0.click()
#pag1
print('pag 1')
sleep(0.5)
main1 = browser.find_element_by_tag_name('main')
ps = main1.find_elements_by_tag_name('p')
equa = (ps[1].text)
print(equa)
num = int(equa[0]) * int(equa[4])
print(num)
a1 = main1.find_elements_by_tag_name('a')
print(int(a1[0].text))
if int(a1[0].text)==int(num):
    a1[1].click()
else:
    a1[0].click()
#pag2
print('pag 2')
sleep(1)
browser.refresh()
sleep(1)
browser.refresh()
sleep(1)
browser.refresh()
sleep(1)
main2 = browser.find_element_by_tag_name('main')
a2 = main2.find_elements_by_tag_name('a')
for elemento in a2:
    if elemento.text == browser.title:
        elemento.click()
        break

#pag3
print('pag 3')
sleep(1)
atual = (urlparse(browser.current_url))
main3 = browser.find_element_by_tag_name('main')
li3 = main3.find_elements_by_tag_name('a')

for elemento in li3:
    if elemento.text in atual.path:
        elemento.click()
        break
    else:
        print(elemento.text)
        print(atual.path)
#pag4
print('pag 4')
sleep(1)
browser.refresh()

#browser.quit()
