import pandas as pd
import cupy as cp
import matplotlib.pyplot as plt

# Caminho do arquivo atualizado
file_path = 'C:/VALORES UTFPR/data.xlsx'

# Carregar os dados com pandas, agora considerando que os cabeçalhos estão na linha 2 (índice 1)
data = pd.read_excel(file_path, header=1)

# Verificar as primeiras linhas para entender a estrutura
print(data.head())

# Definir o intervalo do histograma
bins = cp.arange(0, 60001, 1000)  # De 0 até 60.000 com intervalo de 1.000

# Inicializar a plotagem
fig, axs = plt.subplots(3, 2, figsize=(12, 10))  # Para 6 inversores, 3x2 subplots
axs = axs.ravel()  # Flatten para facilitar o acesso às subplots

# Processar e gerar histograma para cada inversor
inversores = ['Inversor A - Potência CA', 'Inversor B - Potência CA',
              'Inversor C - Potência CA', 'Inversor D - Potência CA',
              'Inversor E - Potência CA', 'Inversor F - Potência CA']

for i, inversor in enumerate(inversores):
    # Verificar se a coluna existe
    if inversor in data.columns:
        # Extrair os dados de potência de cada inversor
        potencia = data[inversor].dropna().values  # Remover NaNs
        potencia_gpu = cp.asarray(potencia)  # Mover os dados para a GPU

        # Calcular o histograma
        hist = cp.histogram(potencia_gpu, bins=bins)[0]

        # Plotar o histograma (convertendo os dados para numpy usando .get())
        axs[i].bar(bins[:-1].get(), hist.get(), width=1000, edgecolor='black')  # .get() traz os dados de volta para a CPU
        axs[i].set_title(f'Histograma - {inversor}')
        axs[i].set_xlabel('Potência CA')
        axs[i].set_ylabel('Frequência')
        axs[i].set_xlim(0, 60000)
        axs[i].grid(True)
    else:
        print(f"Coluna '{inversor}' não encontrada.")

# Exibir o gráfico
plt.tight_layout()
plt.show()
