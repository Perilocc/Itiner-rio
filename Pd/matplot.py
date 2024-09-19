import matplotlib.pyplot as plt

# Gráfico de pizza dos custos e despesas
labels = ['Custo', 'Despesas Operacionais', 'Impostos', 'Lucro Líquido']
valores = [custos, despesas, impostos, lucro_liquido]

plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.title('Distribuição de Despesas e Lucro')
plt.show()
