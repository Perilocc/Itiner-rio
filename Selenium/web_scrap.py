from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

#Lista de Produtos
produtos = ["Notebook", "Smartphone", "Cadeira Gamer"] 

# Configurações do Navegador
service = Service(executable_path="Selenium\msedgedriver.exe")
# Configurações do navegador
edge_options = Options()
edge_options.add_argument("--start-maximized")  # Abre o navegador maximizado
edge_options.add_argument("--disable-notifications")  # Desabilita notificações
edge_options.add_argument("--inprivate")  # Modo de navegação inprivate

# Inicialização do WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Abrindo uma página
driver.get("https://www.mercadolivre.com.br/")


time.sleep(5)
"""
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Rejeitar"))  # Mude o texto se necessário
    ).click()
except:
    print("Botão de cookies não encontrado ou já foi removido.")
"""

# Inicializando Planilha
wb = Workbook()
ws = wb.active
ws.title = "Produtos"
ws.append(["Produto", "Preço", "Imagem"])  # Cabeçalhos

time.sleep(5)

for produto in produtos:
    try:
        # Encontra o campo de busca
        input_box = driver.find_element(By.NAME, "as_word")
        input_box.clear()  # Limpa o campo antes de cada nova busca
        input_box.send_keys(produto + Keys.RETURN)  # Faz a busca
        time.sleep(5)  # wait

        # Espera o primeiro produto carregar e clica nele
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-search-result__content-wrapper"))
        )
        primeiro_produto = driver.find_element(By.CSS_SELECTOR, ".ui-search-result__content-wrapper")
        primeiro_produto.click()  # Clica no primeiro produto
        time.sleep(5)  # Espera a página carregar

        # Pega o nome/título do produto
        nome = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-pdp-title"))
        ).text
        # Pega o preço do produto
        preco = driver.find_element(By.CSS_SELECTOR, ".price-tag-fraction").text
        imagem_url = driver.find_element(By.CSS_SELECTOR, ".ui-pdp-image__figure img").get_attribute("src")

        # Baixar a imagem
        img_data = requests.get(imagem_url).content
        img = Image(BytesIO(img_data))
        
        # Ajustar Imagem
        img.width = 100  
        img.height = 100

        # Salvar dados no Excel
        ws.append([nome, preco])  # Adiciona nome e preço
        img.anchor = f"C{ws.max_row}"  # Define onde a imagem será inserida
        ws.add_image(img)

        print(f"Produto: {nome} | Preço: R${preco} | Imagem: {imagem_url}")
    
    except Exception as e:
        print(f"Erro ao buscar '{produto}': {e}")

    time.sleep(5)  # wait

# Salvar o arquivo Excel
wb.save("produtos_com_imagens.xlsx")

# Fechando o navegador
driver.quit()

