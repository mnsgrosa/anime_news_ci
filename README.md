# RAG anime synopsis

Projeto para demonstracao de adicao de pequenos chunks de textos por tamanho fixo em base de dado
vetorial. Aqui acessaremos a api JIKAN para obter sinopses de animes e armazenar em um banco,
com o client httpx iremos fazer os requests a API e armazenaremos as sinopses no banco de dados gcp
que qualquer alteracao feita no repositorio ira acionar o gitactions e refazer o deploy das dags.

## Como funciona?

O airflow ira disparar uma DAG que fara requisicoes a API JIKAN para obter sinopses de animes e
estara hospedado no Google Cloud Run. As sinopses serao armazenadas em um banco de dados vetorial
a LLM ira acessar esse banco para responder perguntas relacionadas as sinopses dos animes.
A cada nova temporada ele ira acessar a API com os dados da proxima temporada. Teremos 3 bancos
Animes de temporadas anteriores, animes da temporada atual e animes da proxima temporada.

## Requisitos

Gerenciador de pacotes uv

```
- Python 3.12
- Apache Airflow
- httpx
- apache-airflow["google"]
- Google cloud aiplatform
- Streamlit
```

## Configuração do Ambiente

Utilizando o gerenciador de pacote UV basta executar

```
uv venv . --python==3.12
uv venv init .
uv sync
```

Agora e necessario configurar as variaveis de ambiente do google cloud basta executar o config.py

```
uv run config.py
```

E por fim rodar o docker para rodar o streamlit e usar a llm
