import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# Configuración de la página
st.set_page_config(
    page_title="Ruta Ecológica LaPapaya - Dashboard de Control",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para branding LaPapaya (Colores ecológicos y profesionales)
st.markdown("""
    <style>
    .main-title {
        color: #1E5E3A;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: bold;
    }
    .metric-box {
        background-color: #F0F7F4;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 1. BASE DE DATOS DEL PROYECTO (Simulada con st.session_state para interactividad)
# ----------------------------------------------------

# Inicializar tareas de preparación en session_state si no existen
if 'tasks_df' not in st.session_state:
    tasks_data = [
        # Ensayos mensuales de Papayogging
        {"Fase": "Ensayos Mensuales", "Actividad": "1er Ensayo de Papayogging (Río Cali) - Ajuste de dinámicas", "Fecha Objetivo": "2026-07-25", "Estado": "Completado", "Responsable": "Felipe V."},
        {"Fase": "Ensayos Mensuales", "Actividad": "2do Ensayo de Papayogging (Río Cali) - Pruebas de pesaje", "Fecha Objetivo": "2026-08-29", "Estado": "Completado", "Responsable": "Guardianes del Río"},
        {"Fase": "Ensayos Mensuales", "Actividad": "3er Ensayo de Papayogging (Río Cali) - Logística de hidratación", "Fecha Objetivo": "2026-09-26", "Estado": "Pendiente", "Responsable": "Comité Deportivo"},
        {"Fase": "Ensayos Mensuales", "Actividad": "4to Ensayo de Papayogging (Río Cali) - Ensayo general de ruta completa", "Fecha Objetivo": "2026-10-31", "Estado": "Pendiente", "Responsable": "Felipe V."},
        
        # Actividades Críticas de Noviembre (Sábados de reunión)
        {"Fase": "Preparación Noviembre", "Actividad": "Reunión de Avance 1: Preparación de escenarios (Río Cali, Chontaduro, Calima), logística y permisos", "Fecha Objetivo": "2026-11-07", "Estado": "Pendiente", "Responsable": "Felipe V. / Logística"},
        {"Fase": "Preparación Noviembre", "Actividad": "Reunión de Avance 2: Instalación de señalización, pendones, códigos QR, mapas y puntos info", "Fecha Objetivo": "2026-11-14", "Estado": "Pendiente", "Responsable": "Equipo de Diseño & Campo"},
        {"Fase": "Preparación Noviembre", "Actividad": "Reunión de Avance 3: Capacitación de voluntarios, Guardianes del Río y aliados en protocolos y seguridad", "Fecha Objetivo": "2026-11-21", "Estado": "Pendiente", "Responsable": "Social / Voluntariado"},
        
        # Hitos de Venta del Proyecto
        {"Fase": "Estrategia de Venta", "Actividad": "Diseño de portafolio comercial de la Ruta Ecológica Calima para inversionistas/patrocinadores", "Fecha Objetivo": "2026-10-15", "Estado": "Pendiente", "Responsable": "Felipe V."},
        {"Fase": "Estrategia de Venta", "Actividad": "Envío de invitaciones personalizadas a tomadores de decisión para asistir a la Caminata en Calima", "Fecha Objetivo": "2026-11-10", "Estado": "Pendiente", "Responsable": "Felipe V."},
        {"Fase": "Estrategia de Venta", "Actividad": "Consolidación de indicadores en tiempo real post-piloto para dossier de venta", "Fecha Objetivo": "2026-12-08", "Estado": "Pendiente", "Responsable": "Comité de Evaluación"}
    ]
    st.session_state.tasks_df = pd.DataFrame(tasks_data)

# ----------------------------------------------------
# BARRA LATERAL (Filtros y Control de Avance de Tareas)
# ----------------------------------------------------
st.sidebar.image("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&q=80&w=300", caption="Asociación LaPapaya", use_container_width=True)
st.sidebar.markdown("## Panel de Control")
st.sidebar.markdown("Gestiona los estados de las tareas críticas previas al piloto de Noviembre/Diciembre.")

# Formulario rápido en el sidebar para actualizar o agregar tareas
st.sidebar.markdown("### Registrar Avance")
task_to_update = st.sidebar.selectbox("Selecciona una Actividad:", st.session_state.tasks_df["Actividad"].tolist())
new_status = st.sidebar.selectbox("Nuevo Estado:", ["Pendiente", "En Progreso", "Completado"])

if st.sidebar.button("Actualizar Estado"):
    idx = st.session_state.tasks_df[st.session_state.tasks_df["Actividad"] == task_to_update].index[0]
    st.session_state.tasks_df.at[idx, "Estado"] = new_status
    st.sidebar.success("¡Estado actualizado!")

# ----------------------------------------------------
# CUERPO PRINCIPAL DEL DASHBOARD
# ----------------------------------------------------
st.markdown("<h1 class='main-title'>🍃 Piloto Ruta Ecológica LaPapaya</h1>", unsafe_allow_html=True)
st.markdown("### Plan de Lanzamiento, Ensayos y Venta del Proyecto Calima")
st.write("---")

# Métricas de Progreso Superior
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
total_tasks = len(st.session_state.tasks_df)
completed_tasks = len(st.session_state.tasks_df[st.session_state.tasks_df["Estado"] == "Completado"])
pending_tasks = len(st.session_state.tasks_df[st.session_state.tasks_df["Estado"] == "Pendiente"])
progress_pct = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

with col_m1:
    st.markdown(f"<div class='metric-box'><h5>Total Actividades</h5><h2>{total_tasks}</h2></div>", unsafe_allow_html=True)
with col_m2:
    st.markdown(f"<div class='metric-box'><h5>Completadas</h5><h2>{completed_tasks}</h2></div>", unsafe_allow_html=True)
with col_m3:
    st.markdown(f"<div class='metric-box'><h5>Pendientes</h5><h2>{pending_tasks}</h2></div>", unsafe_allow_html=True)
with col_m4:
    st.markdown(f"<div class='metric-box'><h5>Progreso General</h5><h2>{progress_pct}%</h2></div>", unsafe_allow_html=True)

# ----------------------------------------------------
# SECCIÓN 1: CRONOGRAMA DE PREPARACIÓN E HITOS
# ----------------------------------------------------
st.markdown("## 📅 Cronograma de Preparación e Hitos Clave")

# Visualización gráfica del estado de las tareas
fig = px.bar(
    st.session_state.tasks_df, 
    y="Actividad", 
    x="Fase", 
    color="Estado", 
    title="Estado de las Tareas por Fase",
    color_discrete_map={"Pendiente": "#FF6B6B", "En Progreso": "#F4D03F", "Completado": "#2ECC71"},
    orientation="h"
)
fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
st.plotly_chart(fig, use_container_width=True)

# Tabla interactiva con filtro de fase
fases_disponibles = ["Todas"] + st.session_state.tasks_df["Fase"].unique().tolist()
selected_fase = st.selectbox("Filtrar por Fase de Preparación:", fases_disponibles)

if selected_fase == "Todas":
    display_df = st.session_state.tasks_df
else:
    display_df = st.session_state.tasks_df[st.session_state.tasks_df["Fase"] == selected_fase]

st.dataframe(
    display_df.style.map(
        lambda val: "background-color: #D4EDDA; color: #155724;" if val == "Completado" 
        else ("background-color: #FFF3CD; color: #856404;" if val == "En Progreso" else "background-color: #F8D7DA; color: #721C24;"),
        subset=["Estado"]
    ),
    use_container_width=True,
    hide_index=True
)

st.write("---")

# ----------------------------------------------------
# SECCIÓN 2: PROGRAMACIÓN DE LOS EVENTOS PILOTO (LOS 3 DÍAS)
# ----------------------------------------------------
st.markdown("## 🚀 Programación del Piloto de Lanzamiento")
st.write("Explora el itinerario detallado de cada una de las tres etapas de la ruta:")

tab1, tab2, tab3 = st.tabs([
    "🏃‍♂️ Día 1: Papayogging (Nov 28)", 
    "🍍 Día 2: Festival del Chontaduro (Nov 29)", 
    "⛰️ Día 3: Caminata Lago Calima (Dic 5)"
])

# Datos de los Itinerarios
dia1_data = {
    "Hora": ["07:00 AM", "07:30 AM", "07:45 AM", "08:00 AM", "09:30 AM", "10:00 AM", "11:00 AM", "12:00 PM"],
    "Actividad": [
        "Registro de participantes, entrega de pulsera, semilla de chontaduro y kit de limpieza.",
        "Bienvenida, presentación de los Guardianes del Río y recomendaciones de seguridad.",
        "Calentamiento dirigido.",
        "Inicio del Papayogging (Deporte + Recolección).",
        "Clasificación y pesaje de residuos recolectados.",
        "Jornada de siembra de árboles y plantas nativas.",
        "Café Circular: reflexión y debate sobre el futuro del Río Cali.",
        "Cierre de la jornada y fotografía oficial grupal."
    ],
    "Responsable": ["Logística", "Felipe V.", "Fisioterapeuta", "Todo el equipo", "Ambiental", "Guardianes del Río", "Felipe V.", "Comunicaciones"]
}

dia2_data = {
    "Hora": ["08:00 AM", "08:30 AM", "09:30 AM", "10:30 AM", "11:30 AM", "12:30 PM", "02:00 PM", "03:30 PM", "04:30 PM"],
    "Actividad": [
        "Apertura del Festival y bienvenida al público asistente.",
        "Recorrido por la muestra gastronómica y emprendimientos de la comunidad local.",
        "Charlas académicas sobre patrimonio, biodiversidad y economía circular.",
        "Actividades culturales, danzas y presentaciones artísticas.",
        "Concurso gastronómico del Chontaduro y premiación.",
        "Almuerzo comunitario y de integración.",
        "Café Circular con líderes comunitarios, academia y sector público.",
        "Construcción y firma de compromisos para fortalecer la Ruta del Chontaduro.",
        "Cierre oficial del Festival del Chontaduro."
    ],
    "Responsable": ["Comunidad", "Emprendedores", "Academia / Invitados", "Artistas", "Jurados", "Logística Cocina", "Felipe V. / Aliados", "Líderes de Ruta", "Coordinación"]
}

dia3_data = {
    "Hora": ["07:30 AM", "08:00 AM", "08:30 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:30 PM", "02:30 PM", "03:30 PM"],
    "Actividad": [
        "Registro de participantes y bienvenida en el punto de encuentro.",
        "Presentación del Lago Calima y del modelo de la Ruta Ecológica LaPapaya.",
        "Caminata ecológica guiada e interpretación ambiental de flora y fauna.",
        "Observación de biodiversidad y espacio de fotografía de naturaleza.",
        "Actividad de restauración ambiental y siembra en el área de influencia del lago.",
        "Almuerzo campestre.",
        "Café Circular: Oportunidades del turismo sostenible y escalabilidad en Calima.",
        "Evaluación participativa del piloto y recolección de sugerencias.",
        "Compromisos ambientales de cierre y clausura de la Ruta Ecológica Piloto."
    ],
    "Responsable": ["Registro", "Felipe V.", "Guías Locales", "Fotógrafos", "Equipo de Reforestación", "Catering", "Inversionistas / Felipe V.", "Evaluadores", "Asociación LaPapaya"]
}

with tab1:
    st.markdown("#### **Día 1: Papayogging – Guardianes del Río Cali**")
    st.caption("Objetivo: Movilizar a la ciudadanía para la recuperación del Río Cali mediante deporte, voluntariado y educación ambiental.")
    st.table(pd.DataFrame(dia1_data))

with tab2:
    st.markdown("#### **Día 2: Festival del Chontaduro**")
    st.caption("Objetivo: Promover el patrimonio cultural y gastronómico del chontaduro como motor de desarrollo sostenible para el territorio.")
    st.table(pd.DataFrame(dia2_data))

with tab3:
    st.markdown("#### **Día 3: Caminata Ecológica – Lago Calima**")
    st.caption("Objetivo (Clave para Venta): Validar el modelo de turismo regenerativo y demostrar la viabilidad comercial y ambiental a inversores.")
    st.table(pd.DataFrame(dia3_data))

st.write("---")

# ----------------------------------------------------
# SECCIÓN 3: MÉTRICAS DE IMPACTO PROPUESTAS PARA LA VENTA
# ----------------------------------------------------
st.markdown("## 📊 Indicadores de Éxito en Tiempo Real (Para la Venta del Proyecto)")
st.write("Estos indicadores demostrarán a los futuros compradores/inversionistas la tracción y viabilidad del modelo:")

col_e1, col_e2, col_e3, col_e4 = st.columns(4)

with col_e1:
    meta_asistencia = st.number_input("Meta de Asistentes Totales", value=350, step=50)
    st.metric("Asistencia Proyectada", f"{meta_asistencia} pax", "+15% vs Histórico")

with col_e2:
    meta_residuos = st.number_input("Meta Residuos Recuperados (Kg)", value=120, step=10)
    st.metric("Meta de Limpieza", f"{meta_residuos} Kg", "Objetivo Río Cali")

with col_e3:
    meta_arboles = st.number_input("Árboles a Sembrar", value=80, step=10)
    st.metric("Reforestación Activa", f"{meta_arboles} plántulas", "Especies Nativas")

with col_e4:
    st.metric("Nivel de Satisfacción Esperado", ">= 92%", "Encuestas Digitales QR")

st.markdown("""
> 💡 **Nota de Estrategia para Felipe**: Durante el *Café Circular del Día 3 en Calima*, utiliza estos indicadores proyectados (y los reales que vayas midiendo) para consolidar tu pitch de venta. Mostrar datos exactos de impacto ambiental y participación comunitaria es lo que convencerá a los inversionistas de que la Ruta Ecológica es un modelo escalable y altamente rentable a nivel social y de marca.
""")