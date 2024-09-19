import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

df = pd.read_excel('Pd\dados_contabeis.xlsx')

receita_liquida = df['Receita'].sum()
custos = df['Custo'].sum()
despesas = df['Despesas'].sum()
impostos = df['Impostos'].sum()


lucro_bruto = receita_liquida - custos
lucro_operacional = lucro_bruto - despesas
lucro_liquido = lucro_operacional - impostos


dre = pd.DataFrame({
    'Receita Líquida': [receita_liquida],
    'Custo': [custos],
    'Lucro Bruto': [lucro_bruto],
    'Despesas Operacionais': [despesas],
    'Lucro Operacional': [lucro_operacional],
    'Impostos': [impostos],
    'Lucro Líquido': [lucro_liquido]
})

labels = ['Custo', 'Despesas Operacionais', 'Impostos', 'Lucro Líquido']
valores = [custos, despesas, impostos, lucro_liquido]

plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.title('Distribuição de Despesas e Lucro')

plt.savefig('grafico_pizza.png')
plt.show()
plt.close()

wb = load_workbook('dre_gerada.xlsx')
ws = wb.active 

img = Image('grafico_pizza.png')
ws.add_image(img, 'H2') 

# Salvar o arquivo Excel com o gráfico inserido
wb.save('dre_gerada_com_grafico.xlsx')

print("Relatório DRE gerado com gráfico no Excel!")