# Análise de Dados Temporais de Potência Utilizando Programação em GPU

Este projeto analisa dados temporais de potência gerados por múltiplos inversores em um sistema fotovoltaico. Utilizando a programação em GPU com CuPy, o processamento é acelerado, permitindo a geração de histogramas de potência ao longo do tempo com maior eficiência.

## Contextualização

A análise de grandes volumes de dados temporais é essencial para o monitoramento e otimização de sistemas de energia. Este projeto demonstra a eficiência da programação em GPU para essa finalidade, proporcionando insights rápidos e precisos na otimização de sistemas fotovoltaicos.

## Funcionalidades

- **Download automático** de um arquivo Excel com dados de potência.
- **Leitura e processamento dos dados**, removendo valores nulos.
- **Cálculo de histogramas** de potência utilizando CPU e GPU.
- **Comparação de tempos de execução** entre CPU e GPU.
- **Plotagem de gráficos** para visualização dos histogramas de potência de cada inversor.

## Dependências

O projeto utiliza as seguintes bibliotecas:

- **NumPy**: Operações numéricas em CPU.
- **CuPy**: Operações numéricas otimizadas para GPU.
- **Pandas**: Manipulação e análise de dados.
- **Matplotlib**: Criação de gráficos.
- **Requests**: Download do arquivo de dados da internet.
- **Openpyxl**: Leitura de arquivos Excel.

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/yvssva/GPU
    cd GPU
    ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
    - **Linux/Mac**:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - **Windows**:
      ```powershell
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Instale as dependências**:
    ```bash
    pip install numpy cupy pandas matplotlib requests openpyxl
    ```

## Uso

1. **Execute o script principal**:
    ```bash
    python histograma.py
    ```
   
2. O script irá:
   - Baixar automaticamente o arquivo de dados do GitHub.
   - Carregar e processar os dados, removendo valores inválidos.
   - Calcular histogramas para múltiplos inversores.
   - Comparar os tempos de execução entre CPU e GPU.
   - Gerar gráficos dos histogramas de cada inversor.

3. **Saída esperada**:
   - Histogramas comparativos entre CPU e GPU.
   - Impressão dos tempos de execução para cada inversor.

## Estrutura do Projeto
. ├── histograma.py # Script principal ├── README.md # Este arquivo └── data.xlsx # Arquivo de dados (baixado automaticamente pelo script)


---

Desenvolvido como parte da disciplina **GPU28EE - Computação em GPU** do **Mestrado em Engenharia Elétrica e Computação da UTFPR**.

