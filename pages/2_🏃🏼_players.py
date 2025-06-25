# Importa a biblioteca Streamlit
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Players",  # Título da aba do navegador
    page_icon="🏃🏼",        # Ícone da aba
    layout="wide"          # Layout da página (mais largo)
)
# Recupera o DataFrame de dados do estado da sessão
# (deve ser carregado na página principal antes)
df_data = st.session_state["data"]

# Lista de clubes disponíveis para seleção
clubes = df_data["Club"].value_counts().index
# Seleciona o clube na barra lateral
club = st.sidebar.selectbox("Clube", clubes)

# Filtra os jogadores do clube selecionado
df_players = df_data[(df_data["Club"] == club)]
# Lista de jogadores do clube
players = df_players["Name"].value_counts().index
# Seleciona o jogador na barra lateral
player = st.sidebar.selectbox("Jogador", players)

# Recupera as estatísticas do jogador selecionado
player_stats = df_data[df_data["Name"] == player].iloc[0]

# Exibe a foto e o nome do jogador
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

# Exibe informações básicas do jogador
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# Exibe idade, altura e peso em colunas
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

# Exibe o Overall do jogador com barra de progresso
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

# Taxas de conversão de libra para dólar e real
GBP_TO_USD = 1.27
GBP_TO_BRL = 6.50

# Recupera valores financeiros do jogador
valor = player_stats['Value(£)']
wage = player_stats['Wage(£)']
clause = player_stats['Release Clause(£)']

# Exibe métricas financeiras em diferentes moedas
col1.metric(label="Valor de mercado", value=f"£ {valor:,}")
col1.markdown(f"**Dólar:** $ {valor * GBP_TO_USD:,.2f}")
col1.markdown(f"**Real:** R$ {valor * GBP_TO_BRL:,.2f}")

col2.metric(label="Remuneração semanal", value=f"£ {wage:,}")
col2.markdown(f"**Dólar:** $ {wage * GBP_TO_USD:,.2f}")
col2.markdown(f"**Real:** R$ {wage * GBP_TO_BRL:,.2f}")

col3.metric(label="Cláusula de rescisão", value=f"£ {clause:,}")
col3.markdown(f"**Dólar:** $ {clause * GBP_TO_USD:,.2f}")
col3.markdown(f"**Real:** R$ {clause * GBP_TO_BRL:,.2f}")