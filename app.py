
import streamlit as st
import fitz  # PyMuPDF
import pandas as pd
from utils.extrator_cpfl import extrair_dados_fatura
import sqlite3
import os

st.set_page_config(page_title="Fatura Fácil Araçatuba", layout="centered")

st.title("⚡ Fatura Fácil Araçatuba - Web")

uploaded_file = st.file_uploader("Envie uma fatura CPFL em PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with fitz.open("temp.pdf") as doc:
        texto = ""
        for page in doc:
            texto += page.get_text()

    dados = extrair_dados_fatura(texto)

    if dados:
        st.subheader("📋 Dados extraídos")
        st.write(dados)

        # Conexão e inserção no banco de dados
        conn = sqlite3.connect("faturas.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faturas (
                numero_conta TEXT PRIMARY KEY,
                nome_unidade TEXT,
                numero_instalacao TEXT,
                vencimento TEXT,
                valor_total REAL,
                iof REAL,
                competencia TEXT
            )
        """)
        try:
            cursor.execute("""
                INSERT INTO faturas VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                dados["numero_conta"],
                dados["nome_unidade"],
                dados["numero_instalacao"],
                dados["vencimento"],
                dados["valor_total"],
                dados["iof"],
                dados["competencia"]
            ))
            conn.commit()
            st.success("✅ Dados salvos com sucesso no banco de dados.")
        except sqlite3.IntegrityError:
            st.warning("⚠️ Esta fatura já foi registrada anteriormente.")
        conn.close()

        st.subheader("📝 Texto padrão para 1Doc")
        texto_1doc = f'''
Informamos o lançamento da fatura de energia elétrica da unidade **{dados["nome_unidade"]}**, instalação nº {dados["numero_instalacao"]}, com vencimento em {dados["vencimento"]}, no valor de R$ {dados["valor_total"]:.2f}.
'''
        st.code(texto_1doc, language="markdown")

    else:
        st.error("❌ Não foi possível extrair os dados do PDF.")
