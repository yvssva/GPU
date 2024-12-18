import numpy as np
import cupy as cp
import pandas as pd
import matplotlib.pyplot as plt
import time

# Carregar os dados do Excel
file_path = r'C:\VALORES UTFPR\data.xlsx'
data = pd.read_excel(file_path, header=1)

# Lista de colunas que representam os inversores
inversores = [
    'Inversor A - Potência CA',
    'Inversor B - Potência CA',
    'Inversor C - Potência CA',
    'Inversor D - Potência CA',
    'Inversor E - Potência CA',
    'Inversor F - Potência CA',
    'Inversor G - Potência CA'
]

# Bins para o histograma
bins = cp.linspace(0, 60000, 31)

# Inicializar os tempos de execução
cpu_times = []
gpu_times = []

# Criar os subplots
fig, axs = plt.subplots(len(inversores), 1, figsize=(10, len(inversores) * 5))

# Processar cada inversor
for i, inversor in enumerate(inversores):
    # Verificar se a coluna existe
    if inversor in data.columns:
        print(f"Processando {inversor}...")  # Depuração
        # Extrair os dados de potência de cada inversor
        potencia = data[inversor].dropna().values  # Remover NaNs

        # ================== Execução no CPU ==================
        start_time_cpu = time.time()
        hist_cpu, _ = np.histogram(potencia, bins=bins.get())  # Usando numpy no CPU
        end_time_cpu = time.time()
        cpu_time = end_time_cpu - start_time_cpu
        cpu_times.append(cpu_time)

        # ================== Execução no GPU ==================
        potencia_gpu = cp.asarray(potencia)  # Mover os dados para a GPU
        start_time_gpu = time.time()
        hist_gpu = cp.histogram(potencia_gpu, bins=bins)[0]  # Usando cupy na GPU
        end_time_gpu = time.time()
        gpu_time = end_time_gpu - start_time_gpu
        gpu_times.append(gpu_time)

        # ================== Plotando os gráficos ==================
        # Conversão explícita de bins para NumPy
        bins_cpu = bins.get()  # Converte os bins para NumPy

        # Plot no CPU
        axs[i].bar(bins_cpu[:-1], hist_cpu, width=1000, edgecolor='black', alpha=0.6, label='CPU')  # Bar plot CPU

        # Plot no GPU
        axs[i].bar(bins_cpu[:-1], hist_gpu.get(), width=1000, edgecolor='black', alpha=0.6, label='GPU')  # Bar plot GPU

        axs[i].set_title(f'Histograma - {inversor}')
        axs[i].set_xlabel('Potência CA')
        axs[i].set_ylabel('Frequência')
        axs[i].set_xlim(0, 60000)
        axs[i].grid(True)
        axs[i].legend()

    else:
        print(f"Coluna '{inversor}' não encontrada.")

# Mostrar os gráficos
plt.tight_layout()
plt.show()

# Imprimir os tempos de execução
print("\nTempos de execução:")
for i, inversor in enumerate(inversores):
    print(
        f"{inversor}: CPU = {cpu_times[i]:.6f}s, GPU = {gpu_times[i]:.6f}s, Diferença = {cpu_times[i] - gpu_times[i]:.6f}s")
