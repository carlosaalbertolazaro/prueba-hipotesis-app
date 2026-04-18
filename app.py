import streamlit as st

st.set_page_config(page_title="Prueba de Hipótesis", layout="wide")

st.markdown("""
<style>
/* Fuente y fondo general */
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&display=swap');

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background-color: #020b18 !important;
    color: #e0f7ff !important;
    font-family: 'Rajdhani', sans-serif !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #020b18 !important;
    border-right: 1px solid #00d4ff33 !important;
}
[data-testid="stSidebarContent"] * {
    color: #e0f7ff !important;
}

/* Título del menú */
[data-testid="stSidebar"] h3 {
    color: #00d4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 3px !important;
    font-size: 13px !important;
    text-transform: uppercase;
    margin-bottom: 16px;
}

/* Botones del sidebar */
div.stButton > button {
    background-color: #020b18 !important;
    color: #00d4ff !important;
    border: 1px solid #00d4ff55 !important;
    border-radius: 4px !important;
    padding: 12px 0 !important;
    margin-bottom: 8px !important;
    width: 100% !important;
    font-size: 14px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    transition: all 0.2s !important;
    text-transform: uppercase !important;
}
div.stButton > button:hover {
    background-color: #00d4ff15 !important;
    border-color: #00d4ff !important;
    box-shadow: 0 0 12px #00d4ff44 !important;
    color: #ffffff !important;
}

/* Headers */
h1 { 
    color: #00d4ff !important; 
    font-family: 'Share Tech Mono', monospace !important;
    letter-spacing: 4px !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid #00d4ff33;
    padding-bottom: 10px;
}
h2, h3 { 
    color: #00d4ff !important;
    font-family: 'Rajdhani', sans-serif !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* Métricas */
[data-testid="stMetric"] {
    background-color: #0a1628 !important;
    border: 1px solid #00d4ff33 !important;
    border-radius: 4px !important;
    padding: 12px !important;
}
[data-testid="stMetricLabel"] {
    color: #00d4ff99 !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 22px !important;
}

/* Cajas de info/success/warning/error */
[data-testid="stAlert"] {
    border-radius: 4px !important;
    border-left: 3px solid #00d4ff !important;
    background-color: #0a1628 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 15px !important;
}

/* Inputs y selectbox */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] * {
    background-color: #0a1628 !important;
    color: #e0f7ff !important;
    border-color: #00d4ff44 !important;
    font-family: 'Rajdhani', sans-serif !important;
}

/* Radio buttons */
[data-testid="stRadio"] label {
    color: #e0f7ff !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 15px !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid #00d4ff33 !important;
}

/* Divisor */
hr {
    border-color: #00d4ff22 !important;
}

/* Expander */
[data-testid="stExpander"] {
    background-color: #0a1628 !important;
    border: 1px solid #00d4ff33 !important;
    border-radius: 4px !important;
}

/* Spinner */
[data-testid="stSpinner"] * {
    color: #00d4ff !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #020b18; }
::-webkit-scrollbar-thumb { background: #00d4ff44; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #00d4ff; }
</style>
""", unsafe_allow_html=True)

#Estado del menú 
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
    st.markdown("""
    <div style='text-align:center; padding: 40px 0 20px 0;'>
        <div style='font-family: Share Tech Mono, monospace; font-size: 11px; 
                    color: #00d4ff99; letter-spacing: 6px; text-transform: uppercase;
                    margin-bottom: 8px;'>Sistema de análisis estadístico</div>
        <div style='font-family: Share Tech Mono, monospace; font-size: 36px; 
                    color: #00d4ff; letter-spacing: 8px; text-transform: uppercase;
                    text-shadow: 0 0 20px #00d4ff66;'>PRUEBA DE HIPÓTESIS</div>
        <div style='font-family: Rajdhani, sans-serif; font-size: 14px; 
                    color: #e0f7ff88; letter-spacing: 4px; margin-top: 8px;'>
                    PROBABILIDAD Y ESTADÍSTICA — 2026</div>
    </div>
    <hr style='border-color: #00d4ff33; margin: 30px 0;'/>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MÓDULOS", "5")
    col2.metric("PRUEBAS", "Z-Test")
    col3.metric("IA", "Gemini 2.5")
    col4.metric("STATUS", "ACTIVO")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("▶ Comienza cargando tus datos en el módulo CARGA DE DATOS")

elif pagina == "Carga de Datos":
    st.header("📂 Carga de Datos")

    opcion = st.radio("¿Cómo quieres cargar los datos?", 
                      ["📁 Subir CSV", "🎲 Generar datos sintéticos"],
                      index=0 if "datos" not in st.session_state else 
                            0 if st.session_state.get("fuente") == "csv" else 1)

    if opcion == "📁 Subir CSV":
        archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])
        if archivo:
            import pandas as pd
            df = pd.read_csv(archivo)
            st.session_state.df = df
            st.session_state.fuente = "csv"

        if "df" in st.session_state and st.session_state.get("fuente") == "csv":
            df = st.session_state.df
            st.success(f"Archivo cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
            st.dataframe(df.head(10))
            columnas_numericas = df.select_dtypes(include="number").columns.tolist()
            if columnas_numericas:
                col_actual = st.session_state.get("variable", columnas_numericas[0])
                idx = columnas_numericas.index(col_actual) if col_actual in columnas_numericas else 0
                col_sel = st.selectbox("Selecciona la variable a analizar:", columnas_numericas, index=idx)
                if col_sel != st.session_state.get("variable"):
                    st.session_state.datos = df[col_sel].dropna().tolist()
                    st.session_state.variable = col_sel
                    # Limpiar análisis anteriores al cambiar variable
                    for key in ["sesgo", "p_shapiro", "media", "desv", "n", "resultado_z"]:
                        st.session_state.pop(key, None)
                st.success(f"Variable seleccionada: **{col_sel}** ({len(st.session_state.datos)} observaciones)")
            else:
                st.warning("El CSV no tiene columnas numéricas.")

    elif opcion == "🎲 Generar datos sintéticos":
        import numpy as np
        col1, col2, col3 = st.columns(3)
        with col1:
            media = st.number_input("Media (µ)", value=0.0)
        with col2:
            desv = st.number_input("Desviación estándar (σ)", value=1.0, min_value=0.1)
        with col3:
            n = st.number_input("Tamaño de muestra (n)", value=100, min_value=30, step=10)

        if st.button("Generar datos"):
            datos = np.random.normal(loc=media, scale=desv, size=int(n)).tolist()
            st.session_state.datos = datos
            st.session_state.variable = "Datos sintéticos"
            st.session_state.fuente = "sintetica"
            # Limpiar análisis anteriores al generar nuevos datos
            for key in ["sesgo", "p_shapiro", "media", "desv", "n", "resultado_z"]:
                st.session_state.pop(key, None)
            st.success(f"✅ Generados {int(n)} datos con µ={media} y σ={desv}")
            st.write(f"**Vista previa:** {[round(x,2) for x in datos[:10]]}...")

    # Mostrar resumen si ya hay datos cargados
    if "datos" in st.session_state:
        st.markdown("---")
        st.info(f"📌 Datos activos: **{st.session_state.variable}** — {len(st.session_state.datos)} observaciones. Navega a Visualización o Prueba Z cuando quieras.")

elif pagina == "Visualización":
    st.header("📈 Visualización de Distribución")

    if "datos" not in st.session_state:
        st.warning("⚠️ Primero carga o genera datos en el módulo de Carga de Datos.")
    else:
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import stats

        datos = np.array(st.session_state.datos)
        variable = st.session_state.variable

        # --- Cálculos primero ---
        sesgo = stats.skew(datos)
        curtosis = stats.kurtosis(datos)
        stat_sw, p_sw = stats.shapiro(datos[:50] if len(datos) > 50 else datos)
        q1, q3 = np.percentile(datos, [25, 75])
        iqr = q3 - q1
        outliers = datos[(datos < q1 - 1.5*iqr) | (datos > q3 + 1.5*iqr)]

        # --- Guardar en session_state ---
        st.session_state.media = float(np.mean(datos))
        st.session_state.desv = float(np.std(datos))
        st.session_state.n = len(datos)
        st.session_state.sesgo = float(sesgo)
        st.session_state.p_shapiro = float(p_sw)

        st.subheader(f"Variable: `{variable}` — {len(datos)} observaciones")

        # --- Estadísticas básicas ---
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Media", f"{np.mean(datos):.4f}")
        col2.metric("Desv. Estándar", f"{np.std(datos):.4f}")
        col3.metric("Mínimo", f"{np.min(datos):.4f}")
        col4.metric("Máximo", f"{np.max(datos):.4f}")

        st.markdown("---")

        # --- Histograma ---
        st.subheader("Histograma con curva normal")
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.set_facecolor("#000000")
        fig1.patch.set_facecolor("#000000")
        ax1.hist(datos, bins=20, density=True, color="#7c3aed", edgecolor="white", alpha=0.8, label="Datos")
        xmin, xmax = ax1.get_xlim()
        x = np.linspace(xmin, xmax, 200)
        p = stats.norm.pdf(x, np.mean(datos), np.std(datos))
        ax1.plot(x, p, "w--", linewidth=2, label="Curva normal")
        ax1.tick_params(colors="white")
        ax1.xaxis.label.set_color("white")
        ax1.yaxis.label.set_color("white")
        for spine in ax1.spines.values():
            spine.set_edgecolor("white")
        ax1.legend(facecolor="#1e1e1e", labelcolor="white")
        st.pyplot(fig1)

        # --- Boxplot ---
        st.subheader("Boxplot")
        fig2, ax2 = plt.subplots(figsize=(8, 2))
        ax2.set_facecolor("#000000")
        fig2.patch.set_facecolor("#000000")
        ax2.boxplot(datos, vert=False, patch_artist=True,
                    boxprops=dict(facecolor="#7c3aed", color="white"),
                    medianprops=dict(color="white", linewidth=2),
                    whiskerprops=dict(color="white"),
                    capprops=dict(color="white"),
                    flierprops=dict(markerfacecolor="white", marker="o"))
        ax2.tick_params(colors="white")
        for spine in ax2.spines.values():
            spine.set_edgecolor("white")
        st.pyplot(fig2)

        st.markdown("---")

        # --- Análisis automático ---
        st.subheader("🔍 Análisis automático")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sesgo", f"{sesgo:.4f}")
        with col2:
            st.metric("p-value Shapiro-Wilk", f"{p_sw:.4f}")

        st.markdown("---")
        st.subheader("❓ Preguntas de diagnóstico")

        st.markdown("**¿La distribución parece normal?**")
        if p_sw > 0.05 and abs(sesgo) < 0.5:
            st.success("✅ Sí — p-value > 0.05 y sesgo bajo. La distribución se comporta aproximadamente normal.")
        elif p_sw > 0.05 and abs(sesgo) >= 0.5:
            st.warning("⚠️ Parcialmente — El p-value sugiere normalidad pero hay sesgo considerable.")
        else:
            st.error("❌ No — p-value ≤ 0.05, la distribución no es normal.")

        st.markdown("---")

        st.markdown("**¿Hay sesgo?**")
        if abs(sesgo) < 0.5:
            st.success(f"✅ No hay sesgo significativo (sesgo = {sesgo:.4f}). Distribución aproximadamente simétrica.")
        elif sesgo > 0.5:
            st.warning(f"↗️ Sesgo positivo (sesgo = {sesgo:.4f}). Cola hacia la derecha.")
        else:
            st.warning(f"↙️ Sesgo negativo (sesgo = {sesgo:.4f}). Cola hacia la izquierda.")

        st.markdown("---")

        st.markdown("**¿Hay outliers?**")
        if len(outliers) == 0:
            st.success(f"✅ No se detectaron outliers en `{variable}`.")
        elif len(outliers) <= 3:
            st.warning(f"⚠️ {len(outliers)} outlier(s) detectado(s): {[round(float(o), 4) for o in outliers]}")
        else:
            st.error(f"❌ {len(outliers)} outliers detectados. Puede afectar los resultados de la prueba Z.")

elif pagina == "Prueba Z":
    st.header("🔬 Prueba de Hipótesis Z")

    if "datos" not in st.session_state:
        st.warning("⚠️ Primero carga o genera datos en el módulo de Carga de Datos.")
    else:
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy import stats

        datos = np.array(st.session_state.datos)
        media_muestral = float(np.mean(datos))
        n = len(datos)

        st.markdown(" Parámetros de la prueba")

        col1, col2 = st.columns(2)
        with col1:
            mu0 = st.number_input("Hipótesis nula H₀: µ =", value=0.0)
            sigma = st.number_input("Desviación estándar poblacional (σ)", value=1.0, min_value=0.01)
        with col2:
            alpha = st.selectbox("Nivel de significancia (α)", [0.01, 0.05, 0.10], index=1)
            tipo = st.selectbox("Tipo de prueba", ["Bilateral (≠)", "Cola izquierda (<)", "Cola derecha (>)"])

        st.markdown("---")
        st.markdown(" Resultados")

        # Cálculo del estadístico Z
        Z = (media_muestral - mu0) / (sigma / np.sqrt(n))

        # p-value según tipo de prueba
        if tipo == "Bilateral (≠)":
            p_value = 2 * (1 - stats.norm.cdf(abs(Z)))
            z_critico = stats.norm.ppf(1 - alpha / 2)
            rechaza = abs(Z) > z_critico
        elif tipo == "Cola izquierda (<)":
            p_value = stats.norm.cdf(Z)
            z_critico = -stats.norm.ppf(1 - alpha)
            rechaza = Z < z_critico
        else:
            p_value = 1 - stats.norm.cdf(Z)
            z_critico = stats.norm.ppf(1 - alpha)
            rechaza = Z > z_critico

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Media muestral (x̄)", f"{media_muestral:.4f}")
        col2.metric("Estadístico Z", f"{Z:.4f}")
        col3.metric("p-value", f"{p_value:.4f}")
        col4.metric("Z crítico", f"{z_critico:.4f}")

        if rechaza:
            st.error(f"❌ Se RECHAZA H₀ — El estadístico Z={Z:.4f} cae en la región de rechazo (α={alpha})")
        else:
            st.success(f"✅ No se rechaza H₀ — El estadístico Z={Z:.4f} no cae en la región de rechazo (α={alpha})")

        st.markdown("---")

        # Gráfica de la curva con región de rechazo
        st.subheader("Curva normal con región de rechazo")
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.set_facecolor("#000000")
        fig.patch.set_facecolor("#000000")

        x = np.linspace(-4, 4, 400)
        y = stats.norm.pdf(x)
        ax.plot(x, y, color="white", linewidth=2)

        if tipo == "Bilateral (≠)":
            ax.fill_between(x, y, where=(x <= -z_critico), color="#ef4444", alpha=0.6, label="Región de rechazo")
            ax.fill_between(x, y, where=(x >= z_critico), color="#ef4444", alpha=0.6)
            ax.fill_between(x, y, where=((x > -z_critico) & (x < z_critico)), color="#22c55e", alpha=0.3, label="No rechazo")
        elif tipo == "Cola izquierda (<)":
            ax.fill_between(x, y, where=(x <= z_critico), color="#ef4444", alpha=0.6, label="Región de rechazo")
            ax.fill_between(x, y, where=(x > z_critico), color="#22c55e", alpha=0.3, label="No rechazo")
        else:
            ax.fill_between(x, y, where=(x >= z_critico), color="#ef4444", alpha=0.6, label="Región de rechazo")
            ax.fill_between(x, y, where=(x < z_critico), color="#22c55e", alpha=0.3, label="No rechazo")

        ax.axvline(Z, color="#facc15", linewidth=2, linestyle="--", label=f"Z calculado = {Z:.4f}")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_edgecolor("white")
        ax.legend(facecolor="#1e1e1e", labelcolor="white")
        st.pyplot(fig)

        # Guarda resultados para el módulo de IA
        st.session_state.resultado_z = {
            "media_muestral": media_muestral,
            "mu0": mu0,
            "sigma": sigma,
            "n": n,
            "alpha": alpha,
            "tipo": tipo,
            "Z": Z,
            "z_critico": z_critico,
            "p_value": p_value,
            "rechaza": rechaza
        }

elif pagina == "Asistente IA":
    st.header("🤖 Asistente Estadístico con IA")

    import google.generativeai as genai

    if "gemini_key" not in st.session_state:
        st.session_state.gemini_key = ""

    api_key = st.text_input("🔑 Ingresa tu API Key de Gemini",
                             value=st.session_state.gemini_key,
                             type="password",
                             placeholder="AIza...")

    if api_key:
        st.session_state.gemini_key = api_key

    if not st.session_state.gemini_key:
        st.warning("⚠️ Ingresa tu API Key para continuar.")
        st.stop()

    genai.configure(api_key=st.session_state.gemini_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    opciones_ia = {
        "📊 Interpretar distribución": "distribucion",
        "🔬 Analizar Prueba Z": "prueba_z",
        "🔁 Comparar ambos análisis": "comparar"
    }

    seleccion = st.radio("¿Qué quieres que analice la IA?", list(opciones_ia.keys()), horizontal=True)
    modo = opciones_ia[seleccion]

    st.markdown("---")

    prompt = None
    listo = True

    if modo == "distribucion":
        if "sesgo" not in st.session_state:
            st.warning("⚠️ Primero genera datos y ve al módulo de Visualización.")
            listo = False
        else:
            prompt = f"""Soy estudiante de ingeniería y analicé una distribución de datos con los siguientes resultados estadísticos:
- Número de observaciones: {st.session_state.n}
- Media: {st.session_state.media:.4f}
- Desviación estándar: {st.session_state.desv:.4f}
- Sesgo: {st.session_state.sesgo:.4f}
- p-value prueba Shapiro-Wilk: {st.session_state.p_shapiro:.4f}

Con base en estos indicadores (NO en los datos crudos):
1. ¿La distribución parece normal? ¿Por qué?
2. ¿Hay sesgo relevante? ¿En qué dirección?
3. ¿Qué implicaciones prácticas tiene esto para un análisis estadístico?
Explica de forma clara y educativa."""

    elif modo == "prueba_z":
        if "resultado_z" not in st.session_state:
            st.warning("⚠️ Primero ejecuta una Prueba Z en el módulo correspondiente.")
            listo = False
        else:
            r = st.session_state.resultado_z
            prompt = f"""Soy estudiante de ingeniería y realicé una prueba de hipótesis Z con estos parámetros:
- Media muestral: {r['media_muestral']:.4f}
- Media hipotética H₀: {r['mu0']}
- Tamaño de muestra: {r['n']}
- Desviación estándar poblacional: {r['sigma']}
- Nivel de significancia α: {r['alpha']}
- Tipo de prueba: {r['tipo']}
- Estadístico Z calculado: {r['Z']:.4f}
- Z crítico: {r['z_critico']:.4f}
- p-value: {r['p_value']:.4f}
- Decisión automática: {"Se rechaza H₀" if r['rechaza'] else "No se rechaza H₀"}

Con base en esto:
1. ¿Se rechaza H₀? Justifica con el estadístico y el p-value.
2. ¿Los supuestos de la prueba Z son razonables dado el tamaño de muestra?
3. ¿Qué significa esta decisión en términos prácticos?
Explica de forma clara y educativa."""

    elif modo == "comparar":
        if "sesgo" not in st.session_state or "resultado_z" not in st.session_state:
            st.warning("⚠️ Necesitas haber pasado por Visualización y Prueba Z primero.")
            listo = False
        else:
            r = st.session_state.resultado_z
            prompt = f"""Soy estudiante de ingeniería. Analicé una distribución y realicé una prueba Z. Aquí el resumen:

DISTRIBUCIÓN:
- Observaciones: {st.session_state.n}
- Media: {st.session_state.media:.4f}
- Desviación estándar: {st.session_state.desv:.4f}
- Sesgo: {st.session_state.sesgo:.4f}
- p-value Shapiro-Wilk: {st.session_state.p_shapiro:.4f}

PRUEBA Z:
- H₀: µ = {r['mu0']} | Tipo: {r['tipo']} | α = {r['alpha']}
- Z calculado: {r['Z']:.4f} | Z crítico: {r['z_critico']:.4f}
- p-value: {r['p_value']:.4f}
- Decisión: {"Se rechaza H₀" if r['rechaza'] else "No se rechaza H₀"}

Con base en ambos análisis:
1. ¿La distribución era adecuada para aplicar una prueba Z?
2. ¿La decisión de la prueba es confiable dado el comportamiento de los datos?
3. ¿Qué conclusión general puedes dar sobre este análisis estadístico?
Explica de forma clara y educativa."""

    if listo and prompt:
        with st.expander("📋 Ver prompt enviado a la IA"):
            st.code(prompt)

        if st.button("🤖 Consultar a Gemini"):
            with st.spinner("Analizando con Gemini..."):
                try:
                    response = model.generate_content(prompt)
                    respuesta = response.text
                    st.session_state.respuesta_ia = respuesta

                    st.markdown("### 💬 Respuesta de Gemini")
                    st.markdown(respuesta)

                    if modo in ["prueba_z", "comparar"] and "resultado_z" in st.session_state:
                        st.markdown("---")
                        st.markdown("### App vs. IA")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**Decisión de la app:**")
                            if st.session_state.resultado_z['rechaza']:
                                st.error("❌ Se rechaza H₀")
                            else:
                                st.success("✅ No se rechaza H₀")
                        with col2:
                            st.markdown("**¿La IA coincide?**")
                            texto = respuesta.lower()
                            if st.session_state.resultado_z['rechaza'] and "rechaza" in texto:
                                st.success("✅ Coincide")
                            elif not st.session_state.resultado_z['rechaza'] and "no se rechaza" in texto:
                                st.success("✅ Coincide")
                            else:
                                st.warning("⚠️ Revisa manualmente")

                except Exception as e:
                    st.error(f"Error al consultar Gemini: {e}")