import streamlit as st
from src.controllers.auth_controller import AuthController
from src.controllers.scan_controller import ScanController
from src.views.login_ui import mostrar_login
from src.views.dashboard_ui import mostrar_dashboard_usuario
from src.views.admin_ui import mostrar_dashboard_admin
from src.views.theme import aplicar_estilo_personalizado

# 1. Configuración de página rápida
st.set_page_config(page_title="AnzenCore", layout="wide")
aplicar_estilo_personalizado()

# 2. Inicialización con Caché (Evita lentitud al recargar)
@st.cache_resource
def iniciar_controladores():
    return AuthController(), ScanController()

auth_ctrl, scan_ctrl = iniciar_controladores()

if 'user' not in st.session_state:
    st.session_state.user = None

if not st.session_state.user:
    mostrar_login(auth_ctrl)
else:
    # Solo marcamos online una vez por sesión para no saturar la red
    if 'online_set' not in st.session_state:
        auth_ctrl.marcar_online(st.session_state.user['id'], True)
        st.session_state.online_set = True
    
    st.sidebar.markdown("<h2 style='color:#00d4ff;'>🛡️ AnzenCore</h2>", unsafe_allow_html=True)
    st.sidebar.write(f"Usuario: **{st.session_state.user['nombre'].upper()}**")
    
    if st.sidebar.button("Cerrar Sesión"):
        auth_ctrl.marcar_online(st.session_state.user['id'], False)
        st.session_state.clear() # Limpia todo de golpe
        st.rerun()

    if st.session_state.user['rol_id'] == 1:
        mostrar_dashboard_admin(auth_ctrl)
    else:
        mostrar_dashboard_usuario(st.session_state.user, scan_ctrl)