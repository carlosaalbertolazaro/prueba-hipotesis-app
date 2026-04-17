import streamlit as st

st.set_page_config(page_title="Prueba de Hipótesis", layout="wide")

st.title("📊 App de Prueba de Hipótesis")
st.markdown("Unidad 03 — Probabilidad y Estadística 2026")

menu = st.sidebar.radio("Módulos", [
    "🏠 Inicio",
    "📂 Carga de Datos",
    "📈 Visualización",
    "🔬 Prueba Z",
    "🤖 Asistente IA"
])

if menu == "🏠 Inicio":
    st.header("Bienvenido")
    st.write("Usa el menú lateral para navegar entre los módulos.")
    st.info("Esta app nos permite visualizar distribuciones y realizar pruebas de hipótesis con apoyo de IA(Gemini).")

elif menu == "📂 Carga de Datos":
    st.header("📂 Carga de Datos")
    st.write("Módulo en desarrollo...")

elif menu == "📈 Visualización":
    st.header("📈 Visualización de Distribución")
    st.write("Módulo en desarrollo...")

elif menu == "🔬 Prueba Z":
    st.header("🔬 Prueba de Hipótesis Z")
    st.write("Módulo en desarrollo")

elif menu == "🤖 Asistente IA":
    st.header("🤖 Asistente Estadístico con IA")
    st.write("Módulo en desarrollo")