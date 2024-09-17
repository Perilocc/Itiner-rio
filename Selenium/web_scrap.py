import os
import time
import requests
from io import BytesIO
from selenium import webdriver
from PIL import Image as PILImage
from openpyxl import load_workbook
from input import obter_lista_produtos
from FuncImage import add_image_to_cell
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl.drawing.image import Image as OpenpyxlImage
from selenium.webdriver.support import expected_conditions as EC


# Função para obter a lista de produtos
produtos = obter_lista_produtos()

# Caminho do arquivo Excel
file_path = "C:/Users/Perilo/OneDrive/Documentos/Python/Estoque/Selenium/produto_scrap.xlsx"
workbook = load_workbook(filename=file_path)
sheet = workbook["scrap"]

# Configurações do Navegador
service = Service(executable_path="Selenium/msedgedriver.exe")
edge_options = Options()
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--disable-notifications")
edge_options.add_argument("--inprivate")

# Inicialização do WebDriver
driver = webdriver.Edge(service=service, options=edge_options)

# Abrindo a página do Mercado Livre
driver.get("https://www.mercadolivre.com.br/")
time.sleep(5)

# Loop para buscar cada produto na lista
for i, produto in enumerate(produtos):
    try:
        time.sleep(3)
        # Busca pelo produto
        input_box = driver.find_element(By.NAME, "as_word")
        input_box.clear()
        input_box.send_keys(produto + Keys.RETURN)
        
        time.sleep(5)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-search-result__content-wrapper"))
        ).click()
            
        try: 
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-search-item__group--title a"))
            ).click()
        except: 
            pass

        # Obtém título e preço
        titulo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ui-pdp-title"))
        ).text

        preco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".andes-money-amount__fraction"))
        ).text

        # Escreve no Excel o título e o preço
        sheet[f'A{i+2}'] = titulo
        sheet[f'B{i+2}'] = preco

        # Obtém a URL da imagem
        imagem_url = driver.find_element(By.CSS_SELECTOR, ".ui-pdp-gallery__figure__image").get_attribute("src")

        # Baixa a imagem
        img_data = requests.get(imagem_url).content
        img_pil = PILImage.open(BytesIO(img_data))

        if img_pil.format == "WEBP":
            buffer = BytesIO()
            img_pil.save(buffer, format="PNG")
            img_data = buffer.getvalue()
            img_pil = PILImage.open(BytesIO(img_data))  # Reabre a imagem após a conversão para PNG

        add_image_to_cell(sheet, img_data, col=2, row=i+1, col_span=1, row_span=1)  # Ajusta a imagem corretamente
        
        print(f"Produto: {titulo} | Preço: R${preco} | Imagem: {imagem_url}")

    except Exception as e:
        print(f"Erro ao buscar '{produto}': {e}")
        sheet[f'A{i+2}'] = produto
        sheet[f'B{i+2}'] = "Erro ao buscar o produto"
        sheet[f'C{i+2}'] = "Imagem não disponível"

# Tenta salvar o arquivo Excel
try:
    workbook.save("lista_produtos.xlsx")
    print("Arquivo Excel salvo com sucesso.")
except Exception as e:
    print(f"Erro ao salvar o arquivo Excel: {e}")

# Fecha o navegador
driver.quit()
