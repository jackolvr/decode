import streamlit as st
import json

st.title("Decodificador de Unicode Escape para ISO-8859-1")

# Área para inserção do texto com sequências Unicode
texto = st.text_area("Insira o texto com sequências Unicode:")

if st.button("Decodificar"):
    try:
        # Caso o usuário tenha inserido escapes duplicados, converte-os para simples
        texto_corrigido = texto.replace('\\\\', '\\')
        # Usa json.loads para decodificar as sequências Unicode
        texto_decodificado = json.loads(f'"{texto_corrigido}"')
        # Se necessário, converte o resultado para ISO-8859-1; porém como a string já é Unicode,
        # isso só seria útil se você precisar de bytes posteriormente.
        st.success("Texto decodificado:")
        st.text(texto_decodificado)
    except Exception as e:
        st.error(f"Ocorreu um erro na decodificação: {e}")
