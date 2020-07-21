from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME_OR_EMAIL = ""
TWITTER_PASSWORD = ""
SLEEP_TIME_BEFORE_NEW_SCROLL = 5 #em segungos
LIMIT_LOOP_COUNTER = 10

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

driver.implicitly_wait(5)
elem = driver.find_element_by_name("session[username_or_email]") #procurando o campo de login
elem.clear() # limpando o campo
elem.send_keys(TWITTER_USERNAME_OR_EMAIL) # adicionando o dado de usuario ou email

elem = driver.find_element_by_name("session[password]") #procurando o campo de senha
elem.clear()# limpando o campo
elem.send_keys(TWITTER_PASSWORD) # adicionando a senha

elem.send_keys(Keys.RETURN) # apertando o ENTER para enviar os dados de login

height_size_browser = driver.get_window_size().get('height')
scroll_size = 0
loop_counter = 0
while True:
    if loop_counter > LIMIT_LOOP_COUNTER:
        break; 

    driver.execute_script(f"window.scrollTo(0, {scroll_size});")
    time.sleep(SLEEP_TIME_BEFORE_NEW_SCROLL)

    scroll_size += (height_size_browser / 2)
    loop_counter = loop_counter + 1

driver.close()
