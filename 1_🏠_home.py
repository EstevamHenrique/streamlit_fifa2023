# Importa as bibliotecas necessárias
import streamlit as st
import pandas as pd
from datetime import datetime 

# Configuração da página do Streamlit
st.set_page_config(
    page_title="FIFA23 Dataset",  # Título da aba do navegador
    page_icon="⚽️",              # Ícone da aba
    layout="wide"                # Layout da página (mais largo)
)

# Carrega os dados apenas uma vez na sessão
if "data" not in st.session_state:
    try:
        # Lê o arquivo CSV com os dados do FIFA23
        df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
        # Filtra jogadores com contrato válido até o ano atual ou posterior
        df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
        # Filtra jogadores com valor maior que zero
        df_data = df_data[df_data["Value(£)"] > 0]
        # Ordena os jogadores pelo atributo 'Overall' (desempenho geral)
        df_data = df_data.sort_values(by="Overall", ascending=False)
        # Salva o DataFrame no estado da sessão
        st.session_state["data"] = df_data
    except Exception as e:
        # Exibe mensagem de erro caso não consiga carregar os dados
        st.error(f"Erro ao carregar os dados: {e}")
        st.stop()

# Título principal da página
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
# Créditos na barra lateral
st.sidebar.markdown("Desenvolvido por [Estevam Henrique](https://www.linkedin.com/in/estevamhenriquefonsecadeoliveira/)")

# Botão para acessar o dataset no Kaggle
if st.button("Acesse os dados no Kaggle"):
    st.markdown("[Clique aqui para acessar os dados no Kaggle](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data)")

# Descrição do conjunto de dados
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)