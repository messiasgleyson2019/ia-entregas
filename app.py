import streamlit as st
import pandas as pd

# 1. Configuração da Página (Título na aba e Layout largo)
st.set_page_config(
    page_title="Shopee SPX - Gestão de Entregas",
    page_icon="🚚",
    layout="wide"
)

# 2. Estilo Customizado (Cores da Shopee)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; background-color: #ee4d2d; color: white; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_name=True)

# 3. Barra Lateral Organizada
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Shopee.svg", width=150)
    st.title("Painel de Controle")
    uploaded_file = st.file_uploader("📂 Importar planilha de entregas", type=["xlsx", "csv"])
    st.info("Dica: Use arquivos .xlsx padrão do sistema SPX.")

# 4. Cabeçalho Principal
st.title("🚚 App de Entregas - Shopee SPX")
st.subheader("Gerenciamento de Fluxo e Roteirização")

# 5. Seção de Métricas (Aparência de Dashboard)
col1, col2, col3, col4 = st.columns(4)

if uploaded_file is not None:
    try:
        # Lendo os dados
        df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('xlsx') else pd.read_csv(uploaded_file)
        
        # Exibindo métricas fictícias (ou baseadas no seu DF)
        col1.metric("Total de Pacotes", len(df))
        col2.metric("Rotas Geradas", "12")
        col3.metric("Motoristas", "8")
        col4.metric("Status", "Processado ✅")

        st.divider()

        # 6. Exibição dos Dados com Filtro
        st.write("### 📋 Visualização dos Dados")
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    col1.metric("Total de Pacotes", "-")
    col2.metric("Rotas Geradas", "-")
    col3.metric("Motoristas", "-")
    col4.metric("Status", "Aguardando...")
    st.warning("⚠️ Por favor, suba uma planilha na barra lateral para começar.")


