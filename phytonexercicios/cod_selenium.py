from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#Abrir navegador
navegador = webdriver.Chrome()

#Acessar um site
navegador.get("https://gemini.google.com/app")

#Tela cheia
navegador.maximize_window()

#Achando o texto e escrevendo
#campo_pergunta = navegador.find_element(By.CLASS_NAME, "placeholder")
#campo_pergunta.send_keys("Bom dia")
#campo_pergunta.send_keys(Keys.ENTER)
#Clique no botao

time.sleep(60)