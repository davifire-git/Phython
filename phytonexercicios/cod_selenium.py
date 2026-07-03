from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#Abrir navegador
navegador = webdriver.Chrome()

#Acessar um site
navegador.get("https://use.ai/pt?model=claude&utm_match_type=e&utm_funnel=&partner=WM&id=Z29vZ2xlfGNwY3xBSV9CUl9QVF9DaGF0X0RTS19TRUFfTExNX0NsYXVkZXwyMzc0NjkyNDMwOXxjbGF1ZGUgYWl8ODA0Nzc1NzExODg5fHwxOTYxNzI4NzkxOTh8QUlfQlJfUFRfQ2xhdWRlX0V4YWN0fDgwNDc3NTcxMTg4OXx8fHx8fENqd0tDQWp3dTUzU0JoQWhFaXdBSnpTTE5uU0pMTmtjcUhiOE9sOTdBV3kwUDZxYW9aWmtHRFY1SWFSMlZnZkJDU3gwNE5CcnQ0TFdqQm9DeTV3UUF2RF9Cd0V8fHw&url=https%3A%2F%2Fuse.ai%2Fpt%3Fmodel%3Dclaude&gad_source=1&gad_campaignid=23746924309&gbraid=0AAAAACQlLoYthmW6uIqJC41L_iFxSJRdf")

#Tela cheia
navegador.maximize_window()

campo_pergunta = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '[data-testid="chat-input-textarea"]')
    )
)


campo_pergunta.send_keys("Como fazer uma limonada")
campo_pergunta.send_keys(Keys.ENTER)

#Achando o texto e escrevendo

#campo_pergunta = navegador.find_element(By.CLASS_NAME, "col-start-1.col-end-2.row-start-1.row-end-2.w-full.select-text.resize-none.overflow-hidden.border-0.bg-transparent.text-base.leading-6.outline-none.[overflow-wrap:break-word].placeholder:whitespace-nowrap.placeholder:font-normal.text-[#0d0d0d].placeholder-[#3d3d3da9].dark:text-foreground.dark:placeholder-[#9ca3af]")

#campo_pergunta.send_keys("Bom dia")
#campo_pergunta.send_keys(Keys.ENTER)
#Clique no botao

time.sleep(60)