# 🤖 Agente de Análise Exploratória de Dados (Agente EDA)

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.2+-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Este projeto consiste em um agente de Inteligência Artificial desenvolvido como parte da atividade do [I2A2](https://i2a2.academy/). 
O objetivo é fornecer uma ferramenta de Análise Exploratória de Dados (E.D.A.) genérica, capaz de analisar qualquer arquivo CSV, responder perguntas em linguagem natural, gerar gráficos e extrair conclusões valiosas.

## ✨ Funcionalidades

* **Análise de Qualquer Arquivo CSV:** Faça o upload de qualquer arquivo CSV e comece a analisar instantaneamente.
* **Respostas em Linguagem Natural:** Faça perguntas complexas sobre os dados como se estivesse conversando com um analista.
* **Geração de Gráficos:** Solicite histogramas, gráficos de barras, gráficos de dispersão e mais. O agente gera e exibe as visualizações.
* **Análise Estatística:** Obtenha descrições dos dados, medidas de tendência central (média, mediana), variabilidade (desvio padrão) e correlações.
* **Detecção de Anomalias:** Identifique outliers e padrões incomuns nos dados.
* **Interface Web Interativa:** Uma interface amigável construída com Streamlit para facilitar a interação.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Streamlit:** Framework para a criação da interface web.
* **LangChain:** Framework para o desenvolvimento do agente de IA.
* **Google Gemini:** Modelo de Linguagem (LLM) que alimenta o agente.
* **Pandas:** Biblioteca para manipulação e análise dos dados.
* **Matplotlib & Seaborn:** Bibliotecas para a geração dos gráficos.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o agente na sua máquina local.

### Pré-requisitos

* [Python](https://www.python.org/downloads/) (versão 3.9 ou superior)
* [Git](https://git-scm.com/downloads)

### 1. Clonar o Repositório

```bash
git clone [https://github.com/ArthurRG23/agente-eda.git](https://github.com/ArthurRG23/agente-eda.git)
cd agente-eda
```

### 2. Configurar ambiente virtual

# Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate


### 3. Instalar as Dependências

pip install -r requirements.txt

### 4. Configurar a Chave de API

O agente precisa de uma chave de API do Google para funcionar.

    Crie um arquivo chamado .env na raiz do projeto.

    Dentro deste arquivo, adicione sua chave de API da seguinte forma:

    GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"

### 5. Executar a Aplicação

streamlit run app.py

Acesse http://localhost:8501 no seu navegador para começar a usar o agente.

📈 Como Usar

    Faça o Upload: Arraste e solte um arquivo CSV ou clique para procurar em seus arquivos.

    Aguarde a Análise: O agente exibirá uma amostra dos dados carregados.

    Faça Perguntas: Utilize a caixa de chat na parte inferior para fazer perguntas em português.

Exemplos de Perguntas:

    Quais são os tipos de dados de cada coluna?

    Liste as 5 transações com o maior valor na coluna 'Amount'.

    Crie um histograma para a coluna 'Time' para visualizar sua distribuição.

    Qual a correlação entre as colunas V1, V2 e Amount?

    Com base nas análises, quais conclusões você pode tirar sobre esses dados? 

📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
