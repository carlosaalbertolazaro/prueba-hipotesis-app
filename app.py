import streamlit as st

st.set_page_config(page_title="Prueba de Hipótesis", layout="wide")

# estilo del siderbar (Menos simple)
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #000000;
}
[data-testid="stSidebarContent"] * {
    color: white !important;
}
div.stButton > button {
    background-color: #000000 !important;
    color: white !important;
    border: 2px solid white !important;
    border-radius: 12px !important;
    padding: 14px 0 !important;
    margin-bottom: 8px !important;
    width: 100% !important;
    font-size: 15px !important;
    transition: background 0.2s;
}
div.stButton > button:hover {
    background-color: #222222 !important;
    border-color: #aaaaaa !important;
}
</style>
""", unsafe_allow_html=True)

# --- Estado del menú ---
if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"

opciones = {
    "Inicio": "🏠",
    "Carga de Datos": "📂",
    "Visualización": "📈",
    "Prueba Z": "🔬",
    "Asistente IA": "🤖",
}

with st.sidebar:
    st.markdown("### Menú")
    for nombre, icono in opciones.items():
        if st.button(f"{icono}\n{nombre}", key=nombre, use_container_width=True):
            st.session_state.pagina = nombre

pagina = st.session_state.pagina

# Contenidos por pagina

if pagina == "Inicio":
    st.title("📊 App de Prueba de Hipótesis")
    st.markdown("Probabilidad y Estadística")
    st.info("Usa el menú lateral para navegar entre los módulos.")

elif pagina == "Carga de Datos":
    st.header("📂 Carga de Datos")
    st.write("Módulo en desarrollo")

elif pagina == "Visualización":
    st.header("📈 Visualización de Distribución")
    st.write("Módulo en desarrollo")

elif pagina == "Prueba Z":
    st.header("🔬 Prueba de Hipótesis Z")
    st.write("Módulo en desarrollo")

elif pagina == "Asistente IA":
    st.header("🤖 Asistente Estadístico con IA")
    st.write("Módulo en desarrollo")