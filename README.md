
# Fatura Fácil Araçatuba (Web)

App web para leitura e controle de faturas CPFL da Prefeitura de Araçatuba, feito com Streamlit.

## Funcionalidades

- Upload de faturas em PDF
- Extração de dados principais (vencimento, valor, IOF, etc.)
- Armazenamento em banco de dados SQLite
- Evita duplicatas (chave: número da conta)
- Geração de texto padrão para 1Doc

## Como usar

1. Faça upload do PDF da fatura
2. Veja os dados extraídos
3. Salve no banco de dados automaticamente
4. Copie o texto gerado para o 1Doc

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ou suba o repositório no [Streamlit Cloud](https://streamlit.io/cloud).
