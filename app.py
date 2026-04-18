import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from sentiment_analyzer.models.huggingface_provider import HuggingFaceAnalyzer
from sentiment_analyzer.core.services import SentimentBatchService

# --- Configurações Visuais ---
st.set_page_config(page_title="Sentimentalize AI", layout="wide", page_icon="🧠")

# Estilo CSS personalizado para melhorar o visual
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_analyzer():
    return HuggingFaceAnalyzer()

analyzer = load_analyzer()
service = SentimentBatchService(analyzer)

# --- Cabeçalho ---
st.title("🧠 Sentimentalize AI")
st.subheader("Análise Inteligente de Feedbacks e Redes Sociais")
st.divider()

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=100)
    st.title("Configurações")
    uploaded_file = st.file_uploader("📂 Upload de Base de Dados (CSV)", type="csv")
    
    st.info("Dica: Use colunas que contenham comentários de clientes ou redes sociais.")

if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    col_text = st.sidebar.selectbox("Selecione a coluna para análise", df_raw.columns)
    
    if st.sidebar.button("🚀 Iniciar Processamento"):
        with st.spinner("Nossa IA está lendo os dados..."):
            # Processamento
            df_raw.to_csv("temp.csv", index=False)
            df_result = service.process_csv("temp.csv", col_text)
            
            # --- Painel de Métricas ---
            m1, m2, m3 = st.columns(3)
            m1.metric("Total Analisado", f"{len(df_result)} linhas")
            
            most_frequent = df_result['sentiment_label'].mode()[0]
            sentiment_map = {"POS": "😊 Positivo", "NEG": "😡 Negativo", "NEU": "😐 Neutro"}
            m2.metric("Sentimento Predominante", sentiment_map.get(most_frequent))
            
            avg_conf = df_result['sentiment_score'].mean()
            m3.metric("Confiança Média", f"{avg_conf:.2%}")

            st.divider()

            # --- Gráficos e Tabelas ---
            c1, c2 = st.columns([1, 2])
            
            with c1:
                st.write("### 📊 Proporção")
                # O parâmetro correto é color_discrete_map
                fig = px.pie(df_result, names='sentiment_label', hole=0.4, 
                             color='sentiment_label',
                             color_discrete_map={"POS": "#00CC96", "NEG": "#EF553B", "NEU": "#636EFA"})
                st.plotly_chart(fig, use_container_width=True)
            with c2:
                st.write("### 📋 Resultados Detalhados")
                # Mostramos apenas colunas relevantes para não poluir
                st.dataframe(df_result[[col_text, 'text_cleaned', 'sentiment_label', 'sentiment_score']], use_container_width=True)
            
            # Download
            csv = df_result.to_csv(index=False).encode('utf-8')
            st.download_button("💾 Baixar Relatório Completo", csv, "relatorio_sentimentos.csv", "text/csv")