import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

st.set_page_config(page_title="LotoElite v7 - Etapa 1", layout="wide")

st.title("🎯 LotoElite v7 PRO - Etapa 1")
st.caption("Versão limpa sem sklearn - 50 concursos demo")

@st.cache_data
def carregar_concursos():
    # Gera 50 concursos simulados para teste (substitua depois pela API real)
    np.random.seed(7)
    concursos = []
    base_date = date.today() - timedelta(days=150)
    for i in range(50):
        dezenas = sorted(np.random.choice(range(1, 61), 6, replace=False))
        concursos.append({
            "Concurso": 2700 + i,
            "Data": base_date + timedelta(days=i*3),
            "D1": dezenas[0], "D2": dezenas[1], "D3": dezenas[2],
            "D4": dezenas[3], "D5": dezenas[4], "D6": dezenas[5],
        })
    return pd.DataFrame(concursos)

df = carregar_concursos()

col1, col2, col3 = st.columns(3)
col1.metric("Concursos carregados", len(df))
col2.metric("Dezenas por concurso", 6)
col3.metric("Status", "✅ Online")

st.subheader("Últimos 50 concursos")
st.dataframe(df.sort_values("Concurso", ascending=False), use_container_width=True, height=400)

st.subheader("Frequência das dezenas")
todas = pd.concat([df[f"D{i}"] for i in range(1,7)])
freq = todas.value_counts().sort_index().reset_index()
freq.columns = ["Dezena", "Vezes"]
st.bar_chart(freq.set_index("Dezena"))

st.success("Etapa 1 funcionando! Depois a gente conecta a API real da Mega-Sena.")
