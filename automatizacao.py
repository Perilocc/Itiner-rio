import pyautogui as gui
from openpyxl import load_workbook
import time
import pyperclip  # Piperclip para pegar acentuação

def extrair_dados():
    file_path =  "C:/Users/Perilo/OneDrive/Documentos/Python/Estoque/Produtos.xlsx"
    workbook = load_workbook(filename=file_path)
    sheet = workbook["prod"]
    lista_dicts = []
    for i in range(9):
        nome = sheet[f"A{i + 2}"].value
        descricao = sheet[f"B{i + 2}"].value
        qtd = sheet[f"C{i + 2}"].value
        custo = sheet[f"D{i + 2}"].value
        preco = sheet[f"E{i + 2}"].value
        
        dados = {
            "nome": nome,
            "descricao": descricao,
            "qtd": qtd,
            "custo": custo,
            "preco": preco
        }
        
        lista_dicts.append(dados)
    print(lista_dicts)    
    return lista_dicts
    
dados = extrair_dados()

def automatizacao(dados):
    for i, dado in enumerate(dados):
        
        nome = dado["nome"]
        descricao = dado["descricao"]
        qtd = dado["qtd"]
        custo = dado["custo"]
        preco = dado["preco"]
        
        
        print(f"\nProduto: {i+1}")
        print(f"Nome: {nome}, Descrição: {descricao}, Custo: {custo}, Preço: {preco}, Quantidade: {qtd}")
        
        time.sleep(5)
        if i == 0:
            gui.hotkey('alt', 'tab')
            time.sleep(2)
        
        gui.press('tab')
        gui.press('enter')
        gui.click()
        time.sleep(2)
        
        gui.press('tab')
        pyperclip.copy(nome)
        gui.hotkey('ctrl', 'v')
        time.sleep(1)

        gui.press('tab')
        pyperclip.copy(descricao)
        gui.hotkey('ctrl', 'v')
        time.sleep(1)

        gui.press('tab')
        pyperclip.copy(str(custo))
        gui.hotkey('ctrl', 'v')
        time.sleep(1)

        gui.press('tab')
        pyperclip.copy(str(preco))
        gui.hotkey('ctrl', 'v')
        time.sleep(2)

        gui.press('tab')
        pyperclip.copy(str(qtd))
        gui.hotkey('ctrl', 'v')
        time.sleep(1)
        
        gui.press('tab')
        gui.press('enter')
    print("Todos os itens foram Cadastrados")

automatizacao(dados)