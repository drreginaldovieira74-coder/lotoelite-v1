import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="LotoElite", layout="centered")
st.title("🎯 LotoElite – Mega-Sena Inteligente")
st.success("✅ App funcionando! Etapa 1 concluída.")

st.write("Este é o teste. Se você está vendo isso, o deploy deu certo!")

# Gera 5 jogos exemplo
jogos = []
for i in range(5):
    numeros = sorted(random.sample(range(1,61),6))
    jogos.append(numeros)

df = pd.DataFrame(jogos, columns=[f"N{i+1}" for i in range(6)])
st.dataframe(df, use_container_width=True)

st.info("Próximo passo: vamos buscar os 50 últimos concursos reais da Caixa.")
