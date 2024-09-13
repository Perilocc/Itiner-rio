import pyautogui as gui
from openpyxl import load_workbook

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

dados = extrair_dados()

def automatizacao(dados):
    for dado in dados:
        
        pass