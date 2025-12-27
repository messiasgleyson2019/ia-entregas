import streamlit as st
import pandas as pd

st.set_page_config(page_title="IA de Entregas Shopee", page_icon="🚚")
st.title("🚚 App de Entregas – Shopee SPX")

arquivo = st.file_uploader("Importe sua planilha de entregas", type=["csv", "xlsx"])

if arquivo:
    try:
        df = pd.read_excel(arquivo) if arquivo.name.endswith(".xlsx") else pd.read_csv(arquivo)
        st.subheader("📄 Entregas identificadas")
        st.dataframe(df)

        if st.button("🧠 Gerar rota otimizada"):
            enderecos = []
            # Procura por 'RUA' ou 'rua' ou 'ENDEREÇO'
            colunas_alvo = ["RUA", "rua", "ENDEREÇO", "endereco"]
            col_encontrada = next((c for c in colunas_alvo if c in df.columns), None)
            
            if col_encontrada:
                for _, row in df.iterrows():
                    end = str(row[col_encontrada]).strip()
                    if end and end != 'nan':
                        # Formata para o Google Maps
                        enderecos.append(end.replace(" ", "+"))
                
                if enderecos:
                    link_maps = "https://www.google.com/maps/dir/" + "/".join(enderecos)
                    st.success(f"✅ {len(enderecos)} endereços prontos!")
                    st.markdown(f"### 🗺️ [CLIQUE AQUI PARA ABRIR NO GOOGLE MAPS]({link_maps})")
                else:
                    st.error("Coluna encontrada, mas sem endereços válidos.")
            else:
                st.error(f"Não achei a coluna. Verifique se o nome é 'RUA' ou 'ENDEREÇO'.")
    except Exception as e:
        st.error(f"Erro ao ler arquivo: {e}")
        


