# Importa a biblioteca Streamlit
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Players",  # Título da aba do navegador
    page_icon="🏃🏼",        # Ícone da aba
    layout="wide"          # Layout da página (mais largo)
)

# Recupera o DataFrame de dados do estado da sessão
df_data = st.session_state["data"]

# Lista de clubes disponíveis para seleção
clubes = df_data["Club"].value_counts().index
# Seleciona o clube na barra lateral
club = st.sidebar.selectbox("Clube", clubes)

# Filtra os jogadores do clube selecionado e define o nome como índice
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

# Exibe o logo do clube e o nome do clube
st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Define as colunas que serão exibidas na tabela
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

# Exibe a tabela de jogadores do clube com configurações de colunas especiais
st.dataframe(
    df_filtered[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn(
            "Overall", format="%d", min_value=0, max_value=100
        ),
        "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                       min_value=0, max_value=df_filtered["Wage(£)"].max()),
        "Photo": st.column_config.ImageColumn(),
        "Flag": st.column_config.ImageColumn("Country"),
    }
)